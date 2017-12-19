#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : traitlets
Version  : 4.3.2
Release  : 9
URL      : http://pypi.debian.net/traitlets/traitlets-4.3.2.tar.gz
Source0  : http://pypi.debian.net/traitlets/traitlets-4.3.2.tar.gz
Summary  : Traitlets Python config system
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: traitlets-legacypython
Requires: traitlets-python3
Requires: traitlets-python
Requires: Sphinx
Requires: ipython_genutils
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
# Traitlets
[![Build Status](https://travis-ci.org/ipython/traitlets.svg?branch=master)](https://travis-ci.org/ipython/traitlets)
[![Documentation Status](https://readthedocs.org/projects/traitlets/badge/?version=latest)](http://traitlets.readthedocs.org/en/latest/?badge=latest)

%package legacypython
Summary: legacypython components for the traitlets package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the traitlets package.


%package python
Summary: python components for the traitlets package.
Group: Default
Requires: traitlets-legacypython
Requires: traitlets-python3

%description python
python components for the traitlets package.


%package python3
Summary: python3 components for the traitlets package.
Group: Default
Requires: python3-core

%description python3
python3 components for the traitlets package.


%prep
%setup -q -n traitlets-4.3.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507180136
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1507180136
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
