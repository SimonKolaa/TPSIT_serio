from flask import Flask, render_template, request
from zeep import Client

app = Flask(__name__, template_folder='templates')

SOAP_WSDL = 'http://www.dneonline.com/calculator.asmx?wsdl'
_client = None


def get_client():
    global _client
    if _client is None:
        _client = Client(SOAP_WSDL)
    return _client


def soap_calculate(operation, a, b):
    client = get_client()
    try:
        if operation == 'Add':
            return client.service.Add(a, b)
        if operation == 'Subtract':
            return client.service.Subtract(a, b)
        if operation == 'Multiply':
            return client.service.Multiply(a, b)
        if operation == 'Divide':
            return client.service.Divide(a, b)
        raise ValueError('Operazione non valida: %s' % operation)
    except Exception as exc:
        raise RuntimeError('Errore SOAP: %s' % exc)


@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    result = None
    int_a = ''
    int_b = ''
    operation = 'Add'
    operations = [
        ('Add', 'Addizione'),
        ('Subtract', 'Sottrazione'),
        ('Multiply', 'Moltiplicazione'),
        ('Divide', 'Divisione'),
    ]

    if request.method == 'POST':
        int_a = request.form.get('intA', '').strip()
        int_b = request.form.get('intB', '').strip()
        operation = request.form.get('operation', 'Add')

        if int_a == '' or int_b == '':
            error = 'Inserisci entrambi i valori numerici.'
        else:
            try:
                if operation not in [op[0] for op in operations]:
                    raise ValueError('Operazione non valida.')
                a = int(int_a)
                b = int(int_b)
                result = soap_calculate(operation, a, b)
            except ValueError:
                error = 'I valori devono essere numeri interi e l’operazione deve essere valida.'
            except RuntimeError as exc:
                error = str(exc)

    return render_template(
        'index.html',
        intA=int_a,
        intB=int_b,
        operation=operation,
        operations=operations,
        result=result,
        error=error,
    )


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
