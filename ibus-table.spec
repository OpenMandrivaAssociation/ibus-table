%define	version 1.3.0.20100621
%define	release %mkrel 3

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


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.0.20100621-3mdv2011.0
+ Revision: 665494
- mass rebuild

* Wed Nov 03 2010 Funda Wang <fwang@mandriva.org> 1.3.0.20100621-2mdv2011.0
+ Revision: 592715
- rebuild for py2.7

* Thu Jun 24 2010 Funda Wang <fwang@mandriva.org> 1.3.0.20100621-1mdv2010.1
+ Revision: 548991
- New version 1.3.0.20100621

* Fri Feb 12 2010 Funda Wang <fwang@mandriva.org> 1.2.0.20100111-1mdv2010.1
+ Revision: 504507
- New version 1.2.0.20100111

* Sun Jan 17 2010 Funda Wang <fwang@mandriva.org> 1.2.0.20091113-3mdv2010.1
+ Revision: 492802
- split out compose and latext methods (for furture reorganize)

* Sat Jan 09 2010 Funda Wang <fwang@mandriva.org> 1.2.0.20091113-2mdv2010.1
+ Revision: 487915
- add ibus-table file trigger to simplify table installation

* Fri Nov 13 2009 Funda Wang <fwang@mandriva.org> 1.2.0.20091113-1mdv2010.1
+ Revision: 465675
- New version 20091113

* Tue Sep 15 2009 Funda Wang <fwang@mandriva.org> 1.2.0.20090912-1mdv2010.0
+ Revision: 441989
- fix file list
- New version 1.2.0.20090912

* Tue Aug 04 2009 Funda Wang <fwang@mandriva.org> 1.2.0.20090804-1mdv2010.0
+ Revision: 408681
- new version 1.2.0.20090804
- new version 1.2.0

* Mon Jun 15 2009 Funda Wang <fwang@mandriva.org> 1.1.0.20090615-1mdv2010.0
+ Revision: 386038
- fix file list
- New version 1.1.0.20090609

* Thu Jun 11 2009 Funda Wang <fwang@mandriva.org> 1.1.0.20090609-1mdv2010.0
+ Revision: 385122
- New version 1.1.0.20090609

* Wed Jun 03 2009 Funda Wang <fwang@mandriva.org> 1.1.0.20090603-1mdv2010.0
+ Revision: 382428
- New version 1.1.0.20090603

* Tue Jun 02 2009 Funda Wang <fwang@mandriva.org> 1.1.0.20090601-1mdv2010.0
+ Revision: 382246
- New version 1.1.0.20090601

* Thu May 28 2009 Funda Wang <fwang@mandriva.org> 1.1.0.20090527-1mdv2010.0
+ Revision: 380315
- new version 1.1.0.20090527

* Tue May 05 2009 Funda Wang <fwang@mandriva.org> 1.1.0.20090505-1mdv2010.0
+ Revision: 372179
- New version 1.1.0.20090505

* Sat Mar 07 2009 Funda Wang <fwang@mandriva.org> 1.1.0.20090306-1mdv2009.1
+ Revision: 351834
- New version 1.1.0.20090306

* Sat Feb 21 2009 Funda Wang <fwang@mandriva.org> 1.1.0.20090220-1mdv2009.1
+ Revision: 343570
- New version 1.1.0.20090220

* Sun Jan 04 2009 Funda Wang <fwang@mandriva.org> 0.1.2.20090104-1mdv2009.1
+ Revision: 324424
- New version 0.1.2.20090104
  engine splitted

* Thu Dec 25 2008 Funda Wang <fwang@mandriva.org> 0.1.1.20081115-2mdv2009.1
+ Revision: 318669
- rebuild for new python

* Mon Nov 17 2008 Funda Wang <fwang@mandriva.org> 0.1.1.20081115-1mdv2009.1
+ Revision: 303971
- New version 0.1.1.20081115

* Wed Oct 22 2008 Funda Wang <fwang@mandriva.org> 0.1.1.20081014-2mdv2009.1
+ Revision: 296428
- enable engine

* Fri Oct 17 2008 Funda Wang <fwang@mandriva.org> 0.1.1.20081014-1mdv2009.1
+ Revision: 294563
- New version 0.1.1.20081014

* Fri Sep 05 2008 Funda Wang <fwang@mandriva.org> 0.1.1.20080901-1mdv2009.0
+ Revision: 281259
- new version

* Sun Aug 31 2008 Funda Wang <fwang@mandriva.org> 0.1.1.20080829-1mdv2009.0
+ Revision: 277703
- New version 0.1.1.20080829

* Mon Aug 25 2008 Funda Wang <fwang@mandriva.org> 0.1.1.20080823-1mdv2009.0
+ Revision: 275875
- import ibus-table


