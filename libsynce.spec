%define major		0
%define libname		%mklibname synce %{major}
%define develname	%mklibname synce -d
%define svn 0

Summary:	Basic library used by applications in the SynCE project
#Name:		synce-core
Name:		libsynce
Version:	0.16
Release:	3
License:	MIT
Group:		System/Libraries
Source0:	http://downloads.sourceforge.net/project/synce/SynCE/synce-core/synce-core-%{version}.tar.gz
URL:		http://synce.sourceforge.net/
BuildRequires:	dbus-glib-devel
BuildRequires:	dhcp-client
BuildRequires:	pkgconfig(udev)
BuildRequires:	pkgconfig(gudev-1.0)
BuildRequires:	python-devel
BuildRequires:	python-pyrex
BuildRequires:	pkgconfig(pygobject-2.0)


%description
Libsynce is part of the SynCE project. It is a library of basic
functions used by the rest of the project.

%package -n	synce-core
Summary:	Basic library used by applications in the SynCE project
Group:		Communications
Requires:	%{libname} = %{version}-%{release}

%description -n synce-core
Synce-core is part of the SynCE project. It is a library of basic
functions used by the rest of the project.


%package -n %{libname}
Summary:	Basic library used by applications in the SynCE project
Group:		System/Libraries
Requires:	synce-core = %{version}-%{release}

%description -n %{libname}
Libsynce is part of the SynCE project. It is a library of basic
functions used by the rest of the project.

%package -n %{develname}
Summary:	Basic library used by applications in the SynCE project
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Requires:	synce-core = %{version}-%{release}
Obsoletes:	%{mklibname synce 0 -d} < 0.13
Provides:	synce-core-devel

%description -n %{develname}
Libsynce is part of the SynCE project. It is a library of basic
functions used by the rest of the project.

%package -n     python-%{name}
Summary:        %{name} python package
Group:          System/Libraries

%description -n python-%{name}
The python-%{name} package.


%prep
%setup -q -n synce-core-%{version}

%build
export PATH=$PATH:/sbin/

%configure2_5x --enable-udev-support \
	       --disable-hal-support \
	       --enable-dccm-file-support \
	       --enable-odccm-support \
	       --enable-python-bindings \
	       --enable-bluetooth-support \
	       --disable-static
%make

%install
%makeinstall_std

rm -fr %{buildroot}%{_datadir}/doc

%files -n synce-core
%{_datadir}/synce-core/dhclient.conf
%{_datadir}/synce-core/udev-synce-*
%{_datadir}/synce-core/synceconnector.py
%{_datadir}//dbus-1/system-services/org.synce.dccm.service
%{_sysconfdir}/ppp/ip-up.d/synce-udev-bt-ipup
%{_sysconfdir}/ppp/peers/synce-bt-peer
%{_sysconfdir}/dbus-1/system.d/org.synce.dccm.conf
/lib/udev/rules.d/*.rules
/lib/udev/synce-udev-rndis
/lib/udev/synce-udev-serial
%{_bindir}/*
%{_mandir}/man1/*.xz
%{_libdir}/dccm
%{_libdir}/synce-serial-chat

%files -n python-%{name}
%{python_sitearch}/*.so

%files -n %{libname}
%{_libdir}/libsynce.so.%{major}*

%files -n %{develname}
%doc README TODO
%{_libdir}/libsynce.so
%{_includedir}/*.h
%{_libdir}/pkgconfig/libsynce.pc
%{_mandir}/man3/*3*
%{_mandir}/man7/*7*


%changelog
* Fri Jun 15 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.16-2
+ Revision: 805851
- BR: python-pyrex
- configure --enable-python-bindings
- BR: pkgconfig(pygobject-2.0)
- BR: python-devel
- missed build reqs
- package synce-core separated from libsynce
- naming policy
- version update 0.16
- version update 0.16

* Tue Mar 15 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.15.1-1
+ Revision: 645043
- new version 0.15.1
  enable udev support and disable hal support

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.15-2mdv2011.0
+ Revision: 609782
- rebuild

* Tue Apr 27 2010 Emmanuel Andry <eandry@mandriva.org> 0.15-1mdv2010.1
+ Revision: 539628
- New version 0.15

* Thu Mar 04 2010 Emmanuel Andry <eandry@mandriva.org> 0.15-0.r3893.1mdv2010.1
+ Revision: 514163
- pre 0.15 svn snapshot

* Wed Jul 22 2009 Frederik Himpe <fhimpe@mandriva.org> 0.14-1mdv2010.0
+ Revision: 398667
- Update to new version 0.14
- Remove underlinking fix: not needed anymore
- Remove provides and obsolets in main package, becaues the binary
  package with this name is not built anymore since years
- Don't let subpackages obsolete every previous version of themselves
  and don't use the package name in the version number of obsoleted packages

* Sun Jan 11 2009 Adam Williamson <awilliamson@mandriva.org> 0.13-1mdv2009.1
+ Revision: 328436
- do the underlink fix in Makefile.in and drop autopoo regeneration to try and
  fix weird build failure
- add underlink.patch: fix underlinking (against libm)
- new release 0.13

* Wed Jul 16 2008 Adam Williamson <awilliamson@mandriva.org> 0.12-1mdv2009.0
+ Revision: 236576
- new release 0.12

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Apr 16 2008 Adam Williamson <awilliamson@mandriva.org> 0.11.1-1mdv2009.0
+ Revision: 194471
- buildrequires hal-devel
- correct devel package group
- version all obsoletes / provides
- new devel policy
- clean spec
- new release 0.11.1

* Sat Feb 02 2008 Emmanuel Andry <eandry@mandriva.org> 0.11-3mdv2008.1
+ Revision: 161478
- obsoletes and provides synce

  + Thierry Vignaud <tv@mandriva.org>
    - fix description

* Thu Jan 10 2008 Emmanuel Andry <eandry@mandriva.org> 0.11-2mdv2008.1
+ Revision: 147443
- add more obsoletes

* Wed Jan 09 2008 Emmanuel Andry <eandry@mandriva.org> 0.11-1mdv2008.1
+ Revision: 147398
- import libsynce

