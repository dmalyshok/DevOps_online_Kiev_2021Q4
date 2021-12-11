## Task6.2
    1. Use already created internal-network for three VMs (VM1-VM3). VM1 has NAT and internal, VM2, VM3 – internal only interfaces.
```
Add Internal Network in VM1 and VM2 and VM3 in virtualbox:

Internet - Host - enp0s3 (DHCP) - VM1 - enp0s8 (10.20.1.1) ----- Internal Network ---- enp0s3 (10.20.1.2)- VM 2
                                                                        |------------- enp0s3 (10.20.1.3)- VM 3
```
    2. Install and configure DHCP server on VM1. (3 ways: using VBoxManage, DNSMASQ and ISC-DHSPSERVER). You should use at least 2 of them.
```
root@vm1malyshok:~# sudo apt-get install isc-dhcp-server

root@vm1malyshok:~# ip -br addr
lo               UNKNOWN        127.0.0.1/8 ::1/128
enp0s3           UP             10.0.2.15/24 fe80::a00:27ff:fee4:78db/64
enp0s8           UP             10.20.1.1/24 fe80::a00:27ff:fea6:d4cb/64

root@vm1malyshok:~# sudo vi /etc/default/isc-dhcp-server

root@vm1malyshok:~# sudo cat /etc/default/isc-dhcp-server
# Defaults for isc-dhcp-server (sourced by /etc/init.d/isc-dhcp-server)

# Path to dhcpd's config file (default: /etc/dhcp/dhcpd.conf).
#DHCPDv4_CONF=/etc/dhcp/dhcpd.conf
#DHCPDv6_CONF=/etc/dhcp/dhcpd6.conf
....
# On what interfaces should the DHCP server (dhcpd) serve DHCP requests?
#       Separate multiple interfaces with spaces, e.g. "eth0 eth1".
INTERFACESv4="enp0s8"
INTERFACESv6=""

root@vm1malyshok:~# sudo cp /etc/dhcp/dhcpd.conf /etc/dhcp/dhcpd.conf.old
root@vm1malyshok:~# sudo vi /etc/dhcp/dhcpd.conf

option domain-name "malyshok.org.ua";
option domain-name-servers 10.20.1.1;
default-lease-time 32400;
max-lease-time 604800;
ignore-client-uids on;
# A slightly different configuration for an internal subnet.
subnet 10.20.1.0 netmask 255.255.255.0 {
  authoritative;
  range 10.20.1.2 10.20.1.10;
  option domain-name-servers 10.20.1.1;
  option subnet-mask 255.255.255.0;
  option routers 10.20.1.1;
  option broadcast-address 10.20.1.255;
}


root@vm1malyshok:~# sudo service isc-dhcp-server restart

root@vm1malyshok:~# sudo service isc-dhcp-server status
● isc-dhcp-server.service - ISC DHCP IPv4 server
     Loaded: loaded (/lib/systemd/system/isc-dhcp-server.service; enabled; vendor preset: enabled)
     Active: active (running) since Fri 2021-12-10 10:06:44 UTC; 1min 24s ago
       Docs: man:dhcpd(8)
   Main PID: 2519 (dhcpd)
      Tasks: 4 (limit: 467)
     Memory: 7.7M
     CGroup: /system.slice/isc-dhcp-server.service
             └─2519 dhcpd -user dhcpd -group dhcpd -f -4 -pf /run/dhcp-server/dhcpd.pid -cf /etc/dhcp/dhcpd.conf >

Dec 10 10:06:44 vm1malyshok sh[2519]: PID file: /run/dhcp-server/dhcpd.pid
Dec 10 10:06:44 vm1malyshok dhcpd[2519]: Wrote 0 leases to leases file.
Dec 10 10:06:44 vm1malyshok sh[2519]: Wrote 0 leases to leases file.
Dec 10 10:06:44 vm1malyshok dhcpd[2519]: Listening on LPF/enp0s8/08:00:27:a6:d4:cb/10.20.1.0/24
Dec 10 10:06:44 vm1malyshok sh[2519]: Listening on LPF/enp0s8/08:00:27:a6:d4:cb/10.20.1.0/24
Dec 10 10:06:44 vm1malyshok sh[2519]: Sending on   LPF/enp0s8/08:00:27:a6:d4:cb/10.20.1.0/24
Dec 10 10:06:44 vm1malyshok sh[2519]: Sending on   Socket/fallback/fallback-net
Dec 10 10:06:44 vm1malyshok dhcpd[2519]: Sending on   LPF/enp0s8/08:00:27:a6:d4:cb/10.20.1.0/24
Dec 10 10:06:44 vm1malyshok dhcpd[2519]: Sending on   Socket/fallback/fallback-net
Dec 10 10:06:44 vm1malyshok dhcpd[2519]: Server starting service.
```

    3. Check VM2 and VM3 for obtaining network addresses from DHCP server.
```
VM2:

vi /etc/netplan/00-installer-config.yaml
# This is the network config written by 'subiquity'
network:
  ethernets:
    enp0s3:
      dhcp4: yes
  version: 2

root@vm2malyshok:~# netplan apply

root@vm2malyshok:~# ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:e4:78:db brd ff:ff:ff:ff:ff:ff
    inet 10.20.1.2/24 brd 10.20.1.255 scope global dynamic enp0s3
       valid_lft 590sec preferred_lft 590sec
    inet6 fe80::a00:27ff:fee4:78db/64 scope link
       valid_lft forever preferred_lft forever

root@vm2malyshok:~# ip route
default via 10.20.1.1 dev enp0s3 proto dhcp src 10.20.1.2 metric 100
10.20.1.0/24 dev enp0s3 proto kernel scope link src 10.20.1.2
10.20.1.1 dev enp0s3 proto dhcp scope link src 10.20.1.2 metric 100


root@vm1malyshok:~# cat /var/lib/dhcp/dhcpd.leases
lease 10.20.1.6 {
  starts 6 2021/12/11 09:35:05;
  ends 6 2021/12/11 18:35:05;
  cltt 6 2021/12/11 09:35:05;
  binding state active;
  next binding state free;
  rewind binding state free;
  hardware ethernet 08:00:27:e4:78:db;
  client-hostname "vm2malyshok";
}

root@vm1malyshok:~# cat /var/lib/dhcp/dhcpd.leases

VM3:

vi /etc/netplan/00-installer-config.yaml
# This is the network config written by 'subiquity'
network:
  ethernets:
    enp0s3:
      dhcp4: yes
  version: 2

root@vm2malyshok:~# netplan apply

root@vm1malyshok:~# cat /var/lib/dhcp/dhcpd.leases

lease 10.20.1.7 {
  starts 6 2021/12/11 09:35:08;
  ends 6 2021/12/11 18:35:08;
  cltt 6 2021/12/11 09:35:08;
  binding state active;
  next binding state free;
  rewind binding state free;
  hardware ethernet 08:00:27:9c:a0:78;
  client-hostname "vm3malyshok";
}

```
    4. Using existed network for three VMs (from p.1) install and configure DNS server on VM1. (You can use DNSMASQ, BIND9 or something else).
```
VM1:
sudo apt install bind9

root@vm1malyshok:~# cat /etc/bind/named.conf.options
options {
        directory "/var/cache/bind";

        // If there is a firewall between you and nameservers you want
        // to talk to, you may need to fix the firewall to allow multiple
        // ports to talk.  See http://www.kb.cert.org/vuls/id/800113

        // If your ISP provided one or more IP addresses for stable
        // nameservers, you probably want to use them as forwarders.
        // Uncomment the following block, and insert the addresses replacing
        // the all-0's placeholder.

         forwarders {
                8.8.8.8;
         };

        //========================================================================
        // If BIND logs error messages about the root key being expired,
        // you will need to update your keys.  See https://www.isc.org/bind-keys
        //========================================================================
        //dnssec-validation auto;
        dnssec-enable yes;
        dnssec-validation yes;
        listen-on-v6 { any; };
};

root@vm1malyshok:~# cat /etc/resolv.conf
nameserver 127.0.0.1

root@vm1malyshok:~# nslookup google.com.ua
Server:         127.0.0.1
Address:        127.0.0.1#53

Non-authoritative answer:
Name:   google.com.ua
Address: 142.250.185.195
Name:   google.com.ua
Address: 2a00:1450:4001:812::2003
``` 
    5. Check VM2 and VM3 for gaining access to DNS server (naming services).
```
VM2:

malyshok@vm2malyshok:~$ dig google.com.ua

; <<>> DiG 9.16.1-Ubuntu <<>> google.com.ua
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 18400
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;google.com.ua.                 IN      A

;; ANSWER SECTION:
google.com.ua.          81      IN      A       142.250.185.195

;; Query time: 4 msec
;; SERVER: 127.0.0.53#53(127.0.0.53)
;; WHEN: Sat Dec 11 09:11:49 UTC 2021
;; MSG SIZE  rcvd: 58

VM3:
malyshok@vm3malyshok:~$ dig google.com.ua @10.20.1.1 +short
142.250.185.195

malyshok@vm3malyshok:~$ nslookup epam.com 10.20.1.1
Server:         10.20.1.1
Address:        10.20.1.1#53

Non-authoritative answer:
Name:   epam.com
Address: 3.214.134.159
```

    6. ***Using the scheme which follows, configure dynamic routing using OSPF protocol.
```
VM1:

sudo apt install quagga quagga-doc
add /etc/sysctl.conf : net.ipv4.ip_forward=1
cp /usr/share/doc/quagga-core/examples/vtysh.conf.sample /etc/quagga/vtysh.conf
cp /usr/share/doc/quagga-core/examples/zebra.conf.sample /etc/quagga/zebra.conf
cp /usr/share/doc/quagga-core/examples/bgpd.conf.sample /etc/quagga/bgpd.conf
cp /usr/share/doc/quagga-core/examples/ospfd.conf.sample /etc/quagga/ospfd.conf
sudo chown quagga:quagga /etc/quagga/*.conf
sudo chown quagga:quaggavty /etc/quagga/vtysh.conf
sudo chmod 640 /etc/quagga/*.conf

sudo service zebra start
sudo service zebra status
sudo service ospfd start
sudo service ospfd status

"Console" access:
zebra: telnet localhost 2601
ospfd: telnet localhost 2604
vtysh: sudo vtysh

the default password is zebra.

root@vm1malyshok:~# cat /etc/quagga/zebra.conf
!
! Zebra configuration saved from vty
!   2021/12/11 12:27:47
!
hostname Router
password zebra
enable password zebra
log file /var/log/quagga/ospfd.log
!
interface enp0s3
 description WAN
 ip address 10.0.2.15/24
!
interface enp0s8
 description LAN
 ip address 10.20.1.1/24
!
interface lo
!
ip forwarding
!
!
line vty
!


root@vm1malyshok:~# cat /etc/quagga/ospfd.conf
!
! Zebra configuration saved from vty
!   2021/12/11 12:27:47
!
hostname ospfd
password zebra
log file /var/log/quagga/ospfd.log
log stdout
!
!
!
interface enp0s3
!
interface enp0s8
!
interface lo
!
router ospf
 ospf router-id 10.20.1.1
 log-adjacency-changes
 redistribute kernel
 redistribute connected
 redistribute static
 network 10.0.2.0/24 area 0.0.0.0
 network 10.20.1.0/24 area 0.0.0.0
!
line vty
!

VM2:

sudo apt install quagga quagga-doc
add /etc/sysctl.conf : net.ipv4.ip_forward=1
cp /usr/share/doc/quagga-core/examples/vtysh.conf.sample /etc/quagga/vtysh.conf
cp /usr/share/doc/quagga-core/examples/zebra.conf.sample /etc/quagga/zebra.conf
cp /usr/share/doc/quagga-core/examples/bgpd.conf.sample /etc/quagga/bgpd.conf
cp /usr/share/doc/quagga-core/examples/ospfd.conf.sample /etc/quagga/ospfd.conf
sudo chown quagga:quagga /etc/quagga/*.conf
sudo chown quagga:quaggavty /etc/quagga/vtysh.conf
sudo chmod 640 /etc/quagga/*.conf

sudo service zebra start
sudo service zebra status
sudo service ospfd start
sudo service ospfd status

"Console" access:
zebra: telnet localhost 2601
ospfd: telnet localhost 2604
vtysh: sudo vtysh

the default password is zebra.

root@vm2malyshok:~# cat /etc/quagga/zebra.conf
!
! Zebra configuration saved from vty
!   2021/12/11 12:28:13
!
hostname Router
password zebra
enable password zebra
!
interface enp0s3
 description LAN
 ip address 10.20.1.6/24
!
interface lo
!
ip forwarding
!
!
line vty
!

root@vm2malyshok:~# cat /etc/quagga/ospfd.conf
!
! Zebra configuration saved from vty
!   2021/12/11 12:28:13
!
hostname ospfd
password zebra
log stdout
!
!
!
interface enp0s3
 description LAN
!
interface lo
!
router ospf
 ospf router-id 10.20.1.6
 log-adjacency-changes
 redistribute kernel
 redistribute connected
 redistribute static
 network 10.20.1.0/24 area 0.0.0.0
!
line vty
!

VM3:

sudo apt install quagga quagga-doc
add /etc/sysctl.conf : net.ipv4.ip_forward=1
cp /usr/share/doc/quagga-core/examples/vtysh.conf.sample /etc/quagga/vtysh.conf
cp /usr/share/doc/quagga-core/examples/zebra.conf.sample /etc/quagga/zebra.conf
cp /usr/share/doc/quagga-core/examples/bgpd.conf.sample /etc/quagga/bgpd.conf
cp /usr/share/doc/quagga-core/examples/ospfd.conf.sample /etc/quagga/ospfd.conf
sudo chown quagga:quagga /etc/quagga/*.conf
sudo chown quagga:quaggavty /etc/quagga/vtysh.conf
sudo chmod 640 /etc/quagga/*.conf

sudo service zebra start
sudo service zebra status
sudo service ospfd start
sudo service ospfd status

"Console" access:
zebra: telnet localhost 2601
ospfd: telnet localhost 2604
vtysh: sudo vtysh

the default password is zebra.

root@vm3malyshok:~#  cat /etc/quagga/zebra.conf
!
! Zebra configuration saved from vty
!   2021/12/11 12:30:07
!
hostname Router
password zebra
enable password zebra
!
interface enp0s3
 description LAN
 ip address 10.20.1.7/24
!
interface lo
!
ip forwarding
!
!
line vty
!

root@vm3malyshok:~# cat /etc/quagga/ospfd.conf
!
! Zebra configuration saved from vty
!   2021/12/11 12:30:07
!
hostname ospfd
password zebra
log stdout
!
!
!
interface enp0s3
 description LAN
!
interface lo
!
router ospf
 ospf router-id 10.20.1.7
 log-adjacency-changes
 redistribute kernel
 redistribute connected
 redistribute static
 network 10.20.1.0/24 area 0.0.0.0
!
line vty
!
```
    7. Check results.
```
VM1:
root@vm1malyshok:~# sudo vtysh

Hello, this is Quagga (version 1.2.4).
Copyright 1996-2005 Kunihiro Ishiguro, et al.

vm1malyshok# sh ip ospf neighbor

Neighbor ID     Pri State           Dead Time Address         Interface            RXmtL RqstL DBsmL
10.20.1.6         1 Full/DR           31.340s 10.20.1.6       enp0s8:10.20.1.1         0     0     0
10.20.1.7         1 Full/DROther      38.700s 10.20.1.7       enp0s8:10.20.1.1         0     0     0

VM2:

vm2malyshok# sh ip ospf neighbor

Neighbor ID     Pri State           Dead Time Address         Interface            RXmtL RqstL DBsmL
10.20.1.1         1 Full/Backup       37.759s 10.20.1.1       enp0s3:10.20.1.6         0     0     0
10.20.1.7         1 Full/DROther      35.581s 10.20.1.7       enp0s3:10.20.1.6         0     0     0
vm2malyshok#

vm1malyshok# sh ip route
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, P - PIM, A - Babel, N - NHRP,
       > - selected route, * - FIB route

K>* 0.0.0.0/0 via 10.0.2.2, enp0s3, src 10.0.2.15
O   10.0.2.0/24 [110/10] is directly connected, enp0s3, 01:26:00
C>* 10.0.2.0/24 is directly connected, enp0s3
K>* 10.0.2.2/32 is directly connected, enp0s3
O   10.20.1.0/24 [110/10] is directly connected, enp0s8, 01:25:45
C>* 10.20.1.0/24 is directly connected, enp0s8
O>* 10.20.1.1/32 [110/20] via 10.20.1.6, enp0s8, 00:10:49
  *                       via 10.20.1.7, enp0s8, 00:10:49
C>* 127.0.0.0/8 is directly connected, lo

vm2malyshok# sh ip route
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, P - PIM, A - Babel, N - NHRP,
       > - selected route, * - FIB route

K>* 0.0.0.0/0 via 10.20.1.1, enp0s3, src 10.20.1.6
O   10.0.2.0/24 [110/20] via 10.20.1.1, enp0s3 inactive, 01:25:09
O   10.0.2.2/32 [110/20] via 10.20.1.1, enp0s3 inactive, 00:14:25
O   10.20.1.0/24 [110/10] is directly connected, enp0s3, 01:28:19
C>* 10.20.1.0/24 is directly connected, enp0s3
O   10.20.1.1/32 [110/20] via 10.20.1.7, enp0s3, 00:10:23
K>* 10.20.1.1/32 is directly connected, enp0s3
C>* 127.0.0.0/8 is directly connected, lo

VM3:

root@vm3malyshok:~# sudo vtysh

Hello, this is Quagga (version 1.2.4).
Copyright 1996-2005 Kunihiro Ishiguro, et al.

vm3malyshok# sh ip ospf neighbor

Neighbor ID     Pri State           Dead Time Address         Interface            RXmtL RqstL DBsmL
10.20.1.1         1 Full/Backup       34.132s 10.20.1.1       enp0s3:10.20.1.7         0     0     0
10.20.1.6         1 Full/DR           34.595s 10.20.1.6       enp0s3:10.20.1.7         0     0     0


vm3malyshok# sh ip route
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, P - PIM, A - Babel, N - NHRP,
       > - selected route, * - FIB route

K>* 0.0.0.0/0 via 10.20.1.1, enp0s3, src 10.20.1.7
O   10.0.2.0/24 [110/20] via 10.20.1.1, enp0s3 inactive, 00:39:06
O   10.0.2.2/32 [110/20] via 10.20.1.1, enp0s3 inactive, 00:15:12
O   10.20.1.0/24 [110/10] is directly connected, enp0s3, 00:39:06
C>* 10.20.1.0/24 is directly connected, enp0s3
O   10.20.1.1/32 [110/20] via 10.20.1.6, enp0s3, 00:13:08
K>* 10.20.1.1/32 is directly connected, enp0s3
C>* 127.0.0.0/8 is directly connected, lo


add static route add VM2:

root@vm2malyshok:~# ip route add 192.168.5.3 dev enp0s3
root@vm2malyshok:~# ip route
default via 10.20.1.1 dev enp0s3 proto dhcp src 10.20.1.6 metric 100
10.20.1.0/24 dev enp0s3 proto kernel scope link src 10.20.1.6
10.20.1.1 dev enp0s3 proto dhcp scope link src 10.20.1.6 metric 100
192.168.5.3 dev enp0s3 scope link

show new route in VM1:

vm1malyshok# sh ip route
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, P - PIM, A - Babel, N - NHRP,
       > - selected route, * - FIB route

K>* 0.0.0.0/0 via 10.0.2.2, enp0s3, src 10.0.2.15
O   10.0.2.0/24 [110/10] is directly connected, enp0s3, 01:27:36
C>* 10.0.2.0/24 is directly connected, enp0s3
K>* 10.0.2.2/32 is directly connected, enp0s3
O   10.20.1.0/24 [110/10] is directly connected, enp0s8, 01:27:21
C>* 10.20.1.0/24 is directly connected, enp0s8
O>* 10.20.1.1/32 [110/20] via 10.20.1.6, enp0s8, 00:12:25
  *                       via 10.20.1.7, enp0s8, 00:12:25
C>* 127.0.0.0/8 is directly connected, lo
O>* 192.168.5.3/32 [110/20] via 10.20.1.6, enp0s8, 00:00:33


root@vm1malyshok:~# ip route
default via 10.0.2.2 dev enp0s3 proto dhcp src 10.0.2.15 metric 100
10.0.2.0/24 dev enp0s3 proto kernel scope link src 10.0.2.15
10.0.2.2 dev enp0s3 proto dhcp scope link src 10.0.2.15 metric 100
10.20.1.0/24 dev enp0s8 proto kernel scope link src 10.20.1.1
10.20.1.1 proto zebra metric 20
        nexthop via 10.20.1.6 dev enp0s8 weight 1
        nexthop via 10.20.1.7 dev enp0s8 weight 1
192.168.5.3 via 10.20.1.6 dev enp0s8 proto zebra metric 20
```