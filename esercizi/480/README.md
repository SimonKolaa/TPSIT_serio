# Esercizio 480 - CountryInfo SOAP Client

Questa applicazione Flask consente di interrogare il servizio SOAP `CountryInfoService` per ottenere informazioni sulle nazioni.

Funzionalità implementate:
- lista codici ISO disponibili con `ListOfCountryNamesByCode`
- ricerca capitale con `CapitalCity`
- ricerca prefisso telefonico con `CountryIntPhoneCode`
- ricerca informazioni complete con `FullCountryInfo`

## Esecuzione

1. Apri un terminale nella cartella `esercizi\480`
2. Installa le dipendenze:
   ```
   python -m pip install -r requirements.txt
   ```
3. Avvia l'app:
   ```
   python app.py
   ```
4. Apri nel browser:
   `http://127.0.0.1:5000`
