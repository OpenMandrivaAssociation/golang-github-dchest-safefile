# Run tests in check section
%bcond_without check

%global goipath         github.com/dchest/safefile
%global commit          855e8d98f1852d48dde521e0522408d1fe7e836a

%global common_description %{expand:
Go package safefile implements safe "atomic" saving of files.

Instead of truncating and overwriting the destination file, it creates a 
temporary file in the same directory, writes to it, and then renames the 
temporary file to the original name when calling Commit.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Implements safe "atomic" saving of files
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}


%package devel
Summary:       %{summary}

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git855e8d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180529git855e8d9
- First package for Fedora

