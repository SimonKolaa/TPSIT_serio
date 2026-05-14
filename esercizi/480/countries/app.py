from zeep import Client
from zeep.exceptions import Fault
from flask import Flask, request, render_template

app = Flask(__name__)

# soap service
url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"

OPERATIONS = [
    ("CapitalCity", "Capital City"),
    ("CountryIntPhoneCode", "Prefisso Internazionale"),
    ("FullCountryInfo", "Informazioni Complete"),
]


def getAllISOCodes(client):
    return client.service.ListOfCountryNamesByCode()


def object_to_dict(value):
    if value is None:
        return None
    if isinstance(value, (str, int, float, bool)):
        return value
    if hasattr(value, "__iter__") and not isinstance(value, (str, bytes, dict)):
        try:
            return [object_to_dict(item) for item in value]
        except TypeError:
            pass
    if hasattr(value, "__dict__"):
        result = {}
        for key in [k for k in dir(value) if not k.startswith("_") and not callable(getattr(value, k))]:
            try:
                result[key] = object_to_dict(getattr(value, key))
            except Exception:
                result[key] = str(getattr(value, key))
        return result
    if isinstance(value, dict):
        return {k: object_to_dict(v) for k, v in value.items()}
    return str(value)


def get_service_result(client, service_name, iso_code):
    if service_name == "CapitalCity":
        return client.service.CapitalCity(iso_code)
    if service_name == "CountryIntPhoneCode":
        return client.service.CountryIntPhoneCode(iso_code)
    if service_name == "FullCountryInfo":
        return client.service.FullCountryInfo(iso_code)
    raise ValueError(f"Operazione non supportata: {service_name}")


@app.route("/", methods=["GET", "POST"])
def load():
    error = None
    response = None
    selected_iso = ""
    selected_service = OPERATIONS[0][0]
    try:
        client = Client(wsdl=url)
        countries = getAllISOCodes(client)
        oplist = [op[0] for op in OPERATIONS]

        if request.method == "POST":
            selected_iso = request.form.get("isocode", "").strip()
            selected_service = request.form.get("service", selected_service)

            if not selected_iso:
                error = "Inserisci un codice ISO valido."
            else:
                try:
                    response = get_service_result(client, selected_service, selected_iso)
                    if selected_service == "FullCountryInfo":
                        response = object_to_dict(response)
                except Fault as exception:
                    error = f"Errore SOAP: {exception.message if hasattr(exception, 'message') else exception}"
                except Exception as exception:
                    error = str(exception)

        return render_template(
            "home.html.jinja",
            countries=countries,
            oplist=oplist,
            operations=OPERATIONS,
            selected_service=selected_service,
            selected_iso=selected_iso,
            response=response,
            error=error,
        )
    except Fault as exception:
        return f"Errore SOAP: {exception}"
    except Exception as exception:
        return f"Errore server: {exception}"

# pip install zeep
# rif. https://docs.python-zeep.org/en/master/
if __name__ == "__main__":
    app.run()