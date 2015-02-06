# We cannot make this package noarch but there are no binary files here
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	ibus - table-based engine
Name:		ibus-table
Version:	1.5.0
Release:	2
Group:		System/Internationalization
License:	GPLv2+
Url:		http://code.google.com/p/ibus/
Source0:	http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:	ibus-table.filter
Source2:	ibus-table.script
Source10:	%{name}.rpmlintrc
BuildRequires:	pkgconfig(ibus-1.0)
BuildRequires:	pkgconfig(python)
Requires:	ibus
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	ibus-table-compose < 1.5.0
Obsoletes:	ibus-table-latex < 1.5.0

%description
ibus - table-based engine.

%files -f %{name}.lang
%{_bindir}/ibus-table-createdb
%{_libexecdir}/ibus-engine-table
%{_libdir}/pkgconfig/ibus-table.pc
%{_datadir}/ibus-table
%{_datadir}/ibus/component/*.xml
%{_var}/lib/rpm/filetriggers/*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std NO_INDEX=1

%find_lang %{name}

install -d -m 0755 %{buildroot}%{_var}/lib/rpm/filetriggers
install -m 0644 %{SOURCE1} %{buildroot}%{_var}/lib/rpm/filetriggers
install -m 0755 %{SOURCE2} %{buildroot}%{_var}/lib/rpm/filetriggers

