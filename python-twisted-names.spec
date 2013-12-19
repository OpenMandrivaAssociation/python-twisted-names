%define mainver %(echo %{version} | sed -e 's/\\([0-9]*\\.[0-9]*\\)\\.[0-9]*/\\1/')

# There is no debug here, but can't build as noarch,
# since some 'twisted' modules are arch-dependent and all these modules
# should be located in the same place
%define debug_package %{nil}

Summary:	An DNS protocol implementation with client and server
Name:		python-twisted-names
Version:	13.1.0
Release:	1
License:	MIT
Group:		Development/Python
Url:		http://twistedmatrix.com/trac/wiki/TwistedNames
Source0:	http://twistedmatrix.com/Releases/Names/13.1/TwistedNames-%{version}.tar.bz2
BuildRequires:	pkgconfig(python)
BuildRequires:	python-twisted-core
Requires:	python-twisted-core

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
%setup -qn TwistedNames-%version

%build
%__python setup.py build

%install
%__python setup.py install --root=%{buildroot} --install-purelib=%{py_platsitedir}

%files
%defattr(0644,root,root,0755)
%doc LICENSE README doc/*
%dir %{py_platsitedir}/twisted/names
%{py_platsitedir}/twisted/names/*
%{py_platsitedir}/twisted/plugins/*
%{py_platsitedir}/*.egg-info


