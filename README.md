# TippX
Zehnfingerschreiben lernen
![Logo](https://github.com/xxxb-g/TippX/blob/main/Logo.png)

# Installation
## Vom Source-Code
### Für Debian-basierte Linux-Distributionen (oder allgemein mit dpkg kompatible Distros)
`git clone -b Releases https://github.com/xxxb-g/TippX.git`

`cd TippX`

`dpkg-deb --build [Ordnername]`

`sudo dpkg -i [Ordnername].deb`
### Für Windows

benötigt pyinstaller (installieren mit `pip install pyinstaller`)

`curl.exe --output TippX.py https://raw.githubusercontent.com/xxxb-g/TippX/refs/heads/main/main.py`

`curl.exe --output Logo https://raw.githubusercontent.com/xxxb-g/TippX/main/Logo.png`

`pyinstaller --onefile --hidden-import random --hidden-import time --hidden-import math --hidden-import os --hidden-import tkinter -i [Pfad]\Logo.ico TippX.py`

`cd dist`

`TippX.exe`

## Von der vorbereiteten Installationsdatei
### Für Linux
`wget https://github.com/xxxb-g/TippX/releases/download/v0.1.0/TippX_0.1.0-1_all.deb`
`sudo dpkg -i TippX_0.1.0-1_all.deb`

### Für Windows

`curl.exe --output TippX.exe https://github.com/xxxb-g/TippX/releases/download/v0.1.0/TippX_0.1.0-1_all.exe`

`TippX.exe`

### Für Menschen, die nicht das Terminal/cmd nutzen wollen:
Lade die gewünschte Version auf  der [Release-Seite](https://github.com/xxxb-g/TippX/releases/) herunter und öffne sie.



Wenn dir meine Arbeit gefällt, kannst du mich hier unterstützen:

<a href="https://coindrop.to/TippX" target="_blank"><img src="https://coindrop.to/embed-button.png" style="border-radius: 10px; height: 57px !important;width: 229px !important;" alt="Coindrop.to me"></img></a>
