.PHONY: build fix-perms cp-files
build: fix-perms
	fakeroot dpkg-deb --build Package
cp-files: clean
	$(MAKE) -C .. standalone
	mkdir -p ./Package/opt/TippX
	cp -r ../main.dist/* ./Package/opt/TippX/
fix-perms: cp-files
	chmod 0644 Package/DEBIAN/control
	chmod 0755 Package/usr/bin/*
clean:
	rm -rf ./Package/opt/
	rm -f Package.deb