Summary:	GNU Gadu - wolne gadanie
Summary(pl):	GNU Gadu - wolne gadanie
Name:		gg
Version:	0.1.pre5
Release:	1
License:	GPL
Group:          Applications/Communications
Group(de):      Applikationen/Kommunikation
Group(pl):      Aplikacje/Komunikacja
Source0:	http://netkrab.slackware.pl/gg/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.xpm
Icon:		gg.xpm
URL:		http://netkrab.slackware.pl/gg/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Klient Gadu-Gadu na licencji GNU/GPL.

%description -l pl
Klient Gadu-Gadu na licencji GNU/GPL.

%prep
%setup  -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications/gg.desktop

gzip -9nf README ChangeLog

%clean
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gg
%{_datadir}/gg/pixmaps/*
%{_applnkdir}/Network/Communications/gg.desktop
