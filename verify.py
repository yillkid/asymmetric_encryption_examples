from base64 import (
    b64encode,
    b64decode,
)

from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA

def verify_data(data, pub, sig):
    sig = bytes.fromhex(sig)
    data = str.encode(data)
    
    digest = SHA256.new()
    digest.update(data)

    public_key = RSA.importKey(pub)

    # Load public key and verify message
    public_key = RSA.importKey(pub)

    verifier = PKCS1_v1_5.new(public_key)
    verified = verifier.verify(digest, sig)

    return verified
