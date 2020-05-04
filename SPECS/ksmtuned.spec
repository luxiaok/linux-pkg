Name:     ksmtuned
Version:  1.0.0
Release:  1%{?dist}
Summary:  Kernel Samepage Merging
Group:    Development/Tools
Packager: Xiaok <luxiaok2008@gmail.com>
Vendor:   KK-Studio
License:  GPLv2
URL:      https://github.com/luxiaok
Source0:  %{name}-%{version}.tar.gz

%description
Kernel Samepage Merging

%prep
%setup -q

%build
gcc ksmctl.c -o ksmctl

%install
install -D -p -m 0644 ksm.service $RPM_BUILD_ROOT%{_unitdir}/ksm.service
install -D -p -m 0644 ksm.sysconfig $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/ksm
install -D -p -m 0755 ksmctl $RPM_BUILD_ROOT%{_libexecdir}/ksmctl
install -D -p -m 0644 ksmtuned.service $RPM_BUILD_ROOT%{_unitdir}/ksmtuned.service
install -D -p -m 0755 ksmtuned $RPM_BUILD_ROOT%{_sbindir}/ksmtuned
install -D -p -m 0644 ksmtuned.conf $RPM_BUILD_ROOT%{_sysconfdir}/ksmtuned.conf

%post
%systemd_post ksm.service
%systemd_post ksmtuned.service

%preun
%systemd_preun ksm.service
%systemd_preun ksmtuned.service

%postun
%systemd_postun_with_restart ksm.service
%systemd_postun_with_restart ksmtuned.service

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/ksmtuned.conf
%config(noreplace) %{_sysconfdir}/sysconfig/ksm
%{_unitdir}/ksm.service
%{_unitdir}/ksmtuned.service
%{_libexecdir}/ksmctl
%{_sbindir}/ksmtuned

%changelog
