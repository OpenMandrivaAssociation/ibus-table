%define	version 1.2.0.20090912
%define	release %mkrel 1

Name:      ibus-table
Summary:   ibus - table-based engine
Version:   %{version}
Release:   %{release}
Group:     System/Internationalization
License:   GPLv2+
URL:       http://code.google.com/p/ibus/
Source0:   http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ibus-devel >= 1.2.0
%py_requires -d
Requires:	ibus >= 1.2.0
Provides:	%{name}-devel = %{version}-%{release}

%description
ibus - table-based engine.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x \
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
%{_bindir}/ibus-table-createdb
%{_libexecdir}/ibus-engine-table
%{_libexecdir}/ibus-setup-table
%{_libdir}/pkgconfig/ibus-table.pc
%{_datadir}/ibus-table
%{_datadir}/ibus/component/*.xml
