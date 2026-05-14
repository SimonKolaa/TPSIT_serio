import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

SOAP_URL = 'http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso'
SOAP_NAMESPACE = 'http://www.oorsprong.org/websamples.countryinfo'

COUNTRY_CACHE = None


def soap_request(body):
    headers = {
        'Content-Type': 'application/soap+xml; charset=utf-8',
        'Content-Length': str(len(body)),
    }
    request_obj = urllib.request.Request(SOAP_URL, data=body.encode('utf-8'), headers=headers, method='POST')
    try:
        with urllib.request.urlopen(request_obj, timeout=20) as response:
            return response.read()
    except urllib.error.HTTPError as e:
        return e.read()
    except Exception as e:
        raise RuntimeError('Errore di comunicazione con il servizio SOAP: %s' % e)


def parse_xml(xml_bytes):
    try:
        return ET.fromstring(xml_bytes)
    except ET.ParseError as e:
        raise RuntimeError('Impossibile leggere la risposta SOAP: %s' % e)


def get_country_list():
    global COUNTRY_CACHE
    if COUNTRY_CACHE is not None:
        return COUNTRY_CACHE

    body = (
        '<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" '
        'xmlns:m="%s">'
        '<soap:Body>'
        '<m:ListOfCountryNamesByCode/>'
        '</soap:Body>'
        '</soap:Envelope>'
    ) % SOAP_NAMESPACE

    xml = parse_xml(soap_request(body))
    result = []
    for item in xml.findall('.//{http://www.oorsprong.org/websamples.countryinfo}tCountryCodeAndName'):
        code = item.find('{http://www.oorsprong.org/websamples.countryinfo}sISOCode')
        name = item.find('{http://www.oorsprong.org/websamples.countryinfo}sName')
        if code is not None and name is not None:
            result.append({
                'code': code.text or '',
                'name': name.text or '',
                'flag_url': f'https://flagpedia.net/data/flags/w40/{(code.text or "").lower()}.png'
            })

    COUNTRY_CACHE = sorted(result, key=lambda x: x['name'])
    return COUNTRY_CACHE


def call_service(code, service):
    if service == 'CapitalCity':
        body = (
            '<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" '
            'xmlns:m="%s">'
            '<soap:Body>'
            '<m:CapitalCity>'
            '<m:sCountryISOCode>%s</m:sCountryISOCode>'
            '</m:CapitalCity>'
            '</soap:Body>'
            '</soap:Envelope>'
        ) % (SOAP_NAMESPACE, code)
        xml = parse_xml(soap_request(body))
        node = xml.find('.//{http://www.oorsprong.org/websamples.countryinfo}CapitalCityResult')
        return node.text if node is not None else None

    if service == 'CountryIntPhoneCode':
        body = (
            '<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" '
            'xmlns:m="%s">'
            '<soap:Body>'
            '<m:CountryIntPhoneCode>'
            '<m:sCountryISOCode>%s</m:sCountryISOCode>'
            '</m:CountryIntPhoneCode>'
            '</soap:Body>'
            '</soap:Envelope>'
        ) % (SOAP_NAMESPACE, code)
        xml = parse_xml(soap_request(body))
        node = xml.find('.//{http://www.oorsprong.org/websamples.countryinfo}CountryIntPhoneCodeResult')
        return node.text if node is not None else None

    if service == 'FullCountryInfo':
        body = (
            '<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" '
            'xmlns:m="%s">'
            '<soap:Body>'
            '<m:FullCountryInfo>'
            '<m:sCountryISOCode>%s</m:sCountryISOCode>'
            '</m:FullCountryInfo>'
            '</soap:Body>'
            '</soap:Envelope>'
        ) % (SOAP_NAMESPACE, code)
        xml = parse_xml(soap_request(body))
        result_node = xml.find('.//{http://www.oorsprong.org/websamples.countryinfo}FullCountryInfoResult')
        if result_node is None:
            return None
        result = {}
        for child in result_node:
            tag = child.tag.split('}')[-1]
            if len(child):
                # Use simple text for nested elements or list values
                if tag == 'Languages':
                    languages = []
                    for item in child.findall('.//{http://www.oorsprong.org/websamples.countryinfo}sName'):
                        languages.append(item.text or '')
                    result[tag] = ', '.join([x for x in languages if x])
                else:
                    result[tag] = child.text or ''
            else:
                result[tag] = child.text or ''
        return result

    raise ValueError('Servizio non supportato: %s' % service)


@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    result = None
    selected_service = 'CapitalCity'
    selected_code = ''
    country_list = []

    try:
        country_list = get_country_list()
    except Exception as exc:
        error = str(exc)
        country_list = []

    if request.method == 'POST':
        selected_code = request.form.get('iso_code', '').strip().upper()
        selected_service = request.form.get('service', 'CapitalCity')

        if not selected_code:
            error = 'Devi selezionare un codice ISO dalla lista.'
        else:
            try:
                value = call_service(selected_code, selected_service)
                if value is None:
                    error = 'Nessun risultato ottenuto dal servizio.'
                else:
                    result = {'service': selected_service, 'code': selected_code, 'value': value}
            except Exception as exc:
                error = str(exc)

        try:
            country_list = get_country_list()
        except Exception:
            # Usa comunque la lista caricata inizialmente se possibile
            pass

    return render_template(
        'index.html',
        countries=country_list,
        error=error,
        result=result,
        selected_service=selected_service,
        selected_code=selected_code,
    )


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
