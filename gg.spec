Summary:	GNU Gadu - free talking
Summary(pl):	GNU Gadu - wolne gadanie
Name:		gg
Version:	0.2.0
Release:	3
Epoch:		4
License:	GPL
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Source0:	http://netkrab.slackware.pl/gg/%{name}-%{version}.tar.gz
Source2:	%{name}.png
Icon:		gg.xpm
URL:		http://netkrab.slackware.pl/gg/
BuildRequires:	gtk+-devel > 1.2.8
BuildRequires:	esound-devel > 0.2.7
BuildRequires:	gnome-libs-devel 
BuildRequires:	gnome-core-devel 
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Gadu-Gadu client released on GNU/GPL.

%description -l pl
Klient Gadu-Gadu na licencji GNU/GPL.

%package common
Summary:	GNU Gadu - free talking - common files
Summary(pl):	GNU Gadu - wolne gadanie - wspólne pliki
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Obsoletes:	gg < 0.2.0


%description common
Gadu-Gadu client released on GNU/GPL.

%description -l pl common
Klient Gadu-Gadu na licencji GNU/GPL.

%package X11
Summary:	GNU Gadu - free talking - gnome dockable
Summary(pl):	GNU Gadu - wolne gadanie - wersja dokowalna dla gnome
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Prereq:		%{name}-common = %{epoch}:%{version}
Provides:	gg = %{epoch}:%{version}-%{release}

%description X11
Gadu-Gadu client released on GNU/GPL. 

%description -l pl X11
Klient Gadu-Gadu na licencji GNU/GPL. Wersja dla X11.

%package gnome
Summary:	GNU Gadu - free talking - gnome dockable
Summary(pl):	GNU Gadu - wolne gadanie - wersja dokowalna dla gnome
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Prereq:		%{name}-common = %{epoch}:%{version}
Provides:	gg = %{epoch}:%{version}-%{release}

%description X11
Gadu-Gadu client released on GNU/GPL. Gnome dockable version

%description -l pl gnome
Klient Gadu-Gadu na licencji GNU/GPL. Wersja dokowalna dla gnome.

%prep
%setup  -q

%build
LDFLAGS=" -L%{_libdir} %{rpmldflags}"
%configure \
	--enable-gnome \
	--enable-panel
%{__make}
mv src/gg src/gnu_gadu_applet
%{__make} clean

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Network/Communications,%{_pixmapsdir},%{_datadir}/applets/Network/}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install src/gnu_gadu_applet $RPM_BUILD_ROOT%{_bindir}

cp -f src/GnuGadu.desktop $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications/
cat src/GnuGadu.desktop | sed -e 's/Exec=gg/Exec=gnu_gadu_applet/' > $RPM_BUILD_ROOT%{_datadir}/applets/Network/GnuGadu.desktop

install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf README ChangeLog TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files common
%defattr(644,root,root,755)
%doc *.gz
%{_datadir}/gg
%{_pixmapsdir}/*

%files X11
%defattr(644,root,root,755)
%{_applnkdir}/Network/Communications/GnuGadu.desktop
%attr(755,root,root) %{_bindir}/gg

%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnu_gadu_applet
%attr(755,root,root) %{_datadir}/applets/Network/GnuGadu.desktop
