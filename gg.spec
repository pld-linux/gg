Summary:	GNU Gadu - free talking
Summary(pl):	GNU Gadu - wolne gadanie
Name:		gg
Version:	0.2.0
Release:	2
Epoch:		4
License:	GPL
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Source0:	http://netkrab.slackware.pl/gg/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-writecontact.patch
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

%package gnome
Summary:	GNU Gadu - free talking - gnome dockable
Summary(pl):	GNU Gadu - wolne gadanie - wersja dokowalna dla gnome
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja

%description gnome
Gadu-Gadu client released on GNU/GPL. Gnome dockable version

%description -l pl gnome
Klient Gadu-Gadu na licencji GNU/GPL. Wersja dokowalna dla gnome.

%prep
%setup  -q
%patch0 -p1

%build
LDFLAGS=" -L%{_libdir} "
%configure --enable-gnome --enable-panel
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

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications/gg.desktop
cat %{SOURCE1} | sed -e 's/Exec=gg/Exec=gnu_gadu_applet/' > $RPM_BUILD_ROOT%{_datadir}/applets/Network/gnu_gadu_applet.desktop

install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf README ChangeLog TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/gg
%{_datadir}/gg
%{_applnkdir}/Network/Communications/gg.desktop
%{_pixmapsdir}/*

%files gnome
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/gnu_gadu_applet
%{_datadir}/gg
%{_datadir}/applets/Network/gnu_gadu_applet.desktop
%{_pixmapsdir}/*
