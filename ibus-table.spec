%define	version 0.1.1.20081115
%define	release %mkrel 2

Name:      ibus-table
Summary:   ibus - table-based engine
Version:   %{version}
Release:   %{release}
Group:     System/Internationalization
License:   GPLv2+
URL:       http://code.google.com/p/ibus/
Source0:   http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: python-devel
BuildRequires: swig
BuildArch:	noarch
Requires:	ibus

%description
ibus - table-based engine.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x --build=%_host \
	--disable-static \
	--enable-zhengma \
	--enable-wubi86 \
	--enable-wubi98 \
	--enable-cangjie5 \
	--enable-erbi-qs \
	--enable-additional
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/ibus/engine/*.engine
