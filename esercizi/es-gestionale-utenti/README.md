# Esercizio - Gestionale Utenti REST API

## Descrizione
Applicazione web CRUD per la gestione di utenti con architettura REST e interfaccia AJAX.

## Funzionalità

### Operazioni CRUD
- **GET /users/** - Visualizza lista di tutti gli utenti
- **GET /users/<id>** - Visualizza dettagli di un utente
- **POST /users/** - Crea un nuovo utente
- **PUT /users/<id>** - Modifica un utente esistente
- **DELETE /users/<id>** - Elimina un utente

### Codici HTTP Restituiti
- **200 OK** - Operazione riuscita (GET, PUT)
- **201 Created** - Utente creato (POST)
- **204 No Content** - Utente eliminato (DELETE)
- **400 Bad Request** - Dati non validi
- **404 Not Found** - Utente non trovato
- **405 Method Not Allowed** - Metodo HTTP non consentito

### Validazione
- **Nome/Cognome**: 2-50 caratteri, solo lettere e spazi
- **Data di Nascita**: Formato YYYY-MM-DD
- **Mansione**: Minimo 2 caratteri

## Tecnologie Utilizzate
- **Backend**: Python + Flask
- **Frontend**: HTML5 + CSS3
- **Client-side**: AJAX (XMLHttpRequest) + JavaScript ES5
- **Persistenza**: JSON (users.json)
- **Validazione**: Regex

## Struttura del Progetto
```
es-gestionale-utenti/
├── app.py                 # Back-end Flask (Front Controller)
├── users.json             # Archivio dati utenti
├── requirements.txt       # Dipendenze Python
├── templates/
│   └── index.html         # Pagina principale HTML
└── static/
    └── app.js             # Logica AJAX e client-side ES5
```

## Installazione e Avvio

### 1. Installare le dipendenze
```bash
pip install -r requirements.txt
```

### 2. Avviare l'applicazione
```bash
python app.py
```

### 3. Accedere all'applicazione
Aprire il browser e navigare a:
```
http://localhost:5000/gestionale_utenti/
```

## Utilizzo

### Inserire un nuovo utente
1. Compilare il form "Inserisci Nuovo Utente" con i dati richiesti
2. Cliccare su "Inserisci Utente"
3. Se valido, l'utente sarà aggiunto alla lista

### Visualizzare dettaglio utente
1. Cliccare il pulsante "Dettaglio" accanto all'utente nella tabella
2. Si aprirà una finestra modale con i dati completi

### Modificare un utente
1. Cliccare il pulsante "Modifica" accanto all'utente
2. Modificare i dati nel form che appare in modale
3. Cliccare "Salva Modifiche" per confermare

### Eliminare un utente
1. Cliccare il pulsante "Elimina" accanto all'utente
2. Confermare l'eliminazione nel popup
3. L'utente sarà rimosso dalla lista

## Note Tecniche

### Front Controller Pattern
- `app.py` contiene tutte le rotte REST
- Usa `request.method` per distinguere GET, POST, PUT, DELETE
- Utilizza `request.args` per parametri GET
- Utilizza `request.get_json()` per body JSON

### AJAX ES5
- Implementato con `XMLHttpRequest` (no fetch API)
- Separazione chiara tra logica di richiesta e UI
- Gestione errori centralizzata
- Validazione client-side con regex

### Persistenza
- I dati sono salvati in `users.json`
- Struttura dati: array di oggetti con campi id, nome, cognome, data_nascita, mansione
- ID auto-incrementante

## Esercizi di Approfondimento

1. Aggiungere paginazione alla lista degli utenti
2. Implementare ricerca/filtro per nome o cognome
3. Aggiungere sorting per colonna
4. Aggiungere campo email con validazione regex più robusta
5. Implementare autenticazione semplice
6. Aggiungere backup automatico del file JSON
7. Creare API endpoint per statistiche (età media, mansioni più comuni, etc.)
