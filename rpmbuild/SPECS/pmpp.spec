%define _topdir     /rpmbuild
%define name        pmpp
%define release     1
%define version     1.2.0
%define buildroot %{_topdir}/%{name}-%{version}-root
%define pg_version  9.6

BuildRoot:      %{buildroot}
Summary:        PMPP extension for PostgreSQL
License:        GPL
Name:           %{name}
Version:        %{version}
Release:        %{release}
Source:         %{version}.zip
Group:          Development/Tools

URL:            https://github.com/moat/pmpp

%description
PMPP is an extension that provides a means of manually dividing one large query into several smaller ones that return the same shape of result set, allowing for additional query layers on the combined set. This is accomplished through use of polymorphic functions performing asynchronous libpq commands and queue management.

%prep
%setup

%build
make %{?_smp_mflags}

%install
%make_install

%files
/usr/pgsql-%{pg_version}/lib/pmpp.so
/usr/pgsql-%{pg_version}/doc/extension/pmpp.md
/usr/pgsql-%{pg_version}/lib/distribute.so
/usr/pgsql-%{pg_version}/lib/num_cpus.so
/usr/pgsql-%{pg_version}/share/extension/pmpp--1.0.1--1.0.3.sql
/usr/pgsql-%{pg_version}/share/extension/pmpp--1.0.3--1.1.0.sql
/usr/pgsql-%{pg_version}/share/extension/pmpp--1.1.0--1.1.1.sql
/usr/pgsql-%{pg_version}/share/extension/pmpp--1.1.1--1.2.0.sql
/usr/pgsql-%{pg_version}/share/extension/pmpp--1.2.0.sql
/usr/pgsql-%{pg_version}/share/extension/pmpp.control

%changelog
* Fri Apr 28 2017 Andrey Zhidenkov <pensnarik@gmail.com>
- Initial version of the package
