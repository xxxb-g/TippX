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

<<<<<<< HEAD
`sudo ./TippX/Linux/Distributionsunabhängig/TippX_0.1.0-1_all/Installer.sh`

#### Für alle anderen Linux-Distributionen mit make (Unterstützt auch lokale Installation ohne Root-Rechte)
`git clone https://github.com/xxxb-g/TippX.git`

`cd TippX`

`sudo make` oder wenn es nur für den lokalen Nutzer installiert werden soll und dementsprechend keine Root-Rechte benötigt: `make install_noroot` 
=======
`cd TippX`

`cd Linux`

`cd Distributionsunabhängig`

`cd TippX_0.1.0-1_all`

`sudo ./Installer.sh`
>>>>>>> b1c6026 (README.md angepasst)

#### Für alle anderen Linux-Distributionen mit make
`git clone https://github.com/xxxb-g/TippX.git`

`cd TippX`

`sudo make`

### Für Windows

benötigt pyinstaller (installieren mit `pip install pyinstaller`)

`curl.exe --output TippX.py https://raw.githubusercontent.com/xxxb-g/TippX/refs/heads/main/main.py`

`curl.exe --output Logo https://raw.githubusercontent.com/xxxb-g/TippX/main/Logo.png`

<<<<<<< HEAD
<<<<<<< HEAD
`pyinstaller --onefile --hidden-import random --hidden-import time --hidden-import math --hidden-import os --hidden-import tkinter -i [Pfad]\Logo.ico TippX.py`
=======
`pyinstaller --onefile --hidden-import random --hidden-import time --hidden-import math --hidden-import os --hidden-import tkinter -i [Pfad]\Logo.png TippX.py`
>>>>>>> ef837d1 (Update README.md)
=======
`pyinstaller --onefile --hidden-import random --hidden-import time --hidden-import math --hidden-import os --hidden-import tkinter -i [Pfad]\Logo.ico TippX.py`
>>>>>>> 502dfbf (fixed)

`cd dist`

`TippX.exe`

## Von der vorbereiteten Installationsdatei
### Für Debian-basierte Linux-Distributionen
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> bff343a (README.md verbessert)

Dies in /etc/apt/sources.list einfügen: `deb [trusted=yes] https://apt.fury.io/xxxb/ /` (das fügt mein APT-Repo hinzu)

und dann `sudo apt update && sudo apt install tippx`

Oder die Installationsdatei direkt herunterladen (keine auto-Updates)

<<<<<<< HEAD
=======
>>>>>>> b1c6026 (README.md angepasst)
=======
>>>>>>> bff343a (README.md verbessert)
`wget https://github.com/xxxb-g/TippX/releases/download/v0.1.0/TippX_0.1.0-1_all.deb`

`sudo dpkg -i TippX_0.1.0-1_all.deb`

### Für Windows

`curl.exe --output TippX.exe https://github.com/xxxb-g/TippX/releases/download/v0.1.0/TippX_0.1.0-1_all.exe`

`TippX.exe`

### Für Menschen, die nicht das Terminal/cmd nutzen wollen:
Lade die gewünschte Version auf  der [Release-Seite](https://github.com/xxxb-g/TippX/releases/) herunter und öffne sie.

# Deinstallation
## Für Linux
### Für Debian-basierte Linux-Distributionen (oder allgemein mit dpkg kompatible Distros)
<<<<<<< HEAD

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
=======
`sudo dpkg --purge TippX`
### Für Linux allgemein
Lade den Uninstaller herunter:
`wget https://raw.githubusercontent.com/xxxb-g/TippX/refs/heads/Releases/Linux/Distributionsunabh%C3%A4ngig/TippX_0.1.0-1_all/Uninstaller.sh`

`chmod +x Uninstaller.sh`

`sudo ./Uninstaller.sh`

`rm Uninstaller.sh`
### Für Linux allgemein mit Make
Lade die Makefile herunter:
`wget https://raw.githubusercontent.com/xxxb-g/TippX/refs/heads/main/Makefile`

`sudo make uninstall`
## Für Windows
die heruntergeladene bzw. gebaute Datei löschen

<br>
<br>
>>>>>>> b1c6026 (README.md angepasst)

***

Wenn dir meine Arbeit gefällt, kannst du mich hier unterstützen:

<a href="https://coindrop.to/TippX" target="_blank"><img src="https://coindrop.to/embed-button.png" style="border-radius: 10px; height: 57px !important;width: 229px !important;" alt="Coindrop.to me"></img></a>
