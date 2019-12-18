import hashlib, json
from Cryptodome.PublicKey import RSA
import os

def generate(size=4096):
    # generate key pair and an address
    key = RSA.generate(size)

    private_key_readable = key.exportKey().decode("utf-8")
    public_key_readable = key.publickey().exportKey().decode("utf-8")
    address = hashlib.sha224(public_key_readable.encode("utf-8")).hexdigest()  # hashed public key
    return json.dumps({"Private Key": private_key_readable, "Public Key": public_key_readable, "Address": address})

def save(filename="test_wallet.der", data=None):
    if not os.path.exists(filename):
        with open(filename, "w") as wallet_file:
            wallet_file.write(data)
            print(f"Generated {filename}")

print("Started")
for increment in range(0,100):
    save(data=generate(), filename=str(f"wallet_{increment}.der"))