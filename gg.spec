Summary:	GNU Gadu - free talking
Summary(pl):	GNU Gadu - wolne gadanie
Name:		gg
Version:	0.1.pre6
Release:	2
License:	GPL
Group:          Applications/Communications
Group(de):      Applikationen/Kommunikation
Group(pl):      Aplikacje/Komunikacja
Source0:	http://netkrab.slackware.pl/gg/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Icon:		gg.xpm
URL:		http://netkrab.slackware.pl/gg/
BuildRequires:	gtk+-devel > 1.2.8
BuildRequires:	esound-devel > 0.2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Gadu-Gadu client released on GNU/GPL.

%description -l pl
Klient Gadu-Gadu na licencji GNU/GPL.

%prep
%setup  -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Network/Communications,%{_pixmapsdir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications/gg.desktop
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf README ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/gg
%{_datadir}/gg
%{_applnkdir}/Network/Communications/gg.desktop
%{_pixmapsdir}/*
