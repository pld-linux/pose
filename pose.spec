Summary:	Palm OS emulator
Summary(pl.UTF-8):	Emulator Palm OS
Name:		pose
Version:	3.5
Release:	1
License:	GPL
Group:		Applications/Emulators
#Source0Download: http://www.palmos.com/dev/tools/emulator/
Source0:	http://www.palmos.com/dev/tools/emulator/sources/emulator_src_%{version}.tar.gz
# Source0-md5:	c69b10798e524b999739bf1950125655
Patch0:		%{name}-conf.patch
Patch1:		%{name}-dirs.patch
Patch2:		%{name}-fltk10compat.patch
Patch3:		%{name}-gcc34.patch
Patch4:		%{name}-3.5-relax-opt.patch
URL:		http://www.palmos.com/dev/tools/emulator/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fltk-gl-devel
BuildRequires:	glut-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Palm OS Emulator is an application that emulates the hardware for most
Palm Computing Platform Hardware devices (e.g., Pilot, PalmPilot, Palm
III, Palm V, Palm VII, etc.). With the Palm OS Emulator, you can
emulate the functions of a Palm hardware device, including running the
built-in application, as well as installing and running 3rd party
applications.

%description -l pl.UTF-8
Palm OS Emulator to aplikacja emulująca sprzęt większości urządzeń
platformy Palm Computing (np. Pilot, PalmPilot, Palm III, Palm V, Palm
VII itp.). Przy użyciu tego emulatora można emulować funkcje urządzeń
Palm włącznie z wbudowanymi aplikacjami, a także instalować i
uruchamiać dowolne aplikacje firm trzecich.

%prep
%setup -q -n Emulator_Src_%{version}
%patch -P0 -p1
%patch -P1 -p0
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1

%build
cd BuildUnix
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-fltk=/usr/include/FL/
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

cd BuildUnix
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/%{name} 
cd ..
install  ROMTransfer/Source/ROM_Transfer.prc $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Docs/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
