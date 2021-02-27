#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		qrcode
Summary:	QR Code image generator
Name:		python-%{module}
Version:	5.3
Release:	5
License:	BSD
Group:		Libraries/Python
Source0:	https://github.com/lincolnloop/python-qrcode/archive/v5.3/%{name}-%{version}.tar.gz
# Source0-md5:	81e3670f61bdf186ded61d6bafa847ec
URL:		https://pypi.python.org/pypi/qrcode
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pillow
BuildRequires:	python-six
%endif
%endif
%if %{with python3}
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pillow
BuildRequires:	python3-six
%endif
%endif
Requires:	python-pillow
Requires:	python-six
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QR Code image generator.

%package -n python3-%{module}
Summary:	QR Code image generator
Group:		Libraries/Python
Requires:	python3-pillow
Requires:	python3-six

%description -n python3-%{module}
QR Code image generator.

%prep
%setup -q

%build
%if %{with python2}
%py_build %{?with_tests:test -s qrcode.tests.test_qrcode}
%endif

%if %{with python3}
%py3_build %{?with_tests:test -s qrcode.tests.test_qrcode}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.rst README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES.rst README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info

%attr(755,root,root) %{_bindir}/qr
%{_mandir}/man1/qr.1*
%endif
