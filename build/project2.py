import os
import sys
from timeit import default_timer as timer
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def keygen(size):
    if(size != 256 and size != 192 and size != 128):
        print("Incorrect key size")
        return
    key = os.urandom(int(size/8))

    #converts the bytes to hexadecimal string so you can read it in hexadecimal
    hexstr = "".join(["0x{0}".format(format(byte,"02x")) for byte in key])

    with open("../data/key.txt", "w") as fs:
        fs.write(hexstr)
 
def cbcenc():
    with open("../data/key.txt") as kf:
        keytext = kf.read()
    with open("../data/plainText.txt") as pf:
        plaintext = pf.read()
    paddedtext = plaintext

    #padding the text because the text has to be divisible by the block size which 128 bits or 16 bytes in AES
    while((len(paddedtext) % 16) != 0):
        paddedtext += " "

    #iv must be the same size as the block size which is 16 bytes in AES
    iv = os.urandom(int(16))
    ivstring = "".join(["0x{0}".format(format(byte,"02x")) for byte in iv])
    key = bytes([int(b,16) for b in keytext.split("0x")[1:]])

    #writes iv to a file
    with open("../data/iv.txt", 'w') as ivf: 
        ivf.write("".join(["0x{0}".format(format(byte,"02x")) for byte in iv]))

    #encrypts the paddedtext with AES-CBC-256 standard
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(paddedtext.encode(encoding='UTF-8')) + encryptor.finalize()
    #writes the ciphertext to a file
    with open("../data/ciphertext.txt", 'w') as cf:
        cf.write("".join(["0x{0}".format(format(byte,"02x")) for byte in ciphertext]))

def cbcdec():
    with open("../data/key.txt") as kf:
        keytext = kf.read()
    with open("../data/iv.txt") as ivf:
        ivtext = ivf.read()
    with open("../data/ciphertext.txt") as cf:
        ciphertext = cf.read()

    #decrypts the paddedtext with AES-CBC-256 standard
    backend = default_backend()
    key = bytes([int(b,16) for b in keytext.split("0x")[1:]])
    iv = bytes([int(b,16) for b in ivtext.split("0x")[1:]])
    cipherbytes = bytes([int(b,16) for b in ciphertext.split("0x")[1:]])
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()
    decryptedstr = decryptor.update(cipherbytes) + decryptor.finalize()

    #turns the byte string back into a hexadecimal string and translates that to readable text 
    result =  "".join(["{0}".format(format(byte,"02x")) for byte in decryptedstr])
    translatedResult = bytearray.fromhex(result).decode()
    #writes original message to file perhaps with some spaces at the end because of the padding.
    with open("../data/result.txt", 'w') as rf:
        rf.write(translatedResult)

def ecbenc():
    with open("../data/key.txt") as kf:
        keytext = kf.read()
    with open("../data/plainText.txt") as pf:
        plaintext = pf.read()
    paddedtext = plaintext

    #padding the text because the text has to be divisible by the block size which 128 bits or 16 bytes in AES
    while((len(paddedtext) % 16) != 0):
        paddedtext += " "

    key = bytes([int(b,16) for b in keytext.split("0x")[1:]])

    #encrypts the paddedtext with AES-ECB-256 standard
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(paddedtext.encode(encoding='UTF-8')) + encryptor.finalize()
    #writes the ciphertext to a file
    with open("../data/ciphertext.txt", 'w') as cf:
        cf.write("".join(["0x{0}".format(format(byte,"02x")) for byte in ciphertext]))

def ecbdec():
    with open("../data/key.txt") as kf:
        keytext = kf.read()
    with open("../data/iv.txt") as ivf:
        ivtext = ivf.read()
    with open("../data/ciphertext.txt") as cf:
        ciphertext = cf.read()

    #decrypts the paddedtext with AES-ECB-256 standard
    backend = default_backend()
    key = bytes([int(b,16) for b in keytext.split("0x")[1:]])
    iv = bytes([int(b,16) for b in ivtext.split("0x")[1:]])
    cipherbytes = bytes([int(b,16) for b in ciphertext.split("0x")[1:]])
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    decryptor = cipher.decryptor()
    decryptedstr = decryptor.update(cipherbytes) + decryptor.finalize()

    #turns the byte string back into a hexadecimal string and translates that to readable text 
    result =  "".join(["{0}".format(format(byte,"02x")) for byte in decryptedstr])
    translatedResult = bytearray.fromhex(result).decode()
    with open("../data/result.txt", 'w') as rf:
        rf.write(translatedResult)
    
def main():
    option = input("Choose from the following: Key Generation, Encryption, Decryption \n")
    print("You have chosen ", option)
    if(option.upper() == "KEY GENERATION"):
    	#since we are going with the AES-CBC-256 standard I'm going to use 256 as the default key size.
        keygen(256)
    elif(option.upper() == "ENCRYPTION"):
        mode = input("I see you have chosen encryption. What kind of encryption? You got either CBC or ECB.: ")
        if(mode.upper() == "CBC"):
            start = timer()
            cbcenc()
            end = timer()
            print(end - start)
        elif(mode.upper() == "ECB"):
            start = timer()
            ecbenc()
            end = timer()
            print(end - start)
        else:
            print("I don't understand. You'll have to run it again. Sorry.")
    elif(option.upper() == "DECRYPTION"):
        mode = input("Decryption? I'll do it for one bitcoin. JK. I wish.:P But I'm not going to print it out for you. Go find it in the result file. Choose either CBC or ECB decryption.: ")
        if(mode.upper() == "CBC"):
            start = timer()
            cbcdec()
            end = timer()
            print(end - start)
        elif(mode.upper() == "ECB"):
            start = timer()
            ecbdec()
            end = timer()
            print(end - start)
    else:
        print("I'm pretty dumb. I can't tell if you misspelled something or not. Please try again! This is what you chose")
        print(option.upper())
main()