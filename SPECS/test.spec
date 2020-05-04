%define install_dir /data/app

Name: test
Version: 1.0.0
Release: 1%{?dist}
Summary: Test Package      
Packager: Xiaok <luxiaok2008@gmail.com>
Vendor: KK-Studio
Group: Applications/File
License: GPLv2
URL: https://github.com/luxiaok    
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch


%description
This is a test rpm package.


%prep
%setup -q


%build


%install
mkdir -p $RPM_BUILD_ROOT/%{install_dir}
cp -rap test $RPM_BUILD_ROOT/%{install_dir}


%pre


%post
if [ ! -L /usr/bin/foo ] ; then
    ln -s %{install_dir}/%{name}/bin/foo /usr/bin/
fi


%preun


%postun
rm -f /usr/bin/foo


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
%{install_dir}/test


%changelog
* Sun Apr 19 2020 Xiaok <luxiaok2008@gmail.com> - 1.0.0
- Release the first package for test
