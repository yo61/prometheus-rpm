VERSION=0.1.0
PWD=$(shell pwd)

all: rpm clean

rpm:
	mkdir -p "$(PWD)/rpmbuild"
	mkdir -p "$(PWD)/rpmbuild/SOURCES/"
	mkdir -p "$(PWD)/rpmbuild/SOURCES/alertmanager-$(VERSION).linux-amd64"
	cd "$(PWD)/rpmbuild/SOURCES/alertmanager-$(VERSION).linux-amd64" && wget https://github.com/prometheus/alertmanager/releases/download/$(VERSION)/alertmanager-$(VERSION).linux-amd64.tar.gz
	cd "$(PWD)/rpmbuild/SOURCES/alertmanager-$(VERSION).linux-amd64" && tar xzvf *tar.gz
	mv "$(PWD)/rpmbuild/SOURCES/alertmanager-$(VERSION).linux-amd64/alertmanager-$(VERSION).linux-amd64" "$(PWD)/rpmbuild/SOURCES/alertmanager-$(VERSION).linux-amd64/alertmanager"
	cp -Rv contrib "$(PWD)/rpmbuild/SOURCES/alertmanager-$(VERSION).linux-amd64"
	cd "$(PWD)/rpmbuild/SOURCES" && tar cvfz alertmanager-$(VERSION).linux-amd64.tar.gz alertmanager-$(VERSION).linux-amd64
	rpmbuild --define '_topdir '"$(PWD)/rpmbuild" -ba --clean contrib/alertmanager.spec

deploy:
	curl -v -F r=$(REPOSITORY) -F hasPom=false -F e=rpm -F g=$(GROUPID) -F a=alertmanager -F v=$(VERSION) -F p=RPM -F file=@$(WORKSPACE)/alertmanager-rpm/alertmanager/rpmbuild/RPMS/x86_64/alertmanager-$(VERSION)-1.el6.x86_64.rpm -u $(REPOSITORY_CREDENTIALS) $(REPOSITORY_URL)

clean:
	rm -rf "$(PWD)/rpmbuild/SOURCES/alertmanager-$(VERSION)"
	rm "$(PWD)/rpmbuild/SOURCES/alertmanager-$(VERSION).linux-amd64.tar.gz"
