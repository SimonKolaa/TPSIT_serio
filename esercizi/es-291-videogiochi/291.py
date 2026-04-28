from flask import Flask, request, render_template, Response
import sqlite3
import json

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('informatica.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS prodotti (
            codice TEXT PRIMARY KEY,
            prezzo REAL,
            marca TEXT,
            modello TEXT
        )
    ''')
    cursor.execute('INSERT OR IGNORE INTO prodotti VALUES ("A123", 1299.99, "Asus", "Zenbook 14")')
    cursor.execute('INSERT OR IGNORE INTO prodotti VALUES ("B456", 899.50, "Dell", "Inspiron 15")')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('291_index.html')

@app.route('/api/prodotto', methods=['GET'])
def get_prodotto():
    codice = request.args.get('codice', '').upper()
    
    conn = sqlite3.connect('informatica.db')
    cursor = conn.cursor()
    cursor.execute('SELECT prezzo, marca, modello FROM prodotti WHERE codice = ?', (codice,))
    prodotto = cursor.fetchone()
    conn.close()

    if prodotto:
        # Creiamo un dizionario e lo convertiamo in formato JSON
        dati = {
            "prezzo": prodotto[0],
            "marca": prodotto[1],
            "modello": prodotto[2]
        }
        return Response(json.dumps(dati), mimetype='application/json')
    else:
        return Response(json.dumps({"errore": "Prodotto non trovato"}), mimetype='application/json', status=404)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)