from Crypto.PublicKey import RSA

def gen_key_pair():
    key = RSA.generate(1024)
    public_key = key.publickey().exportKey('PEM').decode('ascii')
    private_key = key.exportKey('PEM').decode('ascii')

    with open("credentials/keys/private.pem", 'w') as outfile:
        outfile.write(private_key)

    with open("credentials/keys/public.txt", 'w') as outfile:
        outfile.write(public_key)

    return public_key, private_key
