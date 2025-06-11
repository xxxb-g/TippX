git clone https://github.com/xxxb-g/TippX.git ./tmp
cd ./tmp
cp main.py /usr/bin/TippX.py
cat > /usr/bin/TippX.sh << 'ENDE'
#!/bin/bash
python3 /usr/bin/TippX.py
ENDE
chmod +x /usr/bin/TippX.sh
ln -s /usr/bin/TippX.sh /usr/bin/TippX
cat > /usr/share/applications/TippX.desktop << 'ENDE'
[Desktop Entry]
Version=1.0
Type=Application
Name=TippX
Comment=Deutsches 10-Finger-Schreibsystem lernen
Exec=TippX
Icon=/usr/share/icons/TippX-Logo.png
Terminal=true
Categories=Utility;Application;
StartupNotify=true
ENDE
mkdir -p /usr/share/doc/TippX
cp ./LICENSE /usr/share/doc/TippX/LICENSE
cp ./README.md /usr/share/doc/TippX/README.md
cat > /usr/share/doc/TippX/Version << 'ENDE'
Du hast die Version 0.1.0 kostenlos installiert. Du kann mich auf https://coindrop.to/TippX unterstützen.
ENDE
cp Logo.png /usr/share/icons/TippX-Logo.png
cat > TippX.1 << 'ENDE'
(C) Copyright 2025 Benedikt Goldhahn <xxxbGamer@proton.me>
TippX ist ein Programm zum lernen des 10-Finger-Schreibsystems. Zum Starten musst du nur TippX in deinem Startmenu suchen und öffnen. Alternativ kanst du den Befehl "TippX" im Terminal ausführen.
Am Anfang wirst du gefragt, welches Level du trainieren willst. Gib die entsprechende Zahl (z.B. 1) ein. Danach wirst du gefragt, wie lange du trainieren willst. Gib auch hier eine Zahl ein. Nun beginnt das Training. Tippe den Satz, der auf dem Bildschirm angezeigt wird und bestätige mit der Enter-Taste. Nach Ablauf der Zeit wird dir eine Statistik angezeigt.
ENDE
gzip TippX.1
cp TippX.1.gz /usr/share/man/man1/TippX.1.gz
cd ..
rm -rf ./tmp
