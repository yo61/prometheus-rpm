Name:		prometheus
Version:	0.12.0
Release:	1%{?dist}
Summary:	Prometheus is a systems and service monitoring system. It collects metrics from configured targets at given intervals, evaluates rule expressions, displays the results, and can trigger alerts if some condition is observed to be true.
Group:		System Environment/Daemons
License:	See the LICENSE file at github.
URL:		https://github.com/prometheus/prometheus
Source0:	https://github.com/prometheus/prometheus/archive/%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:  git
BuildRequires:  mercurial
BuildRequires:  gzip
BuildRequires:  curl
BuildRequires:  sed
BuildRequires:  vim-common
Requires(pre):  /usr/sbin/useradd
Requires:       daemonize
AutoReqProv:	No

%description

Prometheus is a systems and service monitoring system.
It collects metrics from configured targets at given intervals, evaluates
rule expressions, displays the results, and can trigger alerts if
some condition is observed to be true.

%prep
%setup -q

%build
make binary %{?_smp_mflags}

%install
mkdir -vp $RPM_BUILD_ROOT/var/log/prometheus/
mkdir -vp $RPM_BUILD_ROOT/var/run/prometheus
mkdir -vp $RPM_BUILD_ROOT/var/lib/prometheus
mkdir -vp $RPM_BUILD_ROOT/usr/bin
mkdir -vp $RPM_BUILD_ROOT/etc/init.d
mkdir -vp $RPM_BUILD_ROOT/etc/prometheus
mkdir -vp $RPM_BUILD_ROOT/etc/sysconfig
install -m 755 prometheus $RPM_BUILD_ROOT/usr/bin/prometheus
install -m 644 contrib/prometheus.conf $RPM_BUILD_ROOT/etc/prometheus/prometheus.conf
install -m 644 contrib/prometheus.rules $RPM_BUILD_ROOT/etc/prometheus/prometheus.rules
install -m 755 contrib/prometheus.init $RPM_BUILD_ROOT/etc/init.d/prometheus
install -m 644 contrib/prometheus.sysconfig $RPM_BUILD_ROOT/etc/sysconfig/prometheus

%clean
make clean

%pre
getent group prometheus >/dev/null || groupadd -r prometheus
getent passwd prometheus >/dev/null || \
  useradd -r -g prometheus -s /sbin/nologin \
    -d $RPM_BUILD_ROOT/var/lib/prometheus/ -c "prometheus Daemons" prometheus
exit 0

%post
chgrp prometheus /var/run/prometheus
chmod 774 /var/run/prometheus
chown prometheus:prometheus /var/log/prometheus
chmod 744 /var/log/prometheus

%files
%defattr(-,root,root,-)
/usr/bin/prometheus
%config(noreplace) /etc/prometheus/prometheus.conf
%config(noreplace) /etc/prometheus/prometheus.rules
/etc/init.d/prometheus
%config(noreplace) /etc/sysconfig/prometheus
#/var/run/prometheus
#/var/log/prometheus
