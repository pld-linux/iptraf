Summary:	IPTraf is a console-based network monitoring program
Summary(pl):	IPTraf s³u¿y do monitorowania sieci.
Name:		iptraf
Version:	1.3.0
Release:	2d
#######		ftp://ftp.cebu.mozcom.com/pub/linux/net/
Source:		%{name}-%{version}.tar.gz
Patch:		%{name}-pld.patch
URL:		http://cebu.mozcom.com/riker/iptraf/
Copyright:	GPL
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

install -d $RPM_BUILD_ROOT/usr/{sbin,man/man8}
install -d $RPM_BUILD_ROOT/{var/{log/iptraf,lib/iptraf}}
install -s src/iptraf $RPM_BUILD_ROOT/usr/sbin
install -s src/cfconv $RPM_BUILD_ROOT/usr/sbin
install -s src/rvnamed $RPM_BUILD_ROOT/usr/sbin

install Documentation/iptraf.8 $RPM_BUILD_ROOT/usr/man/man8
install Documentation/rvnamed.8 $RPM_BUILD_ROOT/usr/man/man8

bzip2 -9  Documentation/*txt README.* CHANGES WHATELSE
gzip -9fn $RPM_BUILD_ROOT/usr/man/man8/*.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Documentation/*txt.bz2 README.* {CHANGES,WHATELSE}.bz2

%attr(755,root,root) /usr/sbin/*
%attr(644,root, man) /usr/man/man8/*
%attr(750,root,root) %dir /var/lib/iptraf
%attr(750,root,root) %dir /var/log/iptraf

%changelog
* Wed Oct 7 1998 Bartek Rozkrut <madey@dione.ids.pl>
  [1.3.0-1d]
- First relase as a PLD Tornado package.
