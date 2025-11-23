# TippX
Zehnfingerschreiben lernen
![Logo](https://github.com/xxxb-g/TippX/blob/main/Logo.png)

# Installation
## Vom Source-Code
### Für Linux

#### Für Debian-basierte Linux-Distributionen (oder allgemein mit dpkg kompatible Distros)

`git clone -b Releases https://github.com/xxxb-g/TippX.git`

`cd TippX`

`cd Linux`

`cd Debian-basiert`

`dpkg-deb --build [Ordnername]`

`sudo dpkg -i [Ordnername].deb`

#### Für alle anderen Linux-Distributionen

`git clone -b Releases https://github.com/xxxb-g/TippX.git`

`sudo ./TippX/Linux/Distributionsunabhängig/TippX_0.1.0-1_all/Installer.sh`

#### Als AppImage

`git clone -b Releases https://github.com/xxxb-g/TippX.git`

`cd TippX`

`cd Linux`

`cd Distributionsunabhängig`

`cd AppImage`

`wget https://github.com/AppImage/appimagetool/releases/download/continuous/appimagetool-x86_64.AppImage`

`chmod +x appimagetool-x86_64.AppImage`

`ARCH=x86_64 ./appimagetool-x86_64.AppImage AppDir_python TippX.AppImage` 

`# Du kannst bei ARCH= deine eigene Architektur einsetzen, x86_64 ist für 64-Bit. Statt AppDir_python kannst du den gewünschten Ordnernamen einsetzen. Die Unterschiede sind, dass _python nur auf Systemen mit Python geht, _universal auf allen und die _small Variante für ein paar kilobyte weniger Dateigröße.`

Nun kannst du das AppImage mit `./TippX.AppImage` öffnen. Für eine bessere Integration in die Desktopumgebung kann ein Programm wie [GearLever](https://github.com/mijorus/gearlever) genutzt werden.

#### Für alle anderen Linux-Distributionen mit make (Unterstützt auch lokale Installation ohne Root-Rechte)
`git clone https://github.com/xxxb-g/TippX.git`

`cd TippX`

`sudo make` oder wenn es nur für den lokalen Nutzer installiert werden soll und dementsprechend keine Root-Rechte benötigt: `make install_noroot` 

### Für Windows

benötigt pyinstaller (installieren mit `pip install pyinstaller`)

`curl.exe --output TippX.py https://raw.githubusercontent.com/xxxb-g/TippX/refs/heads/main/main.py`

`curl.exe --output Logo https://raw.githubusercontent.com/xxxb-g/TippX/main/Logo.png`

`pyinstaller --onefile --hidden-import random --hidden-import time --hidden-import math --hidden-import os --hidden-import tkinter -i [Pfad]\Logo.ico TippX.py`

`cd dist`

`TippX.exe`

## Von der vorbereiteten Installationsdatei
### Für Debian-basierte Linux-Distributionen

Dies in /etc/apt/sources.list einfügen: `deb [trusted=yes] https://apt.fury.io/xxxb/ /` (das fügt mein APT-Repo hinzu)

und dann `sudo apt update && sudo apt install tippx`

Oder die Installationsdatei direkt herunterladen (keine auto-Updates)

`wget https://github.com/xxxb-g/TippX/releases/download/v0.1.0/TippX_0.1.0-1_all.deb`

`sudo dpkg -i TippX_0.1.0-1_all.deb`

### Für andere Linux-Distros

[Hier wird eine Anleitung eingefügt, sobald der Release fertig ist.]

### Für Windows

`curl.exe --output TippX.exe https://github.com/xxxb-g/TippX/releases/download/v0.1.0/TippX_0.1.0-1_all.exe`

`TippX.exe`

### Für Menschen, die nicht das Terminal/cmd nutzen wollen:
Lade die gewünschte Version auf  der [Release-Seite](https://github.com/xxxb-g/TippX/releases/) herunter und öffne sie.

# Deinstallation
## Für Linux
### Für Debian-basierte Linux-Distributionen (oder allgemein mit dpkg kompatible Distros)

`sudo dpkg --purge TippX`

### Für Linux allgemein
Lade den Uninstaller herunter:
`wget https://raw.githubusercontent.com/xxxb-g/TippX/refs/heads/Releases/Linux/Distributionsunabh%C3%A4ngig/TippX_0.1.0-1_all/Uninstaller.sh`

`chmod +x Uninstaller.sh`

`sudo ./Uninstaller.sh`

`rm Uninstaller.sh`

ACHTUNG: Wenn es nur für den aktuellen Benutzer installiert wurde, wird ein anderer Uninstaller benötigt:

`wget https://raw.githubusercontent.com/xxxb-g/TippX/refs/heads/Releases/Linux/Distributionsunabh%C3%A4ngig/TippX_0.1.0-1_all/Uninstaller_Noroot.sh`

`chmod +x Uninstaller_Noroot.sh`

`rm Uninstaller_Noroot.sh`

### Für Linux allgemein mit Make
Lade die Makefile herunter:
`wget https://raw.githubusercontent.com/xxxb-g/TippX/refs/heads/main/Makefile`

`sudo make uninstall`  ACHTUNG: Wenn es nur für den aktuellen Benutzer installiert wurde, wird ein anderer Befehl benötigt:  `make uninstall_noroot`


## Für Windows
die heruntergeladene bzw. gebaute Datei löschen

<br>
<br>

***

Wenn dir meine Arbeit gefällt, kannst du mich hier unterstützen:

<a href="https://coindrop.to/TippX" target="_blank"><img src="https://coindrop.to/embed-button.png" style="border-radius: 10px; height: 57px !important;width: 229px !important;" alt="Coindrop.to me"></img></a>
