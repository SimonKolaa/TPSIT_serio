// ============================================
// EFFETTI DINAMICI MOTION-DRIVEN (AWWWARDS STYLE)
// ============================================

var mouseX = 0;
var mouseY = 0;
var scrollProgress = 0;

// Crea particelle
function creaParticelle(x, y) {
    "use strict";
    var particella = document.createElement('div');
    particella.style.position = 'fixed';
    particella.style.left = x + 'px';
    particella.style.top = y + 'px';
    particella.style.width = '10px';
    particella.style.height = '10px';
    particella.style.background = 'radial-gradient(circle, #667eea, #764ba2)';
    particella.style.borderRadius = '50%';
    particella.style.pointerEvents = 'none';
    particella.style.zIndex = '5';
    
    var colors = ['#667eea', '#764ba2', '#f093fb', '#4facfe', '#00f2fe'];
    particella.style.background = colors[Math.floor(Math.random() * colors.length)];
    
    particella.style.animation = 'particle-float ' + (1 + Math.random() * 2) + 's ease-out forwards';
    
    document.body.appendChild(particella);
    
    setTimeout(function() {
        particella.remove();
    }, 3000);
}

// Event listener per click - crea particelle
document.addEventListener('click', function(e) {
    "use strict";
    for (var i = 0; i < 5; i++) {
        setTimeout(function() {
            creaParticelle(e.clientX, e.clientY);
        }, i * 50);
    }
});

document.addEventListener('DOMContentLoaded', function() {
    "use strict";
    
    // Mouse Tracking per Parallax
    document.addEventListener('mousemove', function(e) {
        mouseX = e.clientX / window.innerWidth;
        mouseY = e.clientY / window.innerHeight;
        
        // Applica effetto di parallax ai blob
        var blobs = document.querySelectorAll('.blob-1, .blob-2, .blob-3');
        for (var i = 0; i < blobs.length; i++) {
            var blob = blobs[i];
            blob.style.transform = 'translate(' + (mouseX * 50) + 'px, ' + (mouseY * 50) + 'px)';
        }
    });
    
    // Scroll Animations - Effetto parallax su scroll
    window.addEventListener('scroll', function() {
        var scrollTop = window.pageYOffset;
        scrollProgress = scrollTop / (document.documentElement.scrollHeight - window.innerHeight);
        
        // Parallax su hero section
        var hero = document.querySelector('.hero-section');
        if (hero) {
            hero.style.transform = 'translateY(' + (scrollTop * 0.5) + 'px)';
            hero.style.opacity = Math.max(0, 1 - (scrollTop / 500));
        }
        
        // Scroll Fade per elementi
        osservaElementi();
        
        // Aggiorna scroll indicator
        var indicator = document.querySelector('.scroll-indicator');
        if (indicator) {
            indicator.style.bottom = (150 + (scrollProgress * 200)) + 'px';
        }
    });
    
    // Osserva gli elementi per animarli al scroll
    osservaElementi();
    
    // Form inserimento
    var formInserisci = document.getElementById('formInserisci');
    if (formInserisci) {
        formInserisci.addEventListener('submit', inserisciUtente);
    }
    
    // Form modifica
    var formModifica = document.getElementById('formModifica');
    if (formModifica) {
        formModifica.addEventListener('submit', salvaModifica);
    }
    
    // Carica utenti al caricamento della pagina
    caricaUtenti();
    
    // Button Effects
    aggiungiEffettiButton();
    
    // Aggiungi staggered animation agli input
    var inputs = document.querySelectorAll('input, textarea');
    for (var j = 0; j < inputs.length; j++) {
        inputs[j].style.animation = 'slideInRight 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94) ' + (j * 0.1) + 's both';
    }
});

function osservaElementi() {
    "use strict";
    var elementi = document.querySelectorAll('.form-section, table, h2, .scroll-fade');
    
    for (var i = 0; i < elementi.length; i++) {
        var element = elementi[i];
        var posizione = element.getBoundingClientRect();
        var window_height = window.innerHeight;
        
        if (posizione.top < window_height * 0.75 && posizione.bottom > 0) {
            element.classList.add('visible');
        }
    }
}

// ============================================
// UTILITY - Gestione AJAX (ES5)
// ============================================

function eseguiRichiesta(metodo, url, dati, callback) {
    "use strict";
    var xhr = new XMLHttpRequest();
    
    xhr.open(metodo, url, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            var response = null;
            var statusCode = xhr.status;
            
            try {
                response = xhr.responseText ? JSON.parse(xhr.responseText) : null;
            } catch (e) {
                response = null;
            }
            
            callback(statusCode, response);
        }
    };
    
    xhr.onerror = function() {
        mostraErrore('Errore di connessione al server');
    };
    
    if (dati) {
        xhr.send(JSON.stringify(dati));
    } else {
        xhr.send();
    }
}

// ============================================
// UTILITY - Alert
// ============================================

function mostraSuccesso(messaggio) {
    "use strict";
    mostraAlert(messaggio, 'success');
}

function mostraErrore(messaggio) {
    "use strict";
    mostraAlert(messaggio, 'error');
}

function mostraInfo(messaggio) {
    "use strict";
    mostraAlert(messaggio, 'info');
}

function mostraAlert(messaggio, tipo) {
    "use strict";
    var container = document.getElementById('alertContainer');
    var alertDiv = document.createElement('div');
    
    alertDiv.className = 'alert alert-' + tipo;
    alertDiv.textContent = messaggio;
    alertDiv.style.animation = 'slideInDown 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94), flicker 2s ease-in-out 0.5s infinite';
    
    container.innerHTML = '';
    container.appendChild(alertDiv);
    
    // Crea particelle intorno all'alert
    setTimeout(function() {
        for (var i = 0; i < 8; i++) {
            var angle = (i / 8) * Math.PI * 2;
            var x = container.offsetLeft + container.offsetWidth / 2 + Math.cos(angle) * 50;
            var y = container.offsetTop + container.offsetHeight / 2 + Math.sin(angle) * 50;
            creaParticelle(x, y);
        }
    }, 100);
    
    // Nascondi dopo 5 secondi
    setTimeout(function() {
        alertDiv.style.animation = 'slideInUp 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94) reverse';
        setTimeout(function() {
            alertDiv.style.display = 'none';
        }, 400);
    }, 5000);
}

// ============================================
// UTILITY - Modal
// ============================================

function apriModalDettaglio() {
    "use strict";
    document.getElementById('modalDettaglio').style.display = 'block';
}

function chiudiModalDettaglio() {
    "use strict";
    document.getElementById('modalDettaglio').style.display = 'none';
}

function apriModalModifica() {
    "use strict";
    document.getElementById('modalModifica').style.display = 'block';
}

function chiudiModalModifica() {
    "use strict";
    document.getElementById('modalModifica').style.display = 'none';
}

// Chiudi modal cliccando fuori
window.onclick = function(event) {
    "use strict";
    var modalDettaglio = document.getElementById('modalDettaglio');
    var modalModifica = document.getElementById('modalModifica');
    
    if (event.target === modalDettaglio) {
        modalDettaglio.style.display = 'none';
    }
    if (event.target === modalModifica) {
        modalModifica.style.display = 'none';
    }
};

// ============================================
// UTILITY - Loading
// ============================================

function mostraLoading() {
    "use strict";
    document.getElementById('loading').style.display = 'block';
}

function nascondiLoading() {
    "use strict";
    document.getElementById('loading').style.display = 'none';
}

// ============================================
// VALIDAZIONE DATI
// ============================================

function validaDati(nome, cognome, dataNascita, mansione) {
    "use strict";
    var errori = [];
    var nomeRegex = /^[a-zA-Z\s]{2,50}$/;
    var dataRegex = /^\d{4}-\d{2}-\d{2}$/;
    
    if (!nomeRegex.test(nome.trim())) {
        errori.push('Nome non valido (2-50 caratteri, solo lettere e spazi)');
    }
    
    if (!nomeRegex.test(cognome.trim())) {
        errori.push('Cognome non valido (2-50 caratteri, solo lettere e spazi)');
    }
    
    if (!dataRegex.test(dataNascita)) {
        errori.push('Data di nascita non valida (formato: YYYY-MM-DD)');
    }
    
    if (mansione.trim().length < 2) {
        errori.push('Mansione non valida (minimo 2 caratteri)');
    }
    
    return errori;
}

// ============================================
// OPERAZIONI CRUD - GET
// ============================================

function caricaUtenti() {
    "use strict";
    mostraLoading();
    
    eseguiRichiesta('GET', '/users/', null, function(status, response) {
        nascondiLoading();
        
        if (status === 200) {
            visualizzaUtenti(response);
            
            // Crea effetto confetti
            for (var k = 0; k < 20; k++) {
                setTimeout(function() {
                    creaParticelle(
                        Math.random() * window.innerWidth,
                        Math.random() * 200
                    );
                }, k * 30);
            }
        } else {
            mostraErrore('Errore nel caricamento degli utenti');
            document.getElementById('listaUtenti').innerHTML = '<div class="empty-state"><p>Impossibile caricare gli utenti</p></div>';
        }
    });
}

function visualizzaDettaglio(id) {
    "use strict";
    eseguiRichiesta('GET', '/users/' + id, null, function(status, response) {
        if (status === 200) {
            var html = '<div>';
            html += '<p><strong>ID:</strong> ' + response.id + '</p>';
            html += '<p><strong>Nome:</strong> ' + response.nome + '</p>';
            html += '<p><strong>Cognome:</strong> ' + response.cognome + '</p>';
            html += '<p><strong>Data di Nascita:</strong> ' + response.data_nascita + '</p>';
            html += '<p><strong>Mansione:</strong> ' + response.mansione + '</p>';
            html += '</div>';
            
            document.getElementById('contenutoDettaglio').innerHTML = html;
            apriModalDettaglio();
        } else if (status === 404) {
            mostraErrore('Utente non trovato');
        } else {
            mostraErrore('Errore nel caricamento del dettaglio');
        }
    });
}

// ============================================
// OPERAZIONI CRUD - POST
// ============================================

function inserisciUtente(event) {
    "use strict";
    event.preventDefault();
    
    var nome = document.getElementById('nome').value;
    var cognome = document.getElementById('cognome').value;
    var dataNascita = document.getElementById('dataNascita').value;
    var mansione = document.getElementById('mansione').value;
    
    // Valida
    var errori = validaDati(nome, cognome, dataNascita, mansione);
    if (errori.length > 0) {
        mostraErrore(errori.join('\n'));
        return;
    }
    
    var dati = {
        nome: nome,
        cognome: cognome,
        data_nascita: dataNascita,
        mansione: mansione
    };
    
    eseguiRichiesta('POST', '/users/', dati, function(status, response) {
        if (status === 201) {
            mostraSuccesso('Utente inserito con successo!');
            document.getElementById('formInserisci').reset();
            caricaUtenti();
        } else if (status === 400) {
            if (response.errori) {
                mostraErrore(response.errori.join('\n'));
            } else {
                mostraErrore(response.errore || 'Dati non validi');
            }
        } else {
            mostraErrore('Errore nell\'inserimento dell\'utente');
        }
    });
}

// ============================================
// OPERAZIONI CRUD - PUT
// ============================================

function caricaModifica(id) {
    "use strict";
    eseguiRichiesta('GET', '/users/' + id, null, function(status, response) {
        if (status === 200) {
            document.getElementById('idModifica').value = response.id;
            document.getElementById('nomeModifica').value = response.nome;
            document.getElementById('cognomeModifica').value = response.cognome;
            document.getElementById('dataNascitaModifica').value = response.data_nascita;
            document.getElementById('mansioneModifica').value = response.mansione;
            apriModalModifica();
        } else {
            mostraErrore('Errore nel caricamento dei dati per la modifica');
        }
    });
}

function salvaModifica(event) {
    "use strict";
    event.preventDefault();
    
    var id = parseInt(document.getElementById('idModifica').value);
    var nome = document.getElementById('nomeModifica').value;
    var cognome = document.getElementById('cognomeModifica').value;
    var dataNascita = document.getElementById('dataNascitaModifica').value;
    var mansione = document.getElementById('mansioneModifica').value;
    
    // Valida
    var errori = validaDati(nome, cognome, dataNascita, mansione);
    if (errori.length > 0) {
        mostraErrore(errori.join('\n'));
        return;
    }
    
    var dati = {
        nome: nome,
        cognome: cognome,
        data_nascita: dataNascita,
        mansione: mansione
    };
    
    eseguiRichiesta('PUT', '/users/' + id, dati, function(status, response) {
        if (status === 200) {
            mostraSuccesso('Utente modificato con successo!');
            chiudiModalModifica();
            caricaUtenti();
        } else if (status === 400) {
            if (response.errori) {
                mostraErrore(response.errori.join('\n'));
            } else {
                mostraErrore(response.errore || 'Dati non validi');
            }
        } else if (status === 404) {
            mostraErrore('Utente non trovato');
        } else {
            mostraErrore('Errore nella modifica dell\'utente');
        }
    });
}

// ============================================
// OPERAZIONI CRUD - DELETE
// ============================================

function eliminaUtente(id) {
    "use strict";
    if (confirm('Sei sicuro di voler eliminare questo utente?')) {
        eseguiRichiesta('DELETE', '/users/' + id, null, function(status, response) {
            if (status === 204) {
                mostraSuccesso('Utente eliminato con successo!');
                caricaUtenti();
            } else if (status === 404) {
                mostraErrore('Utente non trovato');
            } else {
                mostraErrore('Errore nell\'eliminazione dell\'utente');
            }
        });
    }
}

// ============================================
// VISUALIZZAZIONE LISTA
// ============================================

function visualizzaUtenti(utenti) {
    "use strict";
    var container = document.getElementById('listaUtenti');
    
    if (utenti.length === 0) {
        container.innerHTML = '<div class="empty-state"><p>Nessun utente presente. Inserisci il primo utente!</p></div>';
        return;
    }
    
    var html = '<table>';
    html += '<thead>';
    html += '<tr>';
    html += '<th>ID</th>';
    html += '<th>Nome</th>';
    html += '<th>Cognome</th>';
    html += '<th>Data di Nascita</th>';
    html += '<th>Mansione</th>';
    html += '<th>Azioni</th>';
    html += '</tr>';
    html += '</thead>';
    html += '<tbody>';
    
    for (var i = 0; i < utenti.length; i++) {
        var u = utenti[i];
        html += '<tr style="animation: fadeInScale 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94) ' + (i * 0.1) + 's both;">';
        html += '<td style="animation-delay: ' + (i * 0.1 + 0.1) + 's">🆔 ' + u.id + '</td>';
        html += '<td style="animation-delay: ' + (i * 0.1 + 0.15) + 's">👤 ' + u.nome + '</td>';
        html += '<td style="animation-delay: ' + (i * 0.1 + 0.2) + 's">' + u.cognome + '</td>';
        html += '<td style="animation-delay: ' + (i * 0.1 + 0.25) + 's">📅 ' + u.data_nascita + '</td>';
        html += '<td style="animation-delay: ' + (i * 0.1 + 0.3) + 's">💼 ' + u.mansione + '</td>';
        html += '<td style="animation-delay: ' + (i * 0.1 + 0.35) + 's">';
        html += '<div class="actions">';
        html += '<button class="btn-info" onclick="visualizzaDettaglio(' + u.id + ')">Dettaglio</button>';
        html += '<button class="btn-primary" onclick="caricaModifica(' + u.id + ')">Modifica</button>';
        html += '<button class="btn-danger" onclick="eliminaUtente(' + u.id + ')">Elimina</button>';
        html += '</div>';
        html += '</td>';
        html += '</tr>';
    }
    
    html += '</tbody>';
    html += '</table>';
    
    container.innerHTML = html;
    
    // Re-applica gli effetti ai nuovi button
    setTimeout(function() {
        aggiungiEffettiButton();
    }, 100);
}

// ============================================
// INIZIALIZZAZIONE
// ============================================

// Aggiungi questa riga prima del secondo DOMContentLoaded:
function aggiungiEffettiButton() {
    "use strict";
    var buttons = document.querySelectorAll('button');
    
    for (var i = 0; i < buttons.length; i++) {
        var button = buttons[i];
        button.style.animation = 'fadeInScale 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94) ' + (i * 0.05) + 's both';
        
        button.addEventListener('mousemove', function(e) {
            var rect = this.getBoundingClientRect();
            var x = e.clientX - rect.left;
            var y = e.clientY - rect.top;
            
            var ripple = document.createElement('span');
            ripple.style.position = 'absolute';
            ripple.style.left = x + 'px';
            ripple.style.top = y + 'px';
            ripple.style.width = '20px';
            ripple.style.height = '20px';
            ripple.style.background = 'rgba(255,255,255,0.5)';
            ripple.style.borderRadius = '50%';
            ripple.style.pointerEvents = 'none';
            ripple.style.transform = 'scale(0)';
            ripple.style.animation = 'ripple-effect 0.6s ease-out';
            
            this.appendChild(ripple);
            
            setTimeout(function() {
                ripple.remove();
            }, 600);
        });
        
        button.addEventListener('mouseenter', function() {
            // Crea explosione di particelle
            var rect = this.getBoundingClientRect();
            var centerX = rect.left + rect.width / 2;
            var centerY = rect.top + rect.height / 2;
            
            for (var k = 0; k < 3; k++) {
                setTimeout(function() {
                    creaParticelle(centerX, centerY);
                }, k * 30);
            }
            
            // Flash light effect
            var light = document.createElement('div');
            light.style.position = 'fixed';
            light.style.left = (centerX - 50) + 'px';
            light.style.top = (centerY - 50) + 'px';
            light.style.width = '100px';
            light.style.height = '100px';
            light.style.background = 'radial-gradient(circle, rgba(102, 126, 234, 0.5) 0%, transparent 70%)';
            light.style.borderRadius = '50%';
            light.style.pointerEvents = 'none';
            light.style.zIndex = '4';
            light.style.animation = 'pulse-glow 0.5s ease-out forwards';
            
            document.body.appendChild(light);
            
            setTimeout(function() {
                light.remove();
            }, 500);
        });
    }
}

document.addEventListener('DOMContentLoaded', function() {
    "use strict";
    
    // Form inserimento
    var formInserisci = document.getElementById('formInserisci');
    if (formInserisci) {
        formInserisci.addEventListener('submit', inserisciUtente);
    }
    
    // Form modifica
    var formModifica = document.getElementById('formModifica');
    if (formModifica) {
        formModifica.addEventListener('submit', salvaModifica);
    }
    
    // Carica utenti al caricamento della pagina
    caricaUtenti();
    
    // Button Effects
    aggiungiEffettiButton();
});
