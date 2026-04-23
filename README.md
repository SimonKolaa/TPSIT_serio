# TPSIT - Tecnologie e Progettazione di Sistemi Informatici e di Telecomunicazione

Repository contenente gli esercizi svolti durante il corso di TPSIT.

## Struttura del Repository

```
esercizi/
├── es-002-comuni/              # Esercizio 2: Ricerca comuni (HTML, Database)
│   ├── dettagio_es2.html
│   ├── index_es2.html
│   └── risultati_es2.html
│
├── es-003-socket/              # Esercizio 3: Socket TCP/UDP con Python
│   ├── client_es3.py
│   ├── server_es3.py
│   ├── client_udp.py
│   ├── server_udp.py
│   └── templates/
│
├── es-291-videogiochi/         # Esercizio 291: Gestione punteggi videogiochi
│   ├── 291.py                  # App Flask principale
│   ├── 291.sqlite              # Database SQLite
│   ├── init_db_291.py          # Script di inizializzazione database
│   └── templates/
│       ├── 291_index.html      # Pagina di login
│       └── 291_dashboard.html  # Dashboard dopo login
│
├── es-app-biblioteca/          # App: Gestione biblioteca (Flask)
│   ├── app.py
│   └── templates/
│       ├── biblioteca.json
│       ├── inserisci_libro.html
│       ├── visualizza_biblioteca.html
│       ├── registrazione_studente.html
│       ├── risultato_studente.html
│       └── studenti.json
│
├── es-verifica/                # Esercizio di verifica
│   ├── es_verifica.py
│   ├── client_verifica.py
│   └── server_studenti.py
│
└── es-supporto/                # File di supporto e utility
    ├── client_flexible.py
    ├── client1.py
    ├── Kola_espreg.py
    ├── main.py
    ├── moto.py
    ├── server_esempio.py
    ├── test_socket.py
    └── [file XML, XSD, MD e testo di supporto]
```

## Descrizione Esercizi

### Es-002: Comuni
Sistema di ricerca comuni con database. **File:** HTML files

### Es-003: Socket TCP/UDP
Implementazione di client e server in Python.

### Es-291: Gestione Videogiochi
Applicazione Flask con autenticazione e database SQLite.
- **Tecnologie:** Python, Flask, SQLite
- **Avvio:** `python esercizi/es-291-videogiochi/291.py`

### Es-App-Biblioteca
Applicazione Flask per gestione biblioteca.
- **Avvio:** `python esercizi/es-app-biblioteca/app.py`

## Installazione Dipendenze

```bash
pip install flask
```

## License

MIT License
