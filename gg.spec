Summary:	GNU Gadu - free talking
Summary(pl):	GNU Gadu - wolne gadanie
Name:		gg
Version:	0.2.1
Release:	2
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
%define		_sysconfdir	/etc/X11/GNOME

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
Obsoletes:	gg =< 0.2.0


%description common
Gadu-Gadu client released on GNU/GPL.

%description -l pl common
Klient Gadu-Gadu na licencji GNU/GPL.

%package X11
Summary:	GNU Gadu - free talking 
Summary(pl):	GNU Gadu - wolne gadanie 
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
Summary:	GNU Gadu - free talking - GNOME version
Summary(pl):	GNU Gadu - wolne gadanie - wersja dla GNOME
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Prereq:		%{name}-common = %{epoch}:%{version}
Provides:	gg = %{epoch}:%{version}-%{release}

%description gnome
Gadu-Gadu client released on GNU/GPL. GNOME version

%description -l pl gnome
Klient Gadu-Gadu na licencji GNU/GPL. Wersja dla GNOME.

%package gnome-applet
Summary:	GNU Gadu - free talking - GNOME dockable version
Summary(pl):	GNU Gadu - wolne gadanie - wersja dokowalna dla GNOME
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Prereq:		%{name}-common = %{epoch}:%{version}
Provides:	gg = %{epoch}:%{version}-%{release}

%description gnome-applet
Gadu-Gadu client released on GNU/GPL. GNOME dockable version

%description -l pl gnome-applet
Klient Gadu-Gadu na licencji GNU/GPL. Wersja dokowalna dla gnome.

%prep
%setup  -q -n %{name}-%{version}

%build
LDFLAGS=" -L%{_libdir} %{rpmldflags}"
%configure \
	--enable-gnome \
	--enable-panel
%{__make}
mv src/gg src/gg_applet
%{__make} clean

%configure \
	--enable-gnome 
%{__make}
mv src/gg src/gg_gnome
%{__make} clean

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Network/Communications,%{_pixmapsdir},%{_datadir}/applets/Network/}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install src/gg_applet $RPM_BUILD_ROOT%{_bindir}
install src/gg_gnome $RPM_BUILD_ROOT%{_bindir}

cat src/GnuGadu.desktop | sed -e 's/xpm$/png/' > $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications/GnuGadu.desktop
cat src/GnuGadu.desktop | sed -e 's/xpm$/png/' | sed -e 's/Exec=gg/Exec=gg_applet\ --activate-goad-server=gg/' > $RPM_BUILD_ROOT%{_datadir}/applets/Network/GnuGadu.desktop

install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf README ChangeLog TODO

%clean
#rm -rf $RPM_BUILD_ROOT

%post gnome
if [ ! -e /usr/X11R6/bin/gg ]; then
      ln -s /usr/X11R6/bin/gg_gnome /usr/X11R6/bin/gg
fi

%post gnome-applet
if [ ! -e /usr/X11R6/bin/gg ]; then
      ln -s /usr/X11R6/bin/gg_applet /usr/X11R6/bin/gg
fi


%postun
if [ -L /usr/X11R6/bin/gg ]; then
      rm -f /usr/X11R6/bin/gg
fi


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
%attr(755,root,root) %{_bindir}/gg_gnome
%{_applnkdir}/Network/Communications/GnuGadu.desktop

%files gnome-applet
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gg_applet
%attr(755,root,root) %{_datadir}/applets/Network/GnuGadu.desktop
%attr(755,root,root) %{_sysconfdir}/CORBA/servers/GnuGadu.gnorba
