import hmac
from binascii import a2b_hex, b2a_hex
from hashlib import pbkdf2_hmac, sha1, md5

def PRF(key, A, B):
    nByte = 64
    i = 0
    R = b''
    while(i <= ((nByte * 8 + 159) / 160)):
        hmacsha1 = hmac.new(key, A + chr(0x00).encode() + B + chr(i).encode(), sha1)
        R = R + hmacsha1.digest()
        i += 1
    return R[0:nByte]

def MakeAB(aNonce, sNonce, apMac, cliMac):
    A = b"Pairwise key expansion"
    B = min(apMac, cliMac) + max(apMac, cliMac) + min(aNonce, sNonce) + max(aNonce, sNonce)
    return (A, B)

def MakeMIC(pwd, ssid, A, B, data, wpa = False):
    pmk = pbkdf2_hmac('sha1', pwd.encode('utf-8'), ssid.encode('utf-8'), 4096, 32)
    ptk = PRF(pmk, A, B)
    hmacFunc = md5 if wpa else sha1
    mics = [hmac.new(ptk[0:16], i, hmacFunc).digest() for i in data]
    return (mics, ptk, pmk)

def TestPwds(S, ssid, aNonce, sNonce, apMac, cliMac, data, data2, data3, targMic, targMic2, targMic3):
    A, B = MakeAB(aNonce, sNonce, apMac, cliMac)
    for i in S:
        mic, _, _ = MakeMIC(i, ssid, A, B, [data])
        v = b2a_hex(mic[0]).decode()[:-8]
        if(v != targMic):
            continue
        mic2, _, _ = MakeMIC(i, ssid, A, B, [data2])
        v2 = b2a_hex(mic2[0]).decode()[:-8]
        if(v2 != targMic2):
            continue
        mic3, _, _ = MakeMIC(i, ssid, A, B, [data3])
        v3 = b2a_hex(mic3[0]).decode()[:-8]
        if(v3 != targMic3):
            continue
        print('!!!Password Found!!!')
        print('Desired MIC1:\t\t' + targMic)
        print('Computed MIC1:\t\t' + v)
        print('\nDesired MIC2:\t\t' + targMic2)
        print('Computed MIC2:\t\t' + v2)
        print('\nDesired MIC3:\t\t' + targMic3)
        print('Computed MIC3:\t\t' + v3)
        print('Password:\t\t' + i)
        return i
    return None

if __name__ == "__main__":
    with open('/home/sofiabelmar/Documents/Universidad/Crypto/Lab3/files/rockyou_mod.dic', 'r', encoding='utf-8', errors='ignore') as f:
        S = [l.strip() for l in f]
    
    # ssid name
    ssid = "VTR-1645213"
    # ANonce
    aNonce = a2b_hex('4c2fb7eca28fba45accefde3ac5e433314270e04355b6d95086031b004a31935')
    # SNonce
    sNonce = a2b_hex("30bde6b043c2aff8ea482dee7d788e95b634e3f8e3d73c038f5869b96bbe9cdc")
    # Authenticator MAC (AP)
    apMac = a2b_hex("b0487ad2dc18")
    # Station address: MAC of client
    cliMac = a2b_hex("eede678cdf8b")
    # The first MIC
    mic1 = "1813acb976741b446d43369fb96dbf90"
    # The entire 802.1x frame of the second handshake message with the MIC field set to all zeros
    data1 = a2b_hex("0103007502010a0000000000000000000130bde6b043c2aff8ea482dee7d788e95b634e3f8e3d73c038f5869b96bbe9cdc000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001630140100000fac040100000fac040100000fac020000")
    # The second MIC
    mic2 = "a349d01089960aa9f94b5857b0ea10c6"
    # The entire 802.1x frame of the third handshake message with the MIC field set to all ceros
    data2 = a2b_hex("020300970213ca001000000000000000024c2fb7eca28fba45accefde3ac5e433314270e04355b6d95086031b004a3193500000000000000000000000000000000cd000000000000000000000000000000000000000000000000000000000000000038db0eb43c3faf2c0e8b7e8a471f962c307e707e4718be724459167a88fa281f4d7ce38f012943da788d0a7159c9fac6ad71483d788cecf18b")
    # The third MIC
    mic3 = "5cf0d63af458f13a83daa686df1f4067"
    # The entire 802.1x frame of the fourth handshake message with the MIC field set to all ceros
    data3 = a2b_hex("0103005f02030a0000000000000000000200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
    
    # Set MIC fields to zero in data1, data2, and data3
    data1 = data1[:81] + b'\x00' * 16 + data1[97:]
    data2 = data2[:81] + b'\x00' * 16 + data2[97:]
    data3 = data3[:81] + b'\x00' * 16 + data3[97:]
    
    # Run an offline dictionary attack against the access point
    TestPwds(S, ssid, aNonce, sNonce, apMac, cliMac, data1, data2, data3, mic1, mic2, mic3)
