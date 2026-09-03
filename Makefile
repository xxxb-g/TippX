.PHONY: linux windows release standalone
build: linux
standalone:
	CC=/usr/bin/gcc CXX=/usr/bin/g++ python3 -m nuitka --standalone --include-module="requests" --include-module="threading" --include-module="webbrowser" --include-module="random" --include-module="pygame" --product-name=TippX_by_xxxb --output-filename="TippX" --nofollow-import-to=unittest --nofollow-import-to=numpy --nofollow-import-to=pygame.surfarray --nofollow-import-to=pygame.sndarray --nofollow-import-to=pygame.image --nofollow-import-to=pygame.transform --nofollow-import-to=libssl --include-data-files=Ding.wav=. --include-data-files=Doeng.mp3=. --include-data-file=xxxb-Font.otf=. --include-data-file=LICENSE=. --no-deployment-flag=excluded-module-usage main.py
linux:
	CC=/usr/bin/gcc CXX=/usr/bin/g++ python3 -m nuitka --onefile --include-module="requests" --include-module="threading" --include-module="webbrowser" --include-module="random" --include-module="pygame" --product-name=TippX_by_xxxb --output-filename="TippX" --nofollow-import-to=unittest --nofollow-import-to=numpy --nofollow-import-to=pygame.surfarray --nofollow-import-to=pygame.sndarray --nofollow-import-to=pygame.image --nofollow-import-to=pygame.transform --nofollow-import-to=libssl --include-data-files=Ding.wav=. --include-data-files=Doeng.mp3=. --include-data-file=xxxb-Font.otf=. --include-data-file=LICENSE=. --no-deployment-flag=excluded-module-usage main.py
windoof:
	wine pyinstaller --onefile --windowed --name TippX --add-data "Ding.wav;." --add-data "Doeng.mp3;." --add-data "xxxb-Font.otf;." --add-data "LICENSE;." --icon=\TippX.ico main.py
release: linux windoof
