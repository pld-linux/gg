# Conditional build:
#
%bcond_without	gnome		# don't build with GNOME
%bcond_without	gnome_applet	# don't build GNOME applet
%bcond_without	kde		# don't build KDE applet
%bcond_without	wm_applet	# don't build WM applet
%bcond_without	sound		# disable sound support
#
# This looks like overkill but some day we might have *everything* bconded :)
%{?with_gnome:%define		need_gnome	1}
%{?with_gnome:%define 		need_esd	1}
%{?with_gnome_applet:%define	need_gnome	1}
%{?with_gnome_applet:%define 	nees_esd	1}
%{?with_kde:%define 		need_arts	1}
%{?with_wm_applet:%define 	need_esd	1}
#
Summary:	GNU Gadu - free talking
Summary(pl):	GNU Gadu - wolne gadanie
Name:		gg
Version:	1.0.0
Release:	3
Epoch:		5
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/ggadu/%{name}-%{version}.tar.gz
# Source0-md5:	7b32d4c866ef59dfe22373a83b1a9a2a
Source1:	%{name}.png
Source2:	%{name}_gnome.desktop
Source3:	%{name}_WM_applet.desktop
Source4:	%{name}_KDE.desktop
Patch0:		http://piorun.ds.pg.gda.pl/~blues/patches/gg-debian_fixes.patch
Icon:		gg.xpm
URL:		http://gadu.gnu.pl/
%{?need_arts:BuildRequires:	arts-devel}
%if %{with sound}
%{?need_esd:BuildRequires:	esound-devel > 0.2.7}
%endif
%{?need_gnome:BuildRequires:	gnome-libs-devel}
%{?need_gnome:BuildRequires:	gnome-core-devel}
BuildRequires:	gtk+-devel > 1.2.8
BuildRequires:	xmms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/GNOME
%define 	_prefix			/usr/X11R6

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
Klient Gadu-Gadu na licencji GNU/GPL. Wersja dokowalna dla GNOME.

%package wm-applet
Summary:	GNU Gadu - free talking - WindowMaker dockable version
Summary(pl):	GNU Gadu - wolne gadanie - wersja dokowalna dla WindowMaker'a
Group:		Applications/Communications
PreReq:		%{name}-common = %{epoch}:%{version}
Provides:	gg = %{epoch}:%{version}-%{release}

%description wm-applet
Gadu-Gadu client released on GNU/GPL. WindowMaker dockable version

%description wm-applet -l pl
Klient Gadu-Gadu na licencji GNU/GPL. Wersja dokowalna dla
WindowMaker'a.

%package kde
Summary:	GNU Gadu - free talking - KDE version
Summary(pl):	GNU Gadu - wolne gadanie - wersja dla KDE
Group:		Applications/Communications
PreReq:		%{name}-common = %{epoch}:%{version}
Provides:	gg = %{epoch}:%{version}-%{release}

%description kde
Gadu-Gadu client released on GNU/GPL. KDE version

%description kde -l pl
Klient Gadu-Gadu na licencji GNU/GPL. Wersja dla KDE.

%prep
%setup -q
%patch0 -p1

%build
LDFLAGS=" -L%{_libdir} %{rpmldflags}"

%if %{with gnome_applet}
%configure \
	%{!?with_sound:--disable-esd} \
	--enable-gnome \
	--enable-panel \
	--enable-xmms
%{__make}
mv -f src/gg src/gg_applet
%{__make} clean
%endif

%if %{with gnome}
%configure \
	%{!?with_sound:--disable-esd} \
	--enable-gnome \
	--enable-xmms
%{__make}
mv -f src/gg src/gg_gnome
%{__make} clean
%endif

%if %{with wm_applet}
%configure \
	%{!?with_sound:--disable-esd} \
	--enable-dockapp \
	--enable-xmms
%{__make}
mv -f src/gg src/gg_wm
%{__make} clean
%endif

%if %{with kde}
%configure \
	--enable-docklet \
	%{?with_sound:--enable-arts} \
	--disable-esd \
	--enable-xmms
%{__make}
mv -f src/gg src/gg_kde
%{__make} clean
%endif

%configure %{!?with_sound:--disable-esd} --enable-xmms
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Network/Communications,%{_datadir}/applets/Network} \
	$RPM_BUILD_ROOT{%{_sysconfdir}/CORBA/servers,%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{?with_gnome_applet:install src/gg_applet $RPM_BUILD_ROOT%{_bindir}}
%{?with_gnome:install src/gg_gnome $RPM_BUILD_ROOT%{_bindir}}
%{?with_wm_applet:install src/gg_wm $RPM_BUILD_ROOT%{_bindir}}
%{?with_kde:install src/gg_kde $RPM_BUILD_ROOT%{_bindir}}

sed -e 's/xpm$/png/' src/GnuGadu.desktop \
	> $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications/GnuGadu.desktop
sed -e 's/xpm$/png/' -e 's/Exec=gg/Exec=gg_applet\ --activate-goad-server=gg/' \
	src/GnuGadu.desktop > $RPM_BUILD_ROOT%{_datadir}/applets/Network/GnuGadu.desktop

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications/GnuGadu_gnome.desktop
install %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/applets/Network/GnuGadu_WM_applet.desktop
install %{SOURCE4} $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications/GnuGadu_KDE.desktop
install src/GnuGadu.gnorba $RPM_BUILD_ROOT%{_sysconfdir}/CORBA/servers/

%clean
rm -rf $RPM_BUILD_ROOT

%files common
%defattr(644,root,root,755)
%doc README ChangeLog TODO
%{_datadir}/gg
%{_pixmapsdir}/*

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gg
%{_applnkdir}/Network/Communications/GnuGadu.desktop

%if %{with gnome}
%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gg_gnome
%{_applnkdir}/Network/Communications/GnuGadu_gnome.desktop
%endif

%if %{with gnome_applet}
%files gnome-applet
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gg_applet
%{_datadir}/applets/Network/GnuGadu.desktop
%{_sysconfdir}/CORBA/servers/GnuGadu.gnorba
%endif

%if %{with wm_applet}
%files wm-applet
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gg_wm
%{_datadir}/applets/Network/GnuGadu_WM_applet.desktop
%endif

%if %{with kde}
%files kde
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gg_kde
%{_applnkdir}/Network/Communications/GnuGadu_KDE.desktop
%endif
