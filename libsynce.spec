%define major		0
%define libname		%mklibname synce %{major}
%define develname	%mklibname synce -d
%define svn 0

Summary:	Basic library used by applications in the SynCE project
Name:		libsynce
Version:	0.15.1
Release:	%mkrel 1
License:	MIT
Group:		System/Libraries
Source0:	http://prdownloads.sourceforge.net/synce/%{name}-%{version}.tar.gz
URL:		http://synce.sourceforge.net/
Buildroot:	%{_tmppath}/synce-root
BuildRequires:	dbus-glib-devel

%description
Libsynce is part of the SynCE project. It is a library of basic
functions used by the rest of the project.

%package -n %{libname}
Summary:	Basic library used by applications in the SynCE project
Group:		System/Libraries

%description -n %{libname}
Libsynce is part of the SynCE project. It is a library of basic
functions used by the rest of the project.

%package -n %{develname}
Summary:	Basic library used by applications in the SynCE project
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{mklibname synce 0 -d} < 0.13

%description -n %{develname}
Libsynce is part of the SynCE project. It is a library of basic
functions used by the rest of the project.

%prep
%setup -q

%build
%configure2_5x --enable-udev-support --disable-hal-support
%make

%install
%makeinstall

rm -fr %{buildroot}%{_datadir}/doc
rm -fr %{buildroot}%{_libdir}/*.la

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libsynce.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc README TODO
%{_libdir}/libsynce.so
%{_libdir}/libsynce.a
%{_includedir}/*.h
%{_libdir}/pkgconfig/libsynce.pc
%{_mandir}/man3/*3*
%{_mandir}/man7/*7*
