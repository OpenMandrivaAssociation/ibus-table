# We cannot make this package noarch but there are no binary files here
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	ibus - table-based engine
Name:		ibus-table
Version:	1.16.13
Release:	1
Group:		System/Internationalization
License:	GPLv2+
URL:       https://github.com/kaio/ibus-table
Source0:   https://github.com/kaio/ibus-table/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:	ibus-table.filter
Source2:	ibus-table.script
Source10:	%{name}.rpmlintrc

BuildRequires:	pkgconfig(ibus-1.0)
BuildRequires:	pkgconfig(python)
BuildRequires: gettext-devel
BuildRequires: docbook-utils

Requires:	ibus
Requires: python
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	ibus-table-compose < 1.5.0
Obsoletes:	ibus-table-latex < 1.5.0

%description
ibus - table-based engine.

#----------------------------------------------------------------------------

%%prep
%setup -q 

%build
sh autogen.sh
%configure
%make_build

%install
%make_install NO_INDEX=1

mkdir -p %{buildroot}%{_datadir}/pkgconfig/
mv %{buildroot}%{_libdir}/pkgconfig/ibus-table.pc %{buildroot}%{_datadir}/pkgconfig/ibus-table.pc

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/ibus-table-createdb
%{_libexecdir}/ibus-*
%{_datadir}/pkgconfig/ibus-table.pc
%{_datadir}/applications/ibus-setup-table.desktop
%{_datadir}/ibus-table
%{_datadir}/ibus/component/*.xml
%{_datadir}/metainfo/*.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.ibus.engine.table.gschema.xml
%{_mandir}/man1/ibus-*
%{_iconsdir}/hicolor/*x*/apps/ibus-table.png
%{_iconsdir}/hicolor/scalable/apps/ibus-table.svg
