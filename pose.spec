Summary:	palm emulator
Summary(pl):	palm emulator
Name:		pose
Version:	3.5
Release:	0.1
License:	GPL
Group:		Emulators
Source0:	http://www.palmos.com/dev/tools/emulator/sources/emulator_src_%{version}.tar.gz
URL:		http://www.palmos.com/dev/tools/emulator/
Patch0:		%{name}-conf.patch
BuildRequires:	fltk-devel
BuildRequires:	glut-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%prep
%setup -q -n Emulator_Src_%{version}
%patch -p1

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
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
