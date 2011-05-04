%define		plugin	tinyscrollbar
Summary:	Tiny Scrollbar - A lightweight jQuery plugin
Name:		jquery-%{plugin}
Version:	1.6
Release:	1
License:	MIT / GPL v2
Group:		Applications/WWW
Source0:	http://www.baijs.nl/tinyscrollbar/js/jquery.tinyscrollbar.min.js
# Source0-md5:	6920d962d760b0a7734a40bbe53a5b71
URL:		http://www.baijs.nl/tinyscrollbar/
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	jquery
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
Tiny Scrollbar can be used for scrolling content. It was built using
the JavaScript jQuery library. Tiny scrollbar was designed to be a
dynamic lightweight utility that gives webdesigners a powerful way of
enhancing a websites user interface.

%prep
%setup -qcT
cp -p %{SOURCE0} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -p jquery.*.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}
