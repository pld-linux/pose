Summary:	Palm OS emulator
Summary(pl):	Emulator Palm OS
Name:		pose
Version:	3.5
Release:	0.2
License:	GPL
Group:		Emulators
#Source0Download: http://www.palmos.com/dev/tools/emulator/
Source0:	http://www.palmos.com/dev/tools/emulator/sources/emulator_src_%{version}.tar.gz
# Source0-md5:	c69b10798e524b999739bf1950125655
Patch0:		%{name}-conf.patch
Patch1:		%{name}-dirs.patch
Patch2:		%{name}-fltk10compat.patch
URL:		http://www.palmos.com/dev/tools/emulator/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fltk-devel
BuildRequires:	glut-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Palm OS Emulator is an application that emulates the hardware for most
Palm Computing Platform Hardware devices (e.g., Pilot, PalmPilot, Palm
III, Palm V, Palm VII, etc.). With the Palm OS Emulator, you can
emulate the functions of a Palm hardware device, including running the
built-in application, as well as installing and running 3rd party
applications.

%description -l pl
Palm OS Emulator to aplikacja emuluj�ca sprz�t wi�kszo�ci urz�dze�
platformy Palm Computing (np. Pilot, PalmPilot, Palm III, Palm V, Palm
VII itp.). Przy u�yciu tego emulatora mo�na emulowa� funkcje urz�dze�
Palm w��cznie z wbudowanymi aplikacjami, a tak�e instalowa� i
uruchamia� dowolne aplikacje firm trzecich.

%prep
%setup -q -n Emulator_Src_%{version}
%patch0 -p1
%patch1 -p0
%patch2 -p1

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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
