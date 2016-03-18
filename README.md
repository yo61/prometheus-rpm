# prometheus-rpm
Stuff to build a prometheus.io rpm until provided by the prometheus project.

Requires rpmbuild to be installed. To run, simply go into a subdir and run make. 

This is currently used internally for our RHEL 6.6 infrastructure, make deploy deploys it to our internal Nexus repository where it is picked up by yum.
