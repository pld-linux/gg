#
# Conditional build:
#
# _without_gnome
# _without_gnome_applet
# _without_kde
# _without_wm_applet
# _without_sound

%define snapshot 20020612

# This looks like overkill but some day we might have *everything* bconded :)
%{!?_without_gnome: 		%define _need_gnome	1}
%{!?_without_gnome:         %define _need_esd   1}
%{!?_without_gnome_applet:	%define	_need_gnome	1}
%{!?_without_gnome_applet:  %define _nees_esd   1}
%{!?_without_kde:			%define _need_arts	1}
%{!?_without_wm_applet:		%define _need_esd	1}


Summary:	GNU Gadu - free talking
Summary(pl):	GNU Gadu - wolne gadanie
Name:		gg
Version:	0.2.3
Release:	0.1pre%{snapshot}
Epoch:		4
License:	GPL
Group:		Applications/Communications
Source0:	ftp://ftp.slackware.pl/gg/snapshots/%{name}-%{snapshot}.tar.gz
Source1:	%{name}.png
Patch0:		%{name}-ac_fix.patch
Icon:		gg.xpm
URL:		http://netkrab.slackware.pl/gg/
BuildRequires:					gtk+-devel > 1.2.8
%{?_need_gnome:BuildRequires:	gnome-libs-devel}
%{?_need_gnome:BuildRequires:	gnome-core-devel}
%if %{!?_without_sound:1}%{?_without_sound:0}
%{?_need_arts:BuildRequires:	arts-devel}
%{?_need_esd:BuildRequires:		esound-devel > 0.2.7}
%endif

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
%setup -q -n %{name}-%{snapshot}
%patch0 -p0

%build
LDFLAGS=" -L%{_libdir} %{rpmldflags}"

aclocal -I macros
autoconf
automake -a -c -f

%if %{!?_without_gnome_applet:1}%{?_without_gnome_applet:0}
%configure \
	%{?_without_sound:--disable-esd} \
	--enable-gnome \
	--enable-panel
%{__make}
mv -f src/gg src/gg_applet
%{__make} clean
%endif

%if %{!?_without_gnome:1}%{?_without_gnome:0}
%configure \
	%{?_without_sound:--disable-esd} \
	--enable-gnome
%{__make}
mv -f src/gg src/gg_gnome
%{__make} clean
%endif

%if %{!?_without_wm_applet:1}%{?_without_wm_applet:0}
%configure \
	%{?_without_sound:--disable-esd} \
	--enable-dockapp
%{__make}
mv -f src/gg src/gg_wm
%{__make} clean
%endif

%if %{!?_without_kde:1}%{?_without_kde:0}
%configure \
	--enable-docklet \
	%{!?_without_sound:--enable-arts} \
	--disable-esd
%{__make}
mv -f src/gg src/gg_kde
%{__make} clean
%endif

%configure %{?_without_sound:--disable-esd}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Network/Communications,%{_pixmapsdir},%{_datadir}/applets/Network/}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
%{!?_without_gnome_applet:install src/gg_applet $RPM_BUILD_ROOT%{_bindir}}
%{!?_without_gnome:install src/gg_gnome $RPM_BUILD_ROOT%{_bindir}}
%{!?_without_wm_applet:install src/gg_wm $RPM_BUILD_ROOT%{_bindir}}
%{!?_without_kde:install src/gg_kde $RPM_BUILD_ROOT%{_bindir}}

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

%if %{!?_without_gnome:1}%{?_without_gnome:0}
%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gg_gnome
%{_applnkdir}/Network/Communications/GnuGadu.desktop
%endif

%if %{!?_without_gnome_applet:1}%{?_without_gnome_applet:0}
%files gnome-applet
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gg_applet
%attr(755,root,root) %{_datadir}/applets/Network/GnuGadu.desktop
%attr(755,root,root) %{_sysconfdir}/CORBA/servers/GnuGadu.gnorba
%endif

%if %{!?_without_wm_applet:1}%{?_without_wm_applet:0}
%files wm-applet
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gg_wm
%attr(755,root,root) %{_datadir}/applets/Network/GnuGadu.desktop
%endif

%if %{!?_without_kde:1}%{?_without_kde:0}
%files kde
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gg_kde
%attr(755,root,root) %{_datadir}/applets/Network/GnuGadu.desktop
%endif
