VERSION=0.12.0
PWD=$(shell pwd)

all: rpm clean

rpm:
	mkdir -p "$(PWD)/rpmbuild"
	mkdir -p "$(PWD)/rpmbuild/SOURCES/"
	cd "$(PWD)/rpmbuild/SOURCES" && git clone https://github.com/prometheus/prometheus.git
	cd "$(PWD)/rpmbuild/SOURCES/prometheus" && git checkout tags/$(VERSION)
	cp -Rv contrib "$(PWD)/rpmbuild/SOURCES/prometheus"
	cd "$(PWD)/rpmbuild/SOURCES" && mv prometheus prometheus-$(VERSION)
	cd "$(PWD)/rpmbuild/SOURCES" && tar cvfz $(VERSION).tar.gz prometheus-$(VERSION)
	rpmbuild --define '_topdir' "$(PWD)/rpmbuild" -ba --clean contrib/prometheus.spec

clean:
	rm -rf "$(PWD)/rpmbuild/SOURCES/prometheus-$(VERSION)"
	rm "$(PWD)/rpmbuild/SOURCES/$(VERSION).tar.gz"
