%define name	libsynce
%define release	%mkrel 1
%define version	0.11

%define shortname synce
%define major 0
%define libname %mklibname %shortname %major

Summary: SynCE: Basic library used by applications in the SynCE project
Name: %{name}
Version: %{version}
Release: %{release}
License: MIT
Group: System/Libraries
Source: %{name}-%{version}.tar.bz2
URL: http://synce.sourceforge.net/
Buildroot: %{_tmppath}/synce-root
Obsoletes: %{shortname}-%{name}

%description
Libsynce is part of the SynCE project:

  http://synce.sourceforge.net/

This library is required to compile (at least) the following parts of the
SynCE project:

%package -n %libname
Summary: SynCE: Basic library used by applications in the SynCE project
Group: System/Libraries
Provides: lib%shortname = %{version}-%{release}

%description -n %libname
Libsynce is part of the SynCE project:

  http://synce.sourceforge.net/

This library is required to compile (at least) the following parts of the
SynCE project.

%package -n %libname-devel
Summary: SynCE: Basic library used by applications in the SynCE project
Group: System/Libraries
Provides: lib%shortname-devel = %{version}-%{release}
Requires: %{libname} = %{version}-%{release}

%description -n %libname-devel
Libsynce is part of the SynCE project:

  http://synce.sourceforge.net/

This library is required to compile (at least) the following parts of the
SynCE project.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall

rm -fr %buildroot/%_datadir/doc

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files -n %libname
%defattr(-,root,root)
%doc README TODO
%{_libdir}/libsynce.so.%{major}
%{_libdir}/libsynce.so.%{major}.*

%files -n %libname-devel
%defattr(-,root,root)
%{_libdir}/libsynce.so
%{_libdir}/libsynce.a
%{_libdir}/libsynce.la
%{_includedir}/*.h
%{_libdir}/pkgconfig/libsynce.pc
%{_mandir}/man3/*3*
%{_mandir}/man7/*7*
