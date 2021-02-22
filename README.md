# Dokumentation

Wir haben **app-skeleton** entwickelt um uns die Arbeit an unterschiedlichen Projekten zu erleichtern. 
Es stellt eine einfache Webbasierte Benutzeroberfläche mit API-Schnittstelle, PDF Erstellung und einer Datenbank bereit.  

![overview](/docs/overview.png "Erster Start")

An eine Veröffentlichung haben wir erst gedacht, als uns immer mehr Nachfragen aus anderen Kliniken erreichten. 
Dementsprechend befinden sich viele Module und Funktionen noch im Stadium "learning by doing" und die Dokumentation 
ist ein halbvollständiger Deutsch-Englisch-Mix.

Noch keine Erfahrung mit Python?

Die Seite https://www.python-kurs.eu/index.php gibt einen guten Einstieg in die Programmierung mit Python.

## Haftungsausschluss:
Die Verwendung von **app-skeleton** liegt im Ermessen des Anwenders und wir übernehmen keinerlei Verantwortung 
für die Korrektheit der Ergebnisse. Die Verwendung ist nur für Forschungszwecke bestimmt. 

When using **app-skeleton** we assume no responsibility for the correctness of the results. 
Using is for research use only.

## Installation und Konfiguration

* [Installation (en)](docs/en/installation.md)

Die Datei `./config/config.json` bearbeiten und die Konfiguration anpassen. 
Siehe [Konfiguration (de)](docs/de/Konfiguration.md)

## Erster Start

1. Auf der Konsole in das repository Verzeichnis mit `cd` wechseln.
2. Starten mit: `<your miniconda binpath>/python ./skeleton.py` 

Der Oberfläche von **app-skeleton** ist jetzt über die URL: **127.0.0.1:5000** oder die in der `config` angegebenen Parameter erreichbar.

## Zugriff

    /                   - Interface with documentation / Oberfläche mit Dokumentation
    /api                - Documentation of the API interface / Dokumentation der Api Schnittstelle 
    /api/{class}/{id}   - Access to the API interface / Zugriff auf die Api Schnitstelle
    /docs               - Documentation of the program / Dokumentation des Programms

## Wichtige Komponenten
* [flask](https://de.wikipedia.org/wiki/Flask) und [safrs](https://github.com/thomaxxl/safrs/) für die Weboberfläche und API-Schnittstelle 
* [weasyprint](https://weasyprint.readthedocs.io/en/stable/tutorial.html) für die Erstellung der PDF Ausgaben
* [Pandas](https://de.wikipedia.org/wiki/Pandas_(Software)) für die Gruppierung der Testdaten und Erstellung von Tabellen für die Ausgabe
* [unittest](https://docs.python.org/3/library/unittest.html) für die Prüfung der internen Abläufe besonders nach Programmänderugen
* Das [MQTT-Protokoll](https://de.wikipedia.org/wiki/MQTT) wird verwendet um Informationen zwischen verschiedenen Anwendungen zu übertragen
* [node-red](https://nodered.org/) wird verwendet um MQTT Meldungen zu prüfen, zu verarbeiten und weiterzuleiten

## Zukunft

* [ ] Dokumentation in Englisch und/oder Deutsch

## Fehler und Anmerkungen

Der beste Weg, uns zu erreichen, besteht darin, auf Github ein Issue zu erstellen.