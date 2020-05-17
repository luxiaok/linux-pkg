Name:       autoconf
Summary:    A GNU tool for automatically configuring source code
Version:    2.69
Release:    1%{?dist}
License:    GPLv3+ and GFDL
Group:      Development/Tools
URL:        https://ftp.gnu.org/gnu/autoconf
Vendor:     KK-Studio
Packager:   Xiaok <luxiaok2008@gmail.com>
Source:     https://ftp.gnu.org/gnu/autoconf/%{name}-%{version}.tar.xz

%description
GNU Autoconf is a tool for configuring source code and Makefiles.
Using Autoconf, programmers can create portable and configurable
packages, since the person building the package is allowed to
specify various configuration options.

%prep
%setup -q

%build
%configure --prefix=/usr
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install %{?_smp_mflags}
rm -rf $RPM_BUILD_ROOT/usr/share/info

%clean
rm -rf $RPM_BUILD_ROOT

%post

%postun

%files
%defattr(-,root,root)
%doc
%{_bindir}/auto*
%{_bindir}/ifn*
%{_datadir}/autoconf
%{_mandir}/man1

%changelog
* Fri May 15 2020 Xiaok <luxiaok2008@gmail.com> - 2.69-1
- Build rpm package for v2.69-1

