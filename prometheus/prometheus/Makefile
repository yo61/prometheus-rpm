VERSION=0.12.0

all: rpm clean

rpm:
	mkdir -p ~/rpmbuild
	mkdir -p ~/rpmbuild/SOURCES/
	cd ~/rpmbuild/SOURCES && git clone https://github.com/prometheus/prometheus.git
	cd ~/rpmbuild/SOURCES/prometheus && git checkout tags/$(VERSION)
	cp -Rv contrib ~/rpmbuild/SOURCES/prometheus
	cd ~/rpmbuild/SOURCES && mv prometheus prometheus-$(VERSION)
	cd ~/rpmbuild/SOURCES && tar cvfz $(VERSION).tar.gz prometheus-$(VERSION)
	rpmbuild -ba --clean contrib/prometheus.spec

clean:
	rm -rf "~/rpmbuild/SOURCES/prometheus-$(VERSION)"
	rm ~/rpmbuild/SOURCES/$(VERSION).tar.gz
