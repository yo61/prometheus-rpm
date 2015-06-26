VERSION=0.10.0
PWD=$(shell pwd)

all: rpm clean

rpm:
	mkdir -p "$(PWD)/rpmbuild"
	mkdir -p "$(PWD)/rpmbuild/SOURCES/"
	cd "$(PWD)/rpmbuild/SOURCES" && git clone https://github.com/prometheus/node_exporter.git
	cp -Rv contrib "$(PWD)/rpmbuild/SOURCES/node_exporter"
	cd "$(PWD)/rpmbuild/SOURCES" && mv node_exporter prometheus-node-exporter-$(VERSION)
	cd "$(PWD)/rpmbuild/SOURCES" && tar cvfz prometheus-node-exporter-$(VERSION).tar.gz prometheus-node-exporter-$(VERSION)
	rpmbuild --define '_topdir '"$(PWD)/rpmbuild" -ba --clean contrib/node_exporter.spec

deploy:
	curl -v -F r=$(REPOSITORY) -F hasPom=false -F e=rpm -F g=$(GROUPID) -F a=prometheus-node-exporter -F v=$(VERSION) -F p=RPM -F file=@$(WORKSPACE)/prometheus-rpm/node_exporter/rpmbuild/RPMS/x86_64/prometheus-node-exporter-$(VERSION)-1.el6.x86_64.rpm -u $(REPOSITORY_CREDENTIALS) $(REPOSITORY_URL)

clean:
	rm -rf "~/rpmbuild/SOURCES/prometheus-node-exporter-$(VERSION)"
	rm -rf "~/rpmbuild/SOURCES/prometheus-node-exporter-$(VERSION).tar.gz"
