# Bug Report – Beispiel

## 1. Bug-ID
BUG-012

## 2. Titel
Forecast5 liefert nur 20 statt 40 Einträge

## 3. Umgebung
- API-Version: 2.5
- Tool: Insomnia 13.0.1

## 4. Schritte zur Reproduktion
1. GET /forecast?q=Berlin&appid=VALID_KEY
2. Response prüfen

## 5. Erwartetes Ergebnis
- `list[]` enthält 40 Einträge (5 Tage × 8 Intervalle)

## 6. Tatsächliches Ergebnis
- `list[]` enthält nur 20 Einträge

## 7. Statuscode
200 OK

## 8. Severity
High

## 9. Priority
Medium

## 10. Anhänge
- Screenshot
- JSON‑Response

## 11. Notizen
- Fehler tritt nur bei Städten mit hoher Datenlast auf


## **Severity and Priority Levels**


| **Severity** | Bedeutung |
| --- | --- |
| **Critical** | Systemabsturz, API nicht nutzbar |
| **High** | Hauptfunktion defekt |
| **Medium** | Teilfunktion fehlerhaft |
| **Low** | Kosmetischer Fehler |


| **Priority** | Bedeutung |
| --- | --- |
| **High** | Sofort beheben |
| **Medium** | Bald beheben |
| **Low** | Kann warten |





# Bug Report – Beispiel


## 1. Bug-ID
BUG-012

## 2. Titel
Forecast5 liefert nur 20 statt 40 Einträge

## 3. Umgebung
- API-Version: 2.5
- Tool: Insomnia 13.0.1

## 4. Schritte zur Reproduktion
1. GET /forecast?q=Berlin&appid=VALID_KEY
2. Response prüfen

## 5. Erwartetes Ergebnis
- `list[]` enthält 40 Einträge (5 Tage × 8 Intervalle)

## 6. Tatsächliches Ergebnis
- `list[]` enthält nur 20 Einträge

## 7. Statuscode
200 OK

## 8. Severity
High

## 9. Priority
Medium

## 10. Anhänge
- Screenshot
- JSON‑Response

## 11. Notizen
- Fehler tritt nur bei Städten mit hoher Datenlast auf
