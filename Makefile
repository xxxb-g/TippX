.phony: build
build:
	python3 -m nuitka --onefile --include-module="random" --include-module="pygame" --product-name=TippX_by_xxxb --output-filename="TippX" --nofollow-import-to=unittest --nofollow-import-to=numpy --nofollow-import-to=pygame.surfarray --nofollow-import-to=pygame.sndarray --nofollow-import-to=pygame.image --nofollow-import-to=pygame.transform main.py