#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : traitlets
Version  : 4.3.2
Release  : 12
URL      : http://pypi.debian.net/traitlets/traitlets-4.3.2.tar.gz
Source0  : http://pypi.debian.net/traitlets/traitlets-4.3.2.tar.gz
Summary  : Traitlets Python config system
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: traitlets-python3
Requires: traitlets-python
Requires: Sphinx
Requires: ipython_genutils
Requires: sphinx_rtd_theme
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
# Traitlets
[![Build Status](https://travis-ci.org/ipython/traitlets.svg?branch=master)](https://travis-ci.org/ipython/traitlets)
[![Documentation Status](https://readthedocs.org/projects/traitlets/badge/?version=latest)](http://traitlets.readthedocs.org/en/latest/?badge=latest)

%package python
Summary: python components for the traitlets package.
Group: Default
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
export SOURCE_DATE_EPOCH=1523309728
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
