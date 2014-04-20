Summary:	Internet Backplane Protocol libraries
Summary(pl.UTF-8):	Biblioteki protokołu Internet Backplane Protocol
Name:		ibp
Version:	1.4.0.6
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: http://loci.cs.utk.edu/downloads/
Source0:	http://loci.cs.utk.edu/lors/distributions/%{name}-%{version}.tar.gz
# Source0-md5:	b4fd7859f50b35b5404b3ee6f4eddad7
Patch0:		%{name}-fhs.patch
Patch1:		%{name}-link.patch
URL:		http://loci.cs.utk.edu/ibp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Internet Backplane Protocol (IBP) is middleware for managing and
using remote storage. It was invented to support Logistical Networking
in large scale, distributed systems and applications.

%description -l pl.UTF-8
Protokół IBP (Internet Backplane Protocol) to warstwa pośrednia do
zarządzania i wykorzystywania zdalnych składowisk danych. Powstał w
celu obsługi sieci logistycznych na wielką skalę oraz systemów i
aplikacji rozproszonych.

%package devel
Summary:	Header files for IBP libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek IBP
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for IBP libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek IBP.

%package static
Summary:	Static IBP libraries
Summary(pl.UTF-8):	Statyczne biblioteki IBP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static IBP libraries.

%description static -l pl.UTF-8
Statyczne biblioteki IBP.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README doc/{IBP_NFU.pdf,ibpservercfg.pdf}
%attr(755,root,root) %{_bindir}/DM
%attr(755,root,root) %{_bindir}/blaster
%attr(755,root,root) %{_bindir}/blasterd
%attr(755,root,root) %{_bindir}/clientMCAST
%attr(755,root,root) %{_bindir}/clientTCP
%attr(755,root,root) %{_bindir}/ibp-dmtest
%attr(755,root,root) %{_bindir}/ibp-slm
%attr(755,root,root) %{_bindir}/ibp-test
%attr(755,root,root) %{_bindir}/ibp_server_mt
%attr(755,root,root) %{_bindir}/ibpd-%{version}
%attr(755,root,root) %{_bindir}/ibpd
%attr(755,root,root) %{_bindir}/makefs
%attr(755,root,root) %{_bindir}/mclientTCP
%attr(755,root,root) %{_bindir}/pmclientTCP
%attr(755,root,root) %{_bindir}/readfat
%attr(755,root,root) %{_bindir}/serverMCAST
%attr(755,root,root) %{_bindir}/serverTCP
%attr(755,root,root) %{_bindir}/smclientTCP
%attr(755,root,root) %{_bindir}/tblaster
%attr(755,root,root) %{_bindir}/tservMCAST
%attr(755,root,root) %{_libdir}/libibp-%{version}.so
%attr(755,root,root) %{_libdir}/libmdns.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmdns.so.0
%attr(755,root,root) %{_libdir}/libnfuops.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnfuops.so.0
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ibp.cfg
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/nfu.cfg

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libibp.so
%attr(755,root,root) %{_libdir}/libmdns.so
%attr(755,root,root) %{_libdir}/libnfuops.so
%{_libdir}/libibp.la
%{_libdir}/libmdns.la
%{_libdir}/libnfuops.la
%{_includedir}/ibp
%{_includedir}/ibp.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libibp.a
%{_libdir}/libmdns.a
%{_libdir}/libnfuops.a
