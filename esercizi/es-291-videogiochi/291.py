from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

DATABASE = '291.sqlite'

def get_db():
    """Ottiene una connessione al database SQLite"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Inizializza il database con le tabelle"""
    conn = get_db()
    cursor = conn.cursor()
    
    # Tabella utenti
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS utenti (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    
    # Tabella giochi
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS giochi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
    ''')
    
    # Tabella punteggi
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS punteggi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            utente_id INTEGER NOT NULL,
            gioco_id INTEGER NOT NULL,
            punteggio INTEGER NOT NULL,
            data_ora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (utente_id) REFERENCES utenti(id),
            FOREIGN KEY (gioco_id) REFERENCES giochi(id)
        )
    ''')
    
    # Inserisci dati iniziali
    cursor.execute('SELECT COUNT(*) FROM utenti')
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO utenti (username, password) VALUES (?, ?)", ('mario', 'mario123'))
        cursor.execute("INSERT INTO utenti (username, password) VALUES (?, ?)", ('luigi', 'luigi123'))
    
    cursor.execute('SELECT COUNT(*) FROM giochi')
    if cursor.fetchone()[0] == 0:
        giochi = ['Super Mario Bros', 'Pac-Man', 'Space Invaders', 'Tetris', 'Donkey Kong']
        for gioco in giochi:
            cursor.execute("INSERT INTO giochi (nome) VALUES (?)", (gioco,))
    
    conn.commit()
    conn.close()

# Inizializza il database all'avvio
if not os.path.exists(DATABASE):
    init_db()

@app.route('/')
def index():
    """Pagina iniziale con form di login"""
    if 'utente_id' in session:
        return redirect(url_for('dashboard'))
    return render_template('291_index.html')

@app.route('/login', methods=['POST'])
def login():
    """Gestisce il login dell'utente"""
    username = request.form.get('username')
    password = request.form.get('password')
    
    if not username or not password:
        return render_template('291_index.html', error='Inserisci username e password')
    
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM utenti WHERE username = ? AND password = ?', (username, password))
    utente = cursor.fetchone()
    conn.close()
    
    if utente:
        session['utente_id'] = utente['id']
        session['username'] = utente['username']
        return redirect(url_for('dashboard'))
    else:
        return render_template('291_index.html', error='Username o password errati')

@app.route('/dashboard')
def dashboard():
    """Dashboard principale dopo il login"""
    if 'utente_id' not in session:
        return redirect(url_for('index'))
    
    conn = get_db()
    cursor = conn.cursor()
    
    # Ottieni lista giochi
    cursor.execute('SELECT * FROM giochi ORDER BY nome')
    giochi = cursor.fetchall()
    
    # Ottieni punteggi dell'utente
    cursor.execute('''
        SELECT p.*, g.nome as nome_gioco, p.id as ultimo_id
        FROM punteggi p
        JOIN giochi g ON p.gioco_id = g.id
        WHERE p.utente_id = ?
        ORDER BY p.data_ora DESC
    ''', (session['utente_id'],))
    punteggi = cursor.fetchall()
    
    conn.close()
    
    return render_template('291_dashboard.html', 
                         giochi=giochi, 
                         punteggi=punteggi,
                         username=session['username'])

@app.route('/inserisci_punteggio', methods=['POST'])
def inserisci_punteggio():
    """Inserisce un nuovo punteggio"""
    if 'utente_id' not in session:
        return redirect(url_for('index'))
    
    gioco_id = request.form.get('gioco_id')
    punteggio = request.form.get('punteggio')
    
    if not gioco_id or not punteggio:
        return redirect(url_for('dashboard'))
    
    try:
        punteggio = int(punteggio)
        gioco_id = int(gioco_id)
    except ValueError:
        return redirect(url_for('dashboard'))
    
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO punteggi (utente_id, gioco_id, punteggio)
        VALUES (?, ?, ?)
    ''', (session['utente_id'], gioco_id, punteggio))
    conn.commit()
    conn.close()
    
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    """Effettua il logout"""
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
