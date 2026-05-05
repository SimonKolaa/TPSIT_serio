#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__, template_folder='templates')

# Percorso del file JSON con le auto
AUTO_JSON_PATH = os.path.join(os.path.dirname(__file__), 'data', 'auto.json')

def carica_auto():
    """Carica il file JSON con le auto disponibili"""
    try:
        with open(AUTO_JSON_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Errore nel caricamento del file JSON: {e}")
        return []

def filtra_auto(auto_list, marca, modello, alimentazione, colore):
    """Filtra la lista di auto in base ai criteri ricevuti"""
    risultati = []
    
    for auto in auto_list:
        # Se il filtro è vuoto, considera come "qualsiasi"
        if marca and auto['marca'].lower() != marca.lower():
            continue
        if modello and auto['modello'].lower() != modello.lower():
            continue
        if alimentazione and auto['alimentazione'].lower() != alimentazione.lower():
            continue
        if colore and auto['colore'].lower() != colore.lower():
            continue
        
        risultati.append(auto)
    
    return risultati

@app.route('/')
def index():
    """Pagina principale con la form"""
    return render_template('index.html')

@app.route('/cerca_auto', methods=['POST'])
def cerca_auto():
    """Endpoint AJAX per la ricerca delle auto"""
    # Ottiene i dati dalla richiesta POST
    marca = request.form.get('marca', '').strip()
    modello = request.form.get('modello', '').strip()
    alimentazione = request.form.get('alimentazione', '').strip()
    colore = request.form.get('colore', '').strip()
    
    # Carica le auto dal JSON
    auto_list = carica_auto()
    
    # Filtra le auto in base ai criteri
    risultati = filtra_auto(auto_list, marca, modello, alimentazione, colore)
    
    # Restituisce il risultato in formato JSON
    return jsonify({'auto': risultati})

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
