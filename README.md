Speedtest Service – Clean Architecture Learning Project

Dieses Projekt ist ein Lernprojekt, das ich erstellt habe, um die Prinzipien von
Enterprise Software Design, Clean Architecture, Domain-Driven Development
und automatisiertem Testen zu verstehen und praktisch anzuwenden.

Ich bin aktuell dabei, professionelle Softwareentwicklung zu lernen
und dieses Projekt ist ein wichtiger Schritt auf dem Weg zum
Automation Engineer / Enterprise-Level Developer.

Ziele des Projekts

Der Zweck des Projekts ist:

• eine Internet-Speedmessung durchzuführen
• die Ergebnisse in einer sauberen Domain-Struktur abzubilden
• das Ergebnis in einer CSV-Datei zu speichern
• optional eine Benachrichtigung zu versenden
• ALLE Schichten nach Enterprise-Standards zu trennen

Was ich hier geübt habe

Dieses Projekt wurde bewusst so umgesetzt, dass es nicht einfach funktioniert,
sondern, dass ich professionelle Softwarearchitektur übe – dazu gehören:

✔ Domain-Driven Design

• Value Objects
• Domain Entities
• Validierungen mit __post_init__
• Fachlogik in der Domain statt im Service

✔ Clean Architecture

• Trennung in Domain / Protocols / Services / Infrastructure
• Ports & Adapters Prinzip umgesetzt
• Keine direkte Kopplung zwischen Schichten

✔ Enterprise-Level Code

• Lesbare, wartbare Klassen
• Keine unkontrollierten Abhängigkeiten
• Reiner Service Layer ohne externen Code
• Domain enthält die Wahrheit, nicht Formatter

✔ Testabdeckung

Ich habe gelernt, wie man:

• Domain testet
• Fehlerfälle testet
• Parser testet
• Infrastructure testet (CSV-Logger mit tmp_path)
• Mocking & Isolation richtig einsetzt (nächster Schritt)

Alle wichtigen Teile des Systems sind durch Unit Tests abgedeckt.

Projektstruktur
core/
    domain/
        server_location.py
        speedtest_result.py
    protocols/
        runner_protocol.py
        logger_protocol.py
        messenger_protocol.py
    services/
        speedtest_service.py

infrastructure/
    speedtest_runner.py
    csv_logger.py
    telegram_messenger.py (optional)

tests/
    domain/
    infrastructure/
    services/ (geplant)

Was dieses Projekt NICHT ist

✓ kein fertiges Produkt
✓ kein perfekter Code
✓ keine Produktionssoftware

Es ist ein Lernprojekt, und genau so soll es sein.

Was als nächstes kommt

• Tests für den Service (Mocking)
• Dokumentation der Architektur
• Eventuell Docker-Umgebung
• Mein nächstes Projekt: Weather Monitor Service – von Anfang an Enterprise-ready

Warum dieses Projekt wichtig für meinen Lernweg ist

Ich möchte langfristig auf Senior-Level entwickeln können.
Dafür reicht „Code, der funktioniert“ nicht.

Ich übe hier:

• Architektur
• Entkopplung
• Domain-Wissen
• Testbarkeit
• Clean Code
• Verantwortung für Softwarequalität

Dieses Projekt zeigt meinen Lernfortschritt
und ist eines der ersten Projekte, bei dem ich wirklich nach Enterprise-Prinzipien arbeite.
