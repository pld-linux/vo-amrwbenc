Summary:	VisualOn AMR-WB encoder library
Summary(pl.UTF-8):	Biblioteka kodera VisualOn AMR-WB
Name:		vo-amrwbenc
Version:	0.1.2
Release:	2
License:	Apache v2.0
Group:		Libraries
Source0:	http://downloads.sourceforge.net/opencore-amr/%{name}-%{version}.tar.gz
# Source0-md5:	588205f686adc23532e31fe3646ddcb6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library contains an encoder implementation of the Adaptive Multi
Rate Wideband (AMR-WB) audio codec. The library is based on a codec
implementation by VisualOn as part of the Stagefright framework from
the Google Android project.

%description -l pl.UTF-8
Ta biblioteka zawiera implementację kodera kodeka dźwięku AMR-WB
(Adaptive Multi Rate Wideband). Jest opaera na implementacji kodeka
firmy VisualOn jako części środowiska Stagefright z projektu Google
Android.

%package devel
Summary:	Header files for VisualOn AMR-WB encoder library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki kodera VisualOn AMR-WB
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for VisualOn AMR-WB encoder library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki kodera VisualOn AMR-WB.

%package static
Summary:	Static VisualOn AMR-WB encoder library
Summary(pl.UTF-8):	Statyczna biblioteka kodera VisualOn AMR-WB
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static VisualOn AMR-WB encoder library.

%description static -l pl.UTF-8
Statyczna biblioteka kodera VisualOn AMR-WB.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no dependencies and pkg-config file present
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libvo-amrwbenc.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NOTICE README
%attr(755,root,root) %{_libdir}/libvo-amrwbenc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvo-amrwbenc.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvo-amrwbenc.so
%{_includedir}/vo-amrwbenc
%{_pkgconfigdir}/vo-amrwbenc.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libvo-amrwbenc.a
