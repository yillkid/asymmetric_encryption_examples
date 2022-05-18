from base64 import (
    b64encode,
    b64decode,
)

from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA


def sign_data(pri, data):
    message = data.encode("utf-8")
    digest = SHA256.new()
    digest.update(message)

    # Read shared key from file
    private_key = RSA.importKey(pri)

    # Load private key and sign message
    signer = PKCS1_v1_5.new(private_key)
    sig = signer.sign(digest)

    return sig.hex()
