"""Test automatico client-server"""
import socket
import threading
import time

def avvia_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('localhost', 6789))
    s.listen(1)
    print("[SERVER] In attesa...")
    c, _ = s.accept()
    print("[SERVER] Client connesso")
    dati = c.recv(1024).decode('utf-8').strip()
    print(f"[SERVER] Ricevuto: '{dati}'")
    c.sendall((dati.upper() + '\n').encode('utf-8'))
    print(f"[SERVER] Inviato: '{dati.upper()}'")
    c.close()
    s.close()

def avvia_client():
    time.sleep(0.5)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 6789))
    print("[CLIENT] Connesso")
    s.sendall(b'test\n')
    print("[CLIENT] Inviato: 'test'")
    risp = s.recv(1024).decode('utf-8').strip()
    print(f"[CLIENT] Ricevuto: '{risp}'")
    s.close()
    
    if risp == "TEST":
        print("\n✓ TEST SUPERATO!")
        return True
    else:
        print("\n✗ TEST FALLITO")
        return False

print("=== TEST AUTOMATICO CLIENT-SERVER ===\n")

t = threading.Thread(target=avvia_server, daemon=True)
t.start()
successo = avvia_client()
t.join()

print("\n" + "="*40)
if successo:
    print("RISULTATO: Tutto funziona correttamente!")
else:
    print("RISULTATO: C'è un problema")
print("="*40)