Summary:	IPTraf is a console-based network monitoring program
Summary(pl):	IPTraf s³u¿y do monitorowania sieci.
Name:		iptraf
Version:	1.3.0
Release:	3
Copyright:	GPL
URL:		http://cebu.mozcom.com/riker/iptraf/
Source:		ftp://ftp.cebu.mozcom.com/pub/linux/net/%{name}-%{version}.tar.gz
Patch:		%{name}-pld.patch
Group:		Networking
Group(pl):	Sieciowe
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
make clean; make OPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}
install -d $RPM_BUILD_ROOT/var/{log/iptraf,state/iptraf}

install -s src/iptraf $RPM_BUILD_ROOT%{_sbindir}
install -s src/cfconv $RPM_BUILD_ROOT%{_sbindir}
install -s src/rvnamed $RPM_BUILD_ROOT%{_sbindir}

install Documentation/iptraf.8 $RPM_BUILD_ROOT%{_mandir}/man8
install Documentation/rvnamed.8 $RPM_BUILD_ROOT%{_mandir}/man8

gzip -9nf Documentation/*txt README.* CHANGES WHATELSE
gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man8/*.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Documentation/*txt,README.*,CHANGES,WHATELSE}.gz

%attr(755,root,root) %{_sbindir}/*
%attr(750,root,root) %dir /var/state/iptraf
%attr(750,root,root) %dir /var/log/iptraf
%{_mandir}/man8/*
