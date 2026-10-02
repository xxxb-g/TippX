.PHONY: release deb rpm arch clean prepare

APP := TippX

# Version aus ../main.py lesen und führendes "v" entfernen:
VERSION := $(patsubst v%,%,$(shell python3 -c 'import ast; tree=ast.parse(open("../main.py", encoding="utf-8").read()); print(next(n.value.value for n in ast.walk(tree) if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "Version" for t in n.targets) and isinstance(n.value, ast.Constant) and isinstance(n.value.value, str)))'))

DEB := $(APP)_$(VERSION)_amd64.deb

PACKAGE_DIR := Package
DEB_METADATA := deb/DEBIAN
DEB_BUILD := .deb-package


# Release
release: deb rpm arch


# Debian
deb: prepare
	rm -rf $(DEB_BUILD)

	# Temporären Debian-Paketbaum erzeugen
	mkdir -p $(DEB_BUILD)/DEBIAN

	# Debian-Metadaten kopieren und Version setzen
	sed 's/^Version:.*/Version: $(VERSION)/' \
		$(DEB_METADATA)/control \
		> $(DEB_BUILD)/DEBIAN/control

	# Gemeinsame Programmdateien kopieren
	cp -a $(PACKAGE_DIR)/. $(DEB_BUILD)/

	# Rechte setzen
	chmod 0644 $(DEB_BUILD)/DEBIAN/control
	chmod 0755 $(DEB_BUILD)/usr/bin/*

	# .deb bauen
	fakeroot dpkg-deb --build $(DEB_BUILD) $(DEB)

	# Temporären Debian-Paketbaum wieder entfernen
	rm -rf $(DEB_BUILD)


# Gemeinsame Vorbereitung
prepare:
	$(MAKE) -C .. standalone

	rm -rf $(PACKAGE_DIR)/opt/$(APP)
	mkdir -p $(PACKAGE_DIR)/opt/$(APP)

	cp -a ../main.dist/. $(PACKAGE_DIR)/opt/$(APP)/


# Aufräumen
clean:
	rm -rf $(PACKAGE_DIR)/opt/$(APP)
	rm -rf $(DEB_BUILD)
	rm -f $(DEB)