import sys
from collections import Counter
from scapy.all import *
from termcolor import colored
from scapy.all import ICMP

expected_freq = {'a': 0.0817, 'b': 0.0149, 'c': 0.0278, 'd': 0.0425, 'e': 0.127, 'f': 0.0223,
                 'g': 0.0202, 'h': 0.0609, 'i': 0.0697, 'j': 0.0015, 'k': 0.0077, 'l': 0.0403,
                 'm': 0.0241, 'n': 0.0675, 'o': 0.0751, 'p': 0.0193, 'q': 0.001, 'r': 0.0599,
                 's': 0.0633, 't': 0.0906, 'u': 0.0276, 'v': 0.0098, 'w': 0.0236, 'x': 0.0015,
                 'y': 0.0197, 'z': 0.0007}

def cesarDecrypt(text, shift):
    plaintext = ''
    for char in text:
        if char.isalpha():
            shifted = ord(char) - shift
            if shifted < ord('a'):
                shifted += 26
            plaintext += chr(shifted)
        else:
            plaintext += char
    return plaintext

def readPCAPNG(filename):
    packets = rdpcap(filename)
    payloads = []
    for packet in packets:
        if packet.haslayer(ICMP):
            payload = packet[ICMP].load.decode()
            payloads.append(payload[8])
    return payloads

def calculate_frequency(text):
    freq_counter = Counter(text.lower())
    total_chars = sum(freq_counter.values())
    freq_dict = {char: count / total_chars for char, count in freq_counter.items()}
    return freq_dict

if __name__ == "__main__":
    pcapng_file = sys.argv[1]
    payloads = readPCAPNG(pcapng_file)

    best_shift = None
    min_distance = float('inf')

    for shift in range(26):
        decrypted_message = ''.join([cesarDecrypt(payload, shift) for payload in payloads])
        freq_dict = calculate_frequency(decrypted_message)
        distance = sum((freq_dict.get(char, 0) - expected_freq.get(char, 0)) ** 2 for char in expected_freq)
        if distance < min_distance:
            best_shift = shift
            min_distance = distance

    for shift in range(26):
        decrypted_message = ''.join([cesarDecrypt(payload, shift) for payload in payloads])
        if shift == best_shift:
            print(colored(f"{shift}: {decrypted_message}", 'green'))
        else:
            print(f"{shift}: {decrypted_message}")
