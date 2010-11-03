%define	version 1.3.0.20100621
%define	release %mkrel 2

Name:      ibus-table
Summary:   ibus - table-based engine
Version:   %{version}
Release:   %{release}
Group:     System/Internationalization
License:   GPLv2+
URL:       http://code.google.com/p/ibus/
Source0:   http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:   ibus-table.filter
Source2:   ibus-table.script
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ibus-devel >= 1.2.0
BuildRequires:	python-devel
Requires:	ibus >= 1.2.0
Provides:	%{name}-devel = %{version}-%{release}

%description
ibus - table-based engine.

%package compose
Summary: Mimic Compose Key input
Group: System/Internationalization
Requires: %name >= 1.2.0.20091113-3
Conflicts: %name < 1.2.0.20091113-3

%description compose
Provides Mimic Compose Key input via ibus-table.

%package latex
Summary: Use LaTeX input keystrokes to input symbols
Group: System/Internationalization
Requires: %name >= 1.2.0.20091113-3
Conflicts: %name < 1.2.0.20091113-3

%description latex
Use LaTeX input keystrokes to input lots of symbols.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x \
	--enable-additional
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std NO_INDEX=1

%find_lang %name

install -d -m 0755 %buildroot%{_var}/lib/rpm/filetriggers
install -m 0644 %{SOURCE1} %buildroot%{_var}/lib/rpm/filetriggers
install -m 0755 %{SOURCE2} %buildroot%{_var}/lib/rpm/filetriggers

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%{_bindir}/ibus-table-createdb
%{_libexecdir}/ibus-engine-table
%{_libdir}/pkgconfig/ibus-table.pc
%{_datadir}/ibus-table
%{_datadir}/ibus/component/*.xml
%{_var}/lib/rpm/filetriggers/*
%exclude %{_datadir}/ibus-table/icons/compose.svg
%exclude %{_datadir}/ibus-table/tables/compose.db
%exclude %{_datadir}/ibus-table/icons/latex.svg
%exclude %{_datadir}/ibus-table/tables/latex.db

%files compose
%defattr(-,root,root)
%{_datadir}/ibus-table/icons/compose.svg
%{_datadir}/ibus-table/tables/compose.db

%files latex
%defattr(-,root,root)
%{_datadir}/ibus-table/icons/latex.svg
%{_datadir}/ibus-table/tables/latex.db
