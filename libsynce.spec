%define major		0
%define libname		%mklibname synce %{major}
%define develname	%mklibname synce -d
%define svn 0
%rename	synce-core

Summary:	Basic library used by applications in the SynCE project
#Name:		synce-core
Name:		libsynce
Version:	0.16
Release:	1
License:	MIT
Group:		System/Libraries
Source0:	http://downloads.sourceforge.net/project/synce/SynCE/synce-core/synce-core-%{version}.tar.gz
URL:		http://synce.sourceforge.net/
BuildRequires:	dbus-glib-devel
BuildRequires:	dhcp-client


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
	       --enable-bluetooth-support \
	       --disable-static
%make

%install
%makeinstall_std

rm -fr %{buildroot}%{_datadir}/doc

%files
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
