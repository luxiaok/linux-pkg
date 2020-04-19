%define install_dir /data/app

Name: test
Version: 1.0.0
Release: 1%{?dist}
Summary: Test Package      
Packager: luxiaok2008@gmail.com
Vendor: Luxiaok
Group: Applications/File
License: GPLv2
URL: https://github.com/luxiaok    
Source0: %{name}-%{version}.tar.gz


%description
Descriptions for test.


%prep
%setup -q


%build


%install
rm -rf $RPM_BUILD_ROOT
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
