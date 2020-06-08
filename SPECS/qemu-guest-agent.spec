Name: qemu-guest-agent
Version: 2.12.1
Release: 1%{?dist}
Summary: QEMU Guest Agent (QGA)
Packager: Xiaok <luxiaok2008@gmail.com>
Vendor: KK-Studio
Group: Development/Tools
License: GPLv2
URL: https://github.com/luxiaok
Source0: %{name}-%{version}.tar.gz

# For RHEL 6
%if 0%{?rhel} == 6
Epoch: 2
%endif

%description
This package provides a qemu guest agent daemon to be running inside of
linux guests to provide the guest information.


%prep
%setup -q


%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{etc/init.d,etc/sysconfig,usr/bin}
cp etc/init.d/qemu-ga $RPM_BUILD_ROOT/etc/init.d/
cp etc/sysconfig/qemu-ga $RPM_BUILD_ROOT/etc/sysconfig/
cp usr/bin/qemu-ga $RPM_BUILD_ROOT/usr/bin/


%pre


%post
chkconfig --add qemu-ga 2>&1 >/dev/null


%preun
/etc/init.d/qemu-ga stop 2>&1 >/dev/null
chkconfig --del qemu-ga 2>&1 >/dev/null


%postun

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
/etc/init.d/qemu-ga
/etc/sysconfig/qemu-ga
/usr/bin/qemu-ga

%changelog
