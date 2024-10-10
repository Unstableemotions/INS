#Aim: To study and implement the Diffe-Hellman key exchange algorithm for secure exchange of keys between two entities. 
# Important: Rename this file and remove comments before showing output

from random import randint

if __name__ == '__main__':
    # P is a prime number that serves as the modulus for the calculations.
    P = 23  
    
    # G is the base (also called the generator) that is used in the key exchange process.
    G = 9   

    print('The Value of P is : %d' % (P))
    print('The Value of G is : %d' % (G))

    a = 4  # Secret number for Alice
    print('Secret Number for Alice is : %d' % (a))
    x = int(pow(G, a, P))  # Alice computes her public key

    b = 6  # Secret number for Bob
    print('Secret Number for Bob is : %d' % (b))
    y = int(pow(G, b, P))  # Bob computes his public key

    ka = int(pow(y, a, P))  # Alice computes the shared secret key using Bob's public key
    kb = int(pow(x, b, P))  # Bob computes the shared secret key using Alice's public key

    print('Secret key for Alice is : %d' % (ka))
    print('Secret key for Bob is : %d' % (kb))
