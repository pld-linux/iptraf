Summary:	IPTraf is a console-based network monitoring program
Summary(pl):	IPTraf s³u¿y do monitorowania sieci
Name:		iptraf
Version:	2.2.0
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narzêdzia
Source0:	ftp://ftp.cebu.mozcom.com/pub/linux/net/%{name}-%{version}.tar.gz
Patch0:		iptraf.patch
Icon:		iptraf.gif
URL:		http://cebu.mozcom.com/riker/iptraf/
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	ncurses-ext
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IPTraf is a console-based network monitoring utility. IPTraf gathers
data like TCP connection packet and byte counts, interface statistics
and activity indicators, TCP/UDP traffic breakdowns, and LAN station
packet and byte counts. IPTraf features include an IP traffic monitor
which shows TCP flag information, packet and byte counts, ICMP
details, OSPF packet types, and oversized IP packet warnings;
interface statistics showing IP, TCP, UDP, ICMP, non-IP and other IP
packet counts, IP checksum errors, interface activity and packet size
counts; a TCP and UDP service monitor showing counts of incoming and
outgoing packets for common TCP and UDP application ports, a LAN
statistics module that discovers active hosts and displays statistics
about their activity; TCP, UDP and other protocol display filters so
you can view just the traffic you want; logging; support for Ethernet,
FDDI, ISDN, SLIP, PPP, and loopback interfaces; and utilization of the
built-in raw socket interface of the Linux kernel, so it can be used
on a wide variety of supported network cards.

%description -l pl
IPTraf jest narzêdziem s³u¿±cym do monitorowania sieci. Posiada
kolorowy, prosty w obs³udze interfejs. Wspó³pracuje z wieloma
protoko³ami sieciowymi. Obs³uguje standardy : Ethernet i PPP/SLIP.

%prep
%setup -q
%patch -p1

%build
cd src
make clean
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8} \
	$RPM_BUILD_ROOT/var/{log/iptraf,lib/iptraf}

install -s src/{iptraf,cfconv,rvnamed} $RPM_BUILD_ROOT%{_sbindir}

install Documentation/{iptraf,rvnamed}.8 $RPM_BUILD_ROOT%{_mandir}/man8

gzip -9nf README* CHANGES \
	$RPM_BUILD_ROOT%{_mandir}/man8/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README*,CHANGES}.gz
%doc Documentation/*.{gif,html}
%attr(755,root,root) %{_sbindir}/*
%attr(750,root,root) %dir /var/lib/iptraf
%attr(750,root,root) %dir /var/log/iptraf
%{_mandir}/man8/*
