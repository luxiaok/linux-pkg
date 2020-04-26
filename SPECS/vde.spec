Name:     vde
Version:  2.3.2
Release:  1%{?dist}
Summary:  Virtual Distributed Ethernet
Group:    Development/Tools
Packager: Xiaok <luxiaok2008@gmail.com>
Vendor:   KK-Studio
License:  GPL
URL:      https://github.com/virtualsquare/vde-2
Source0:  %{name}-%{version}.tar.gz

BuildRequires: libpcap-devel

%description
Virtual Distributed Ethernet
git-c7b36a57831a9067c8619c3e17a03e595623b3eb-20191011

%package -n vde-python
Summary: Virtual Distributed Ethernet support for Python

%description -n vde-python
Virtual Distributed Ethernet support for Python
git-c7b36a57831a9067c8619c3e17a03e595623b3eb-20191011

%prep
%setup -q

%build
autoreconf --install
%configure --prefix=/usr --sysconfdir=/etc --libdir=/usr/lib64
make

%install
make install DESTDIR=%{buildroot}

%post
ldconfig

%preun

%postun
ldconfig

%files
%defattr(-,root,root,-)
/etc/vde2
/usr/bin/*
/usr/sbin/vde_tunctl
/usr/libexec/vdetap
/usr/lib64/*
/usr/include/libvde*.h
/usr/share/man/*

%files -n vde-python
/usr/lib/python2.7/site-packages/*

%changelog
