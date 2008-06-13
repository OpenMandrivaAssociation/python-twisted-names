%define version 8.1.0
%define rel 1

Summary:        An DNS protocol implementation with client and server
Name:           python-twisted-names
Version: %version
Release: %mkrel %rel
Source0:        http://tmrc.mit.edu/mirror/twisted/Names/8.1/TwistedNames-%{version}.tar.bz2
License:        MIT
Group:          Development/Python
URL:            http://twistedmatrix.com/trac/wiki/TwistedNames
BuildRoot:      %{_tmppath}/%{name}-buildroot
BuildRequires:	python-devel python-twisted-core
Requires:       python-twisted-core

%description
Twisted Names is both a domain name server as well as a client resolver 
library.

Twisted Names comes with an "out of the box" nameserver which can read most 
BIND-syntax zone files as well as a simple Python-based configuration format. 
Twisted Names can act as an authoritative server, perform zone transfers from 
a master to act as a secondary, act as a caching nameserver, or any combination
of these. 

Twisted Names' client resolver library provides functions to query for all 
commonly used record types as well as a replacement for the blocking 
gethostbyname() function provided by the Python stdlib socket module.

%prep
%setup -q -n TwistedNames-%version

%build
%__python setup.py build

%install
%__rm -rf %buildroot
%__python setup.py install --root  %buildroot --install-purelib=%py_platsitedir

%clean
%__rm -rf %buildroot

%files
%defattr(0644,root,root,0755)
%doc LICENSE README doc/*
%py_platsitedir/twisted/names/
%py_platsitedir/twisted/plugins/*
%if %mdkversion >= 200710
%py_platsitedir/Twisted*egg-info
%endif


