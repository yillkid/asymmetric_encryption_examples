from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
from base64 import b64encode, b64decode
import binascii

def bin2hex(bin_str):
    return binascii.hexlify(bin_str)

def hex2bin(hex_str):
    return binascii.unhexlify(hex_str)

def decrypt_with_pri_key(private_key, data):
    # Decrypt
    # private_key = ""
    decrypted = ""
    # with open("./private.pem", 'r') as outfile:
    #    private_key = outfile.read()

    privatekey = RSA.importKey(private_key)
    decryptor = PKCS1_OAEP.new(privatekey)

    # Convert string to byte
    encrypted = data.encode('ascii')

    # Hex to bin
    encrypted = hex2bin(encrypted)
    decrypted = decryptor.decrypt(encrypted)

    return decrypted.decode()


#cyphertext = "013b0a7a2811bfcbbd35d18a4142f28605eadd5bd3e82a27bcc651501682c3974aeabde118fc2e93fd9095bdde7fac390fa21f36cded030b7aafefeb8bbf39257e6237f06a02cdd32d56fc8155388c0170ce45b47a0b60bcc1bd0a8db7933cc05a44ba2348aefe6ff7539db30f476bf3e24e8c5bc85776880d5590b24110baf4"

#cyphertext = decrypt_with_pri_key(cyphertext)

#print(cyphertext)
