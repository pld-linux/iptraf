Summary:	IPTraf is a console-based network monitoring program
Summary(pl):	IPTraf s³u¿y do monitorowania sieci.
Name:		iptraf
Version:	2.1.1
Release:	1
Copyright:	GPL
Group:		Networking
Group(pl):	Sieciowe
Source:		ftp://ftp.cebu.mozcom.com/pub/linux/net/%{name}-%{version}.tar.gz
Patch:		iptraf.patch
URL:		http://cebu.mozcom.com/riker/iptraf/
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	ncurses-ext
Buildroot:	/tmp/%{name}-%{version}-root

%description
IPTraf is a console-based network monitoring program that displays information
about IP traffic. This program can be used to determine the type of traffic on
your network, and what kind of service is the most heavily used on what
machines, among others.
IPTraf works on Ethernet and SLIP/PPP interfaces.

%description -l pl
IPTraf jest narzêdziem s³u¿±cym do monitorowania sieci. Posiada kolorowy,
prosty w obs³udze interfejs. Wspó³pracuje z wieloma protoko³ami sieciowymi.
Obs³uguje standardy : Ethernet i PPP/SLIP.

%prep
%setup -q
%patch -p1

%build
cd src
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}
install -d $RPM_BUILD_ROOT/var/{log/iptraf,state/iptraf}

install -s src/iptraf $RPM_BUILD_ROOT%{_sbindir}
install -s src/cfconv $RPM_BUILD_ROOT%{_sbindir}
install -s src/rvnamed $RPM_BUILD_ROOT%{_sbindir}

install Documentation/iptraf.8 $RPM_BUILD_ROOT%{_mandir}/man8
install Documentation/rvnamed.8 $RPM_BUILD_ROOT%{_mandir}/man8

gzip -9nf README* CHANGES \
	$RPM_BUILD_ROOT%{_mandir}/man8/*.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README*,CHANGES}.gz
%doc Documentation/*.{gif,html}
%attr(755,root,root) %{_sbindir}/*
%attr(750,root,root) %dir /var/state/iptraf
%attr(750,root,root) %dir /var/log/iptraf
%{_mandir}/man8/*
