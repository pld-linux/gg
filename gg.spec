%define		_release	3

Summary:	GNU Gadu - free talking
Summary(pl):	GNU Gadu - wolne gadanie
Name:		gg
Version:	0.2.2.1
Release:	2
Epoch:		4
License:	GPL
Group:		Applications/Communications
Source0:	ftp://ftp.slackware.pl/gg/%{name}-%{version}.tar.gz
Source1:	%{name}.png
Patch0:		%{name}-home_etc.patch
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
Obsoletes:	gg =< 0.2.0

%description common
Gadu-Gadu client released on GNU/GPL.

%description common -l pl
Klient Gadu-Gadu na licencji GNU/GPL.

%package X11
Summary:	GNU Gadu - free talking
Summary(pl):	GNU Gadu - wolne gadanie
Group:		Applications/Communications
PreReq:		%{name}-common = %{epoch}:%{version}
Provides:	gg = %{epoch}:%{version}-%{release}

%description X11
Gadu-Gadu client released on GNU/GPL.

%description X11 -l pl
Klient Gadu-Gadu na licencji GNU/GPL. Wersja dla X11.

%package gnome
Summary:	GNU Gadu - free talking - GNOME version
Summary(pl):	GNU Gadu - wolne gadanie - wersja dla GNOME
Group:		Applications/Communications
PreReq:		%{name}-common = %{epoch}:%{version}
Provides:	gg = %{epoch}:%{version}-%{release}

%description gnome
Gadu-Gadu client released on GNU/GPL. GNOME version

%description gnome -l pl
Klient Gadu-Gadu na licencji GNU/GPL. Wersja dla GNOME.

%package gnome-applet
Summary:	GNU Gadu - free talking - GNOME dockable version
Summary(pl):	GNU Gadu - wolne gadanie - wersja dokowalna dla GNOME
Group:		Applications/Communications
PreReq:		%{name}-common = %{epoch}:%{version}
Provides:	gg = %{epoch}:%{version}-%{release}

%description gnome-applet
Gadu-Gadu client released on GNU/GPL. GNOME dockable version

%description gnome-applet -l pl
Klient Gadu-Gadu na licencji GNU/GPL. Wersja dokowalna dla gnome.

%package wm-applet
Summary:	GNU Gadu - free talking - WindowMaker dockable version.
Summary(pl):	GNU Gadu - wolne gadanie - wersja dokowalna dla WindowMaker'a.
Group:		Applications/Communications
PreReq:		%{name}-common = %{epoch}:%{version}
Provides:	gg = %{epoch}:%{version}-%{release}

%description wm-applet
Gadu-Gadu client released on GNU/GPL. WindowMaker dockable version

%description wm-applet -l pl
Klient Gadu-Gadu na licencji GNU/GPL. Wersja dokowalna dla
WindowMaker'a.

%package kde
Summary:	GNU Gadu - free talking - KDE version.
Summary(pl):	GNU Gadu - wolne gadanie - wersja dla KDE.
Group:		Applications/Communications
PreReq:		%{name}-common = %{epoch}:%{version}
Provides:	gg = %{epoch}:%{version}-%{release}

%description kde
Gadu-Gadu client released on GNU/GPL. KDE version

%description kde -l pl
Klient Gadu-Gadu na licencji GNU/GPL. Wersja dla KDE.

%prep
%setup -q -n %{name}-%{version}
#%patch0 -p1

%build
LDFLAGS=" -L%{_libdir} %{rpmldflags}"
%configure \
	--enable-gnome \
	--enable-panel
%{__make}
mv -f src/gg src/gg_applet
%{__make} clean

%configure \
	--enable-gnome
%{__make}
mv -f src/gg src/gg_gnome
%{__make} clean

%configure \
	--enable-dockapp
%{__make}
mv -f src/gg src/gg_wm
%{__make} clean

%configure \
	--enable-docklet
%{__make}
mv -f src/gg src/gg_kde
%{__make} clean

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Network/Communications,%{_pixmapsdir},%{_datadir}/applets/Network/}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install src/gg_applet $RPM_BUILD_ROOT%{_bindir}
install src/gg_gnome $RPM_BUILD_ROOT%{_bindir}
install src/gg_wm $RPM_BUILD_ROOT%{_bindir}
install src/gg_kde $RPM_BUILD_ROOT%{_bindir}

sed -e 's/xpm$/png/' src/GnuGadu.desktop \
	> $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications/GnuGadu.desktop
sed -e 's/xpm$/png/' -e 's/Exec=gg/Exec=gg_applet\ --activate-goad-server=gg/' \
	src/GnuGadu.desktop > $RPM_BUILD_ROOT%{_datadir}/applets/Network/GnuGadu.desktop

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf README ChangeLog TODO
install -d $RPM_BUILD_ROOT%{_sysconfdir}/CORBA/servers/
install src/GnuGadu.gnorba $RPM_BUILD_ROOT%{_sysconfdir}/CORBA/servers/

%clean
rm -rf $RPM_BUILD_ROOT

%post gnome
if [ ! -e /usr/X11R6/bin/gg ]; then
	ln -sf /usr/X11R6/bin/gg_gnome /usr/X11R6/bin/gg
fi

%post gnome-applet
if [ ! -e /usr/X11R6/bin/gg ]; then
	ln -sf /usr/X11R6/bin/gg_applet /usr/X11R6/bin/gg
fi

%post wm-applet
if [ ! -e /usr/X11R6/bin/gg ]; then
	ln -sf /usr/X11R6/bin/gg_wm /usr/X11R6/bin/gg
fi

%post kde
if [ ! -e /usr/X11R6/bin/gg ]; then
	ln -sf /usr/X11R6/bin/gg_kde /usr/X11R6/bin/gg
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

%files wm-applet
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gg_wm
%attr(755,root,root) %{_datadir}/applets/Network/GnuGadu.desktop

%files kde
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gg_kde
%attr(755,root,root) %{_datadir}/applets/Network/GnuGadu.desktop
