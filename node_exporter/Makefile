VERSION=0.80

all: rpm clean

rpm:
	mkdir -p ~/rpmbuild
	mkdir -p ~/rpmbuild/SOURCES/
	cd ~/rpmbuild/SOURCES && git clone https://github.com/prometheus/node_exporter.git
	cp -Rv contrib ~/rpmbuild/SOURCES/node_exporter
	cd ~/rpmbuild/SOURCES && mv node_exporter prometheus-node-exporter-$(VERSION)
	cd ~/rpmbuild/SOURCES && tar cvfz prometheus-node-exporter-$(VERSION).tar.gz prometheus-node-exporter-$(VERSION)
	rpmbuild --clean -ba contrib/node_exporter.spec

deploy:
	curl -v -F r=$(REPOSITORY) -F hasPom=false -F e=rpm -F g=$(GROUPID) -F a=prometheus-node-exporter -F v=$(VERSION) -F p=RPM -F file=@$(WORKSPACE)/prometheus-rpm/node_exporter/rpmbuild/RPMS/x86_64/prometheus-node-exporter-$(VERSION)-1.el6.x86_64.rpm -u $(REPOSITORY_CREDENTIALS) $(REPOSITORY_URL)

clean:
	rm -rf "~/rpmbuild/SOURCES/prometheus-node-exporter-$(VERSION)"
	rm -rf "~/rpmbuild/SOURCES/prometheus-node-exporter-$(VERSION).tar.gz"
