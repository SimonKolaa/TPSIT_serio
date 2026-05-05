# Esercizio 302: Concessionaria Auto Usate

## Descrizione
Questo esercizio crea una pagina web interattiva per cercare auto usate in una concessionaria. La ricerca avviene tramite una form che comunica con il server via AJAX.

## Struttura del progetto

```
es-302-auto-usate/
├── app.py                 # Script Flask per il server
├── data/
│   └── auto.json          # Database JSON con le auto disponibili
├── templates/
│   └── index.html         # Pagina HTML principale con form e AJAX
└── img/                   # Cartella per le immagini (placeholder)
```

## Come funziona

### Lato Server (Python - Flask)
- Legge il file JSON con le auto disponibili
- Riceve i parametri di filtro dalla form (marca, modello, alimentazione, colore)
- Filtra la lista in base ai criteri (ricerca case-insensitive)
- Restituisce i risultati in formato JSON

### Lato Client (HTML/JavaScript)
- Form con 4 campi di input per i filtri
- XMLHttpRequest per inviare dati al server in AJAX
- Decodifica la risposta JSON e visualizza i risultati in una tabella
- CSS moderno e responsive per la formattazione

## Prerequisiti

- Python 3.x
- Flask (`pip install flask`)

## Come eseguire

1. **Installa Flask** (se non lo hai ancora):
   ```bash
   pip install flask
   ```

2. **Naviga nella cartella del progetto**:
   ```bash
   cd esercizi/es-302-auto-usate
   ```

3. **Avvia il server**:
   ```bash
   python app.py
   ```

4. **Apri il browser**:
   - Vai a `http://localhost:5000`

## Caratteristiche implementate

✅ **Form di ricerca** con i campi:
- Marca
- Modello
- Alimentazione (dropdown con opzioni: Diesel, Benzina, Hybrid)
- Colore

✅ **Database JSON**:
- 15 auto diverse per combinazioni di parametri
- Ogni auto contiene: marca, modello, alimentazione, colore, immagine

✅ **AJAX**:
- XMLHttpRequest per comunicazione client-server senza ricaricare la pagina
- Gestione della risposta JSON

✅ **Risultati tabulari**:
- Tabella con colonne per marca, modello, alimentazione, colore, immagine
- Mostra il numero di risultati trovati
- Messaggio se nessun veicolo corrisponde ai criteri

✅ **CSS professionale**:
- Gradiente di colore (viola)
- Layout responsive
- Hover effects
- Visualizzazione mobile-friendly
- Animazioni e transizioni

✅ **Gestione errori**:
- Messaggi di errore se la connessione fallisce
- Indicatore di caricamento
- Try/catch per errori JSON

## Filtri di ricerca

I filtri funzionano come seguente:
- Se vuoti, tutti i valori sono accettati
- La ricerca è case-insensitive (maiuscole/minuscole non importano)
- Si possono combinare più filtri

**Esempi di ricerca**:
- Marca "Fiat" → tutte le Fiat
- Marca "Ford" + Alimentazione "Diesel" → solo Ford diesel
- Colore "Rosso" → tutte le auto rosse

## Note tecniche

- **JavaScript**: Usa ES5 (no arrow functions, no const/let con block scope)
- **AJAX**: Implementato con XMLHttpRequest (no fetch API)
- **JSON**: Utilizzato sia per il database che per le risposte
- **Flask**: Framework web Python leggero e intuitivo

## Possibili estensioni

1. Aggiungere un campo prezzo e filtro per intervallo di prezzo
2. Aggiungere immagini reali dei veicoli
3. Aggiungere dettagli aggiuntivi (anno, km, prezzo)
4. Implementare paginazione per i risultati
5. Aggiungere ordinamento per colonna
6. Memorizzare i risultati con localStorage
