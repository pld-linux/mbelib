Summary:	P25 Phase 1 and ProVoice vocoder
Name:		mbelib
Version:	1.2.5
Release:	1
License:	BSD
Group:		Applications/System
Source0:	https://github.com/szechyjs/mbelib/archive/v%{version}.tar.gz
# Source0-md5:	6a609b494a4dfff281a4a6605a3b406f
URL:		https://github.com/szechyjs/mbelib
BuildRequires:	cmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mbelib supports the 7200x4400 bit/s codec used in P25 Phase 1, the
7100x4400 bit/s codec used in ProVoice and the "Half Rate" 3600x2250
bit/s vocoder used in various radio systems.

%package devel
Summary:	Header files and development documentation for mbelib
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files and development documentation for mbelib.

%package static
Summary:	Static mbelib library
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static mbelib library.

%prep
%setup -q

%build
install -d build
cd build
%{cmake} ..

%install
rm -rf $RPM_BUILD_ROOT

# fix this using some better way
sed -i -e 's#/lib"#/%{_lib}"#g' -e 's#/lib/#/%{_lib}/#g' build/cmake_install.cmake

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG README.md
%attr(755,root,root) %{_libdir}/libmbe.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libmbe.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmbe.so
%{_includedir}/mbelib.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libmbe.a
