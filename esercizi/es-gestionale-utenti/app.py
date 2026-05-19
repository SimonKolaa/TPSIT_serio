import flask
import json
import os
import re
from datetime import datetime

app = flask.Flask(__name__)

# Percorso file JSON
USERS_FILE = os.path.join(os.path.dirname(__file__), 'users.json')

# Regex pattern per validazione
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
NAME_REGEX = r'^[a-zA-Z\s]{2,50}$'
DATE_REGEX = r'^\d{4}-\d{2}-\d{2}$'

def carica_utenti():
    """Carica gli utenti dal file JSON"""
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except:
                return []
    return []

def salva_utenti(utenti):
    """Salva gli utenti nel file JSON"""
    with open(USERS_FILE, 'w', encoding='utf-8') as f:
        json.dump(utenti, f, indent=2, ensure_ascii=False)

def genera_id():
    """Genera un nuovo ID unico"""
    utenti = carica_utenti()
    if not utenti:
        return 1
    return max(u['id'] for u in utenti) + 1

def valida_utente(data):
    """Valida i dati dell'utente"""
    errori = []
    
    if 'nome' not in data or not re.match(NAME_REGEX, data['nome'].strip()):
        errori.append('Nome non valido (2-50 caratteri, solo lettere e spazi)')
    
    if 'cognome' not in data or not re.match(NAME_REGEX, data['cognome'].strip()):
        errori.append('Cognome non valido (2-50 caratteri, solo lettere e spazi)')
    
    if 'data_nascita' not in data or not re.match(DATE_REGEX, data['data_nascita']):
        errori.append('Data di nascita non valida (formato: YYYY-MM-DD)')
    else:
        try:
            datetime.strptime(data['data_nascita'], '%Y-%m-%d')
        except:
            errori.append('Data di nascita non valida')
    
    if 'mansione' not in data or len(data['mansione'].strip()) < 2:
        errori.append('Mansione non valida (minimo 2 caratteri)')
    
    return errori

@app.route('/gestionale_utenti/')
def index():
    """Pagina principale"""
    return flask.render_template('index.html')

@app.route('/users/', methods=['GET', 'POST'])
def users_list():
    """
    GET: Restituisce la lista di tutti gli utenti
    POST: Crea un nuovo utente
    """
    if flask.request.method == 'GET':
        utenti = carica_utenti()
        return flask.jsonify(utenti), 200
    
    elif flask.request.method == 'POST':
        data = flask.request.get_json()
        
        if not data:
            return flask.jsonify({'errore': 'Dati mancanti'}), 400
        
        # Valida i dati
        errori = valida_utente(data)
        if errori:
            return flask.jsonify({'errori': errori}), 400
        
        # Crea il nuovo utente
        utenti = carica_utenti()
        nuovo_utente = {
            'id': genera_id(),
            'nome': data['nome'].strip(),
            'cognome': data['cognome'].strip(),
            'data_nascita': data['data_nascita'],
            'mansione': data['mansione'].strip()
        }
        
        utenti.append(nuovo_utente)
        salva_utenti(utenti)
        
        return flask.jsonify(nuovo_utente), 201
    
    return '', 405

@app.route('/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def user_detail(user_id):
    """
    GET: Restituisce i dettagli di un utente
    PUT: Modifica un utente
    DELETE: Elimina un utente
    """
    utenti = carica_utenti()
    utente = next((u for u in utenti if u['id'] == user_id), None)
    
    if not utente:
        return flask.jsonify({'errore': 'Utente non trovato'}), 404
    
    if flask.request.method == 'GET':
        return flask.jsonify(utente), 200
    
    elif flask.request.method == 'PUT':
        data = flask.request.get_json()
        
        if not data:
            return flask.jsonify({'errore': 'Dati mancanti'}), 400
        
        # Valida i dati
        errori = valida_utente(data)
        if errori:
            return flask.jsonify({'errori': errori}), 400
        
        # Aggiorna l'utente
        utente['nome'] = data['nome'].strip()
        utente['cognome'] = data['cognome'].strip()
        utente['data_nascita'] = data['data_nascita']
        utente['mansione'] = data['mansione'].strip()
        
        salva_utenti(utenti)
        
        return flask.jsonify(utente), 200
    
    elif flask.request.method == 'DELETE':
        utenti = [u for u in utenti if u['id'] != user_id]
        salva_utenti(utenti)
        
        return '', 204
    
    return '', 405

@app.errorhandler(405)
def metodo_non_consentito(e):
    """Gestisce errore 405 Method Not Allowed"""
    return flask.jsonify({'errore': 'Metodo HTTP non consentito'}), 405

@app.errorhandler(404)
def non_trovato(e):
    """Gestisce errore 404 Not Found"""
    return flask.jsonify({'errore': 'Risorsa non trovata'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
