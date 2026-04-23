# Server Python per servire i file HTML e salvare studenti.json
# Avvia con: python server_studenti.py
# Poi apri: http://localhost:8080/registrazione_studente.html

import os
import json
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORTA = 8080
CARTELLA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=CARTELLA, **kwargs)

    def do_POST(self):
        if self.path == "/salva_studenti":
            lunghezza = int(self.headers["Content-Length"])
            corpo = self.rfile.read(lunghezza)
            dati = json.loads(corpo)
            percorso = os.path.join(CARTELLA, "studenti.json")
            with open(percorso, "w", encoding="utf-8") as f:
                json.dump(dati, f, indent=2, ensure_ascii=False)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(b'{"ok": true}')
        else:
            self.send_error(404)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

print("Server avviato su http://localhost:" + str(PORTA))
print("Apri http://localhost:" + str(PORTA) + "/registrazione_studente.html")
HTTPServer(("", PORTA), Handler).serve_forever()
