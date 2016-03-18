# prometheus-rpm
Stuff to build rpms for prometheus, node_exporter and alertmanager for amd64 until rpms are provided by the prometheus.io project itself.

Requires rpmbuild to be installed. To run, simply go into a subdir and run make. 

This is currently used internally for our RHEL 6.6 infrastructure, 'make deploy' deploys it to our internal Nexus repository where it is picked up by yum.
