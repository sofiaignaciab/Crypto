#pcap to hash
hcxpcapngtool -o handshake.22000 handshake.pcap

#hashcat - potfile:enable
hashcat -D 1 -m 22000 handshake.22000 rockyou_mod.dic --potfile-path potfile.txt

#hashcat - potfile:disable
hashcat -D 1 -m 22000 handshake.22000 rockyou_mod.dic --potfile-disable

#aircrack-ng
aircrack-ng -a2 -w rockyou_mod.dic handshake.pcap