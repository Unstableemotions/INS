#Aim: To study and implement the RSA Encryption and Decryption 
# Important: Rename this file and remove comments before showing output

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

# Generate RSA key pair
keyPair = RSA.generate(1024)

# Get the public key
pubKey = keyPair.publickey()
print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))

# Get the private key
print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))

# Encryption
msg = 'RSA Algorithm'
encryptor = PKCS1_OAEP.new(pubKey)
# Convert the message to bytes
encrypted = encryptor.encrypt(msg.encode('utf-8'))
print("Encrypted:", binascii.hexlify(encrypted))
