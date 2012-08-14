%define		plugin	tinyscrollbar
Summary:	Tiny Scrollbar - A lightweight jQuery plugin
Name:		jquery-%{plugin}
Version:	1.8
Release:	1
License:	MIT / GPL v2
Group:		Applications/WWW
Source0:	http://www.baijs.nl/tinyscrollbar/js/jquery.tinyscrollbar.js
# Source0-md5:	d857f9e245226e306d9c4a19988954a3
Source1:	http://www.baijs.nl/tinyscrollbar/js/jquery.tinyscrollbar.min.js
# Source1-md5:	d49ecb6a2e39c243a69ed6ca64627e54
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
cp -p %{SOURCE1} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -p jquery.%{plugin}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.js
cp -p jquery.%{plugin}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
ln -s %{plugin}-%{version}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.min.js

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}
