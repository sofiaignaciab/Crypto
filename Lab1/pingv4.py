import sys
import time
from scapy.all import IP, ICMP, send
from datetime import datetime


def sendICMP(character,seq,id):

    ts = int(time.time())
    hex_ts = hex(ts)[2:].zfill(16)
    bytes_ts = bytes.fromhex(hex_ts)
    reversed_bytes_ts = bytes_ts[::-1]
    data = bytes(character + '\x00\x00', 'utf-8')
    data += bytes('\x00\x00\x00\x00\x00', 'utf-8')
    data += bytes(range(0x10, 0x38))
    payload = reversed_bytes_ts + data
    package = IP(dst='127.0.0.1')/ICMP(seq=seq, id=id)/payload
    
    send(package)

def sendICMPPackege(text):
    seq=1
    id=1
    for caracter in text:
        sendICMP(caracter, seq,id)
        seq+=1
        id+=1
        time.sleep(1)

if __name__ == "__main__":
    text = sys.argv[1]
    sendICMPPackege(text)
