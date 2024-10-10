#Aim: To study and implement the Message Authentication Code  for ensuring the message intergrity and authenticity 
# Important: Rename this file and remove comments before showing output

import hashlib

# Compute MD5 hashes
result = hashlib.md5(b'Hola')
result1 = hashlib.md5(b'Amigo')

# Printing the equivalent byte value
print("The byte equivalent of hash is (for 'Hola'): ", end="")
print(result.digest())

print("The byte equivalent of hash is (for 'Amigo'): ", end="")
print(result1.digest())


#SHA-1
import hashlib

# Get user input
str_input = input("Enter the value to encode: ")

# Compute SHA-1 hash
result = hashlib.sha1(str_input.encode())

# Print the hexadecimal equivalent of SHA-1
print("The hexadecimal equivalent of SHA-1 is:")
print(result.hexdigest())
