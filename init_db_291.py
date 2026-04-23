import sqlite3

DATABASE = '291.sqlite'

def init_db():
    """Inizializza il database SQLite"""
    conn = sqlite3.connect(DATABASE)
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
        print("✓ Utenti inseriti")
    
    cursor.execute('SELECT COUNT(*) FROM giochi')
    if cursor.fetchone()[0] == 0:
        giochi = ['Super Mario Bros', 'Pac-Man', 'Space Invaders', 'Tetris', 'Donkey Kong']
        for gioco in giochi:
            cursor.execute("INSERT INTO giochi (nome) VALUES (?)", (gioco,))
        print("✓ Giochi inseriti")
    
    conn.commit()
    conn.close()
    print(f"✓ Database {DATABASE} creato/aggiornato con successo!")

if __name__ == '__main__':
    init_db()
