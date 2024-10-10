# AIM:Implementing Substitution and Transposition Ciphers
# Important: Rename this file and remove comments before showing output

#Ceaser Cipher
def encrypt(text, s):
    result = ""

    # Traverse the text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char  # Non-alphabetic characters are added unchanged

    return result

# Check the above function
text = input("Enter the text to encrypt: ")
s = 3  # You can change the shift value here
print("Text : " + text)
print("Cipher: " + encrypt(text, s))





#Railfence Cipher
def RailFence(txt):
    result = ""
    
    # Append characters at even indices first
    for i in range(len(txt)):
        if i % 2 == 0:
            result += txt[i]
    
    # Append characters at odd indices next
    for i in range(len(txt)):
        if i % 2 != 0:
            result += txt[i]
    
    return result

# Get input from the user
string = input("Enter a string: ")
print("Rail Fence Cipher:", RailFence(string))

