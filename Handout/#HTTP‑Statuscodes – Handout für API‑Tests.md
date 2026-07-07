# HTTP‑Statuscodes – Handout für API‑Tester  
## Grundlagen für API‑Tests (ISTQB‑konform)

---

## 1. Was sind HTTP‑Statuscodes?
HTTP‑Statuscodes sind **standardisierte Antworten** eines Servers auf eine Anfrage (Request).  
Sie zeigen an, **ob die Anfrage erfolgreich war**, **Fehler aufgetreten sind** oder **weitere Schritte nötig** sind.

Jeder Statuscode besteht aus **3 Ziffern** und gehört zu einer **von fünf Klassen**.

---

## 2. Die fünf Klassen von Statuscodes

### **1xx – Information**
Der Server hat die Anfrage erhalten und verarbeitet sie weiter.  
Wird selten in API‑Tests genutzt.

Beispiele:
- **100 Continue**
- **101 Switching Protocols**

---

### **2xx – Erfolg**
Die Anfrage wurde **korrekt verarbeitet**.

| Code | Bedeutung | Beispiel |
|------|-----------|----------|
| **200 OK** | Erfolgreiche Anfrage | GET /weather |
| **201 Created** | Ressource wurde erstellt | POST /user |
| **204 No Content** | Erfolgreich, aber ohne Body | DELETE /item |

---

### **3xx – Weiterleitung**
Der Client muss **einen weiteren Schritt** ausführen (z. B. neue URL).

| Code | Bedeutung |
|------|-----------|
| **301 Moved Permanently** | Ressource dauerhaft verschoben |
| **302 Found** | Temporäre Weiterleitung |
| **304 Not Modified** | Cache‑Antwort |

---

### **4xx – Clientfehler**
Die Anfrage ist **fehlerhaft** oder **unvollständig**.

| Code | Bedeutung | Typische Ursache |
|------|-----------|------------------|
| **400 Bad Request** | Ungültige Anfrage | Parameter fehlen |
| **401 Unauthorized** | Kein/ungültiger API‑Key | appid falsch |
| **403 Forbidden** | Zugriff verboten | Rechte fehlen |
| **404 Not Found** | Ressource nicht gefunden | Stadtname falsch |
| **429 Too Many Requests** | Rate‑Limit erreicht | Zu viele Requests |

---

### **5xx – Serverfehler**
Der Fehler liegt **auf Serverseite**.

| Code | Bedeutung |
|------|-----------|
| **500 Internal Server Error** | Allgemeiner Serverfehler |
| **502 Bad Gateway** | Fehler zwischen Servern |
| **503 Service Unavailable** | Server überlastet / Wartung |
| **504 Gateway Timeout** | Server antwortet zu langsam |

---

## 3. Warum sind Statuscodes wichtig für API‑Tests?
Statuscodes helfen dir zu prüfen:

- Ob die API korrekt funktioniert  
- Ob Fehler richtig behandelt werden  
- Ob Eingaben valide sind  
- Ob Sicherheitsmechanismen greifen  
- Ob Rate‑Limits korrekt ausgelöst werden  

Sie sind ein **zentrales Element** in jedem Testfall.

---

## 4. Beispiele aus OpenWeatherMap (OWM)

### **200 OK**
Gültige Anfrage:

- /weather?q=Berlin&appid=KEY
  

### **401 Unauthorized**
Ungültiger API‑Key:

- /weather?q=Berlin&appid=FALSCHER_KEY


### **429 Too Many Requests**
Zu viele Requests in kurzer Zeit:
- Besonders relevant bei Free Tier  
- Wird durch schnelle Wiederholungen ausgelöst  

---

## 5. Testideen für Statuscodes (ISTQB‑konform)

### **Positivtests**
- Gültige Anfrage → **200 OK**
- Ressource erstellt → **201 Created**

### **Negativtests**
- Fehlender Parameter → **400**
- Ungültiger API‑Key → **401**
- Ungültige Ressource → **404**
- Rate‑Limit überschritten → **429**

### **Grenzwerttests**
- Minimale/Maximale Parameter  
- Leere Strings  
- Ungültige Datentypen  

---

## 6. Mini‑Referenz (Kurzfassung)

| Klasse | Bedeutung |
|--------|-----------|
| **1xx** | Information |
| **2xx** | Erfolg |
| **3xx** | Weiterleitung |
| **4xx** | Clientfehler |
| **5xx** | Serverfehler |

---

## 7. Zusammenfassung
HTTP‑Statuscodes sind ein **zentrales Werkzeug** für API‑Tester.  
Sie zeigen klar an, ob eine Anfrage erfolgreich war oder Fehler korrekt behandelt wurden.  
Für ISTQB‑konforme Testfälle sind sie unverzichtbar.

