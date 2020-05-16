Name:          libzip
Summary:       C library for reading, creating, and modifying zip archives
Version:       1.6.1
Release:       1%{?dist}
License:       BSD
Group:         System Environment/Libraries
URL:           https://github.com/nih-at/libzip
Vendor:        GitHub
Packager:      Xiaok <luxiaok2008@gmail.com>
Source:        libzip-%{version}.tar.xz
BuildRequires: cmake3

%description
libzip is a C library for reading, creating, and modifying zip archives. Files
can be added from data buffers, files, or compressed data copied directly from
other zip archives. Changes made without closing the archive can be reverted.
The API is documented by man pages.

%prep
%setup -q

%build
mkdir build
cd build
cmake3 .. -DCMAKE_INSTALL_PREFIX=/usr
make %{?_smp_mflags}

%install
# Clean up in case there is trash left from a previous build
rm -rf $RPM_BUILD_ROOT
cd build
make DESTDIR=$RPM_BUILD_ROOT install %{?_smp_mflags}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc
%{_bindir}/zipcmp
%{_bindir}/zipmerge
%{_bindir}/ziptool
%{_includedir}/zipconf.h
%{_includedir}/zip.h
%{_libdir}/libzip.so
%{_libdir}/libzip.so.5
%{_libdir}/libzip.so.5.1
%{_libdir}/pkgconfig/libzip.pc
%{_mandir}/man1
%{_mandir}/man3

%changelog
* Fri May 15 2020 Xiaok <luxiaok2008@gmail.com> - 1.6.1-1
- Build rpm package for v1.6.1-1
