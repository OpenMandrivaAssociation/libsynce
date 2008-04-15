%define shortname	synce

%define major		0
%define libname		%mklibname %{shortname} %{major}
%define develname	%mklibname %{shortname} -d

Summary:	Basic library used by applications in the SynCE project
Name:		libsynce
Version:	0.11.1
Release:	%{mkrel 1}
License:	MIT
Group:		System/Libraries
Source:		http://prdownloads.sourceforge.net/%{shortname}/%{name}-%{version}.tar.gz
URL:		http://synce.sourceforge.net/
Buildroot:	%{_tmppath}/synce-root
BuildRequires:	dbus-glib-devel
BuildRequires:	hal-devel
Obsoletes:	%{shortname}-%{name} < %{version}-%{release}
Obsoletes:	%{shortname} < %{version}-%{release}
Provides:	%{shortname} = %{version}-%{release}

%description
Libsynce is part of the SynCE project. It is a library of basic
functions used by the rest of the project.

%package -n %{libname}
Summary:	Basic library used by applications in the SynCE project
Group:		System/Libraries
Obsoletes:	%{libname} < %{libname}-%{version}

%description -n %{libname}
Libsynce is part of the SynCE project. It is a library of basic
functions used by the rest of the project.

%package -n %{develname}
Summary:	Basic library used by applications in the SynCE project
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{libname}-devel < %{libname}-devel-%{version}
Obsoletes:	%{mklibname synce 0 -d} < %{version}-%{release}

%description -n %{develname}
Libsynce is part of the SynCE project. It is a library of basic
functions used by the rest of the project.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall

rm -fr %{buildroot}%{_datadir}/doc

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libsynce.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc README TODO
%{_libdir}/libsynce.so
%{_libdir}/libsynce.a
%{_libdir}/libsynce.la
%{_includedir}/*.h
%{_libdir}/pkgconfig/libsynce.pc
%{_mandir}/man3/*3*
%{_mandir}/man7/*7*

