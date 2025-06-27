.PHONY: all install uninstall clean install_noroot uninstall_noroot

all: install

clean: uninstall

install:
	cp main.py /usr/bin/TippX.py
	echo '#!/bin/bash\npython3 /usr/bin/TippX.py' > /usr/bin/TippX.sh
	chmod +x /usr/bin/TippX.sh
	ln -f -s /usr/bin/TippX.sh /usr/bin/TippX
	echo '[Desktop Entry]\nVersion=1.0\nType=Application\nName=TippX\nComment=Deutsches 10-Finger-Schreibsystem lernen\nExec=TippX\nIcon=/usr/share/icons/TippX-Logo.png\nTerminal=true\nCategories=Utility;Application;\nStartupNotify=true' > /usr/share/applications/TippX.desktop
	mkdir -p /usr/share/doc/TippX
	cp ./LICENSE /usr/share/doc/TippX/LICENSE
	cp ./README.md /usr/share/doc/TippX/README.md
	echo 'Du hast die Version 0.1.0 kostenlos installiert. Du kann mich auf https://coindrop.to/TippX unterstützen.' > /usr/share/doc/TippX/Version
	cp Logo.png /usr/share/icons/TippX-Logo.png
	echo -e "(C) Copyright 2025 Benedikt Goldhahn <xxxbGamer@proton.me>\nTippX ist ein Programm zum lernen des 10-Finger-Schreibsystems. Zum Starten musst du nur TippX in deinem Startmenu suchen und öffnen. Alternativ kanst du den Befehl "TippX" im Terminal ausführen.\nAm Anfang wirst du gefragt, welches Level du trainieren willst. Gib die entsprechende Zahl (z.B. 1) ein. Danach wirst du gefragt, wie lange du trainieren willst. Gib auch hier eine Zahl ein. Nun beginnt das Training. Tippe den Satz, der auf dem Bildschirm angezeigt wird und bestätige mit der Enter-Taste. Nach Ablauf der Zeit wird dir eine Statistik angezeigt." > TippX.1
	gzip -f TippX.1
	cp TippX.1.gz /usr/share/man/man1/TippX.1.gz
	rm -f TippX.1
	rm -f TippX.1.gz
uninstall:
	rm -f /usr/bin/TippX.py /usr/bin/TippX.sh /usr/bin/TippX /usr/share/applications/TippX.desktop
	rm -rf /usr/share/doc/TippX
	rm -f /usr/share/icons/TippX-Logo.png /usr/share/man/man1/TippX.1.gz
install_noroot:
	cp main.py $(HOME)/bin/TippX.py
	echo '#!/bin/bash\npython3 $(HOME)/bin/TippX.py' > $(HOME)/bin/TippX.sh
	chmod +x $(HOME)/bin/TippX.sh
	ln -f -s $(HOME)/bin/TippX.sh $(HOME)/bin/TippX
	echo '[Desktop Entry]\nVersion=1.0\nType=Application\nName=TippX\nComment=Deutsches 10-Finger-Schreibsystem lernen\nExec=TippX\nIcon=$(HOME)/.local/share/icons/TippX-Logo.png\nTerminal=true\nCategories=Utility;Application;\nStartupNotify=true' > $(HOME)/.local/share/applications/TippX.desktop
	mkdir -p $(HOME)/.local/share/doc/TippX
	cp ./LICENSE $(HOME)/.local/share/doc/TippX
	cp ./README.md $(HOME)/.local/share/doc/TippX
	echo 'Du hast die Version 0.1.0 kostenlos installiert. Du kann mich auf https://coindrop.to/TippX unterstützen.' > $(HOME)/.local/share/doc/TippX/Version
	cp ./Logo.png $(HOME)/.local/share/icons/TippX-Logo.png
	mkdir -p $(HOME)/.local/share/man/man1/
	echo -e "(C) Copyright 2025 Benedikt Goldhahn <xxxbGamer@proton.me>\nTippX ist ein Programm zum lernen des 10-Finger-Schreibsystems. Zum Starten musst du nur TippX in deinem Startmenu suchen und öffnen. Alternativ kanst du den Befehl "TippX" im Terminal ausführen.\nAm Anfang wirst du gefragt, welches Level du trainieren willst. Gib die entsprechende Zahl (z.B. 1) ein. Danach wirst du gefragt, wie lange du trainieren willst. Gib auch hier eine Zahl ein. Nun beginnt das Training. Tippe den Satz, der auf dem Bildschirm angezeigt wird und bestätige mit der Enter-Taste. Nach Ablauf der Zeit wird dir eine Statistik angezeigt." > TippX.1
	gzip -f TippX.1
	cp TippX.1.gz $(HOME)/.local/share/man/man1/TippX.1.gz
	rm -f TippX.1
	rm -f TippX.1.gz
uninstall_noroot:
	rm -f $(HOME)/bin/TippX.py $(HOME)/bin/TippX.sh $(HOME)/bin/TippX $(HOME)/.local/share/applications/TippX.desktop
	rm -rf $(HOME)/.local/share/doc/TippX
	rm -f $(HOME)/.local/share/icons/TippX-Logo.png $(HOME)/.local/share/man/man1/TippX.1.gz