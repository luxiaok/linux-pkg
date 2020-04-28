%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
Name:           python-pycurl
Version:        7.43.0.5
Release:        1%{?dist}
Summary:        A Python interface to libcurl
Vendor:         Xiaok <luxiaok2008@gmail.com>
Packager:       KK-Studio
Group:          Development/Languages
License:        LGPLv2+ or MIT
URL:            http://pycurl.io/
Source0:        https://files.pythonhosted.org/packages/ef/05/4b773f74f830a90a326b06f9b24e65506302ab049e825a3c0b60b1a6e26a/pycurl-7.43.0.5.tar.gz
Requires:       keyutils-libs
BuildRequires:  python-devel
BuildRequires:  openssl-devel

# curl-7.29.0-16 or newer is needed for CURL_SSLVERSION_TLSv1_[0-2]
BuildRequires:  libcurl-devel >= 7.29.0-16

Provides:       pycurl = %{version}-%{release}

%description
PycURL is a Python interface to libcurl. PycURL can be used to fetch
objects identified by a URL from a Python program, similar to the
urllib Python module. PycURL is mature, very fast, and supports a lot
of features.

%prep
%setup0 -q -n pycurl-%{version}
chmod a-x examples/*

%build
%{__python} setup.py build --with-nss

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
rm -rf %{buildroot}%{_datadir}/doc/pycurl

%files
%doc ChangeLog examples doc tests
%{python_sitearch}/*

%changelog
* Tue Apr 28 2020 Xiaok <luxiaok@gmail.com> - 7.43.0.5-1
- compiled pycurl-v7.43.0.5

