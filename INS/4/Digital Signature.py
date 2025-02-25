#Aim: To study and implement the Digital Signature algorithm 
# Important: Rename this file and remove comments before showing output

from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random

def generate_signature(private_key, message):
    # Load the private key
    key = RSA.importKey(private_key)

    # Generate SHA-256 hash of the message
    hashed_message = SHA256.new(message.encode('utf-8'))

    # Create a signature using the private key
    signer = PKCS1_v1_5.new(key)
    signature = signer.sign(hashed_message)

    return signature

def verify_signature(public_key, message, signature):
    # Load the public key
    key = RSA.importKey(public_key)

    # Generate SHA-256 hash of the message
    hashed_message = SHA256.new(message.encode('utf-8'))

    # Verify the signature using the public key
    verifier = PKCS1_v1_5.new(key)
    return verifier.verify(hashed_message, signature)

# Generate RSA key pair
random_generator = Random.new().read
key_pair = RSA.generate(2048, random_generator)

# Extract public and private keys
public_key = key_pair.publickey().export_key()
private_key = key_pair.export_key()

# Example usage
message = "Hola Amigo"

# Generate a digital signature
signature = generate_signature(private_key, message)
print("Generated Signature:", signature)

# Verify the digital signature
is_valid = verify_signature(public_key, message, signature)
print("Signature Verification Result:", is_valid)
