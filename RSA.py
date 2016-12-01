"""
RSA implementation using the notes & algorithm defined on http://www.di-mgt.com.au/rsa_alg.html
"""

import random
from Utilities import *

#e = 65537 #e values could be 3, 5, 17, 257, 65537
k = 1024  #bit length of 1024, 2048, 3072,...

def generate_RSA_keys(e):
    """Will generate RSA key pair (n, e, d)"""
    """e should be 3, 5, 17, 257, 65537"""

    while True: #check e is coprime to phi....TODO fix generate_prime so we don't need this

        while True: #generate p
            p = generate_prime(k/2) #TODO, fixing this wouldn't require checking coprime with e
            if p % e == 1:
                break

        while True: #generate q
            q = generate_prime(k/2)
            if q != p and q % e == 1:
                break

        n = p * q
        phi = (p-1) * (q-1)

        if coprime(e, phi):
            break
    print "p:", p, "q:", q
    print "e:", e, "phi:", phi
    d = modinv(e, phi)
    return (n, e, d)


def encrypt(msg, public_key, session_key, ):
    """Encrypting using the RSA encryption system
       msg: The message with limit of bytes ???
       public_key: in xyz format ???
       session_key: ....."""
    return None

def decrypt(e_msg, private_key):
    return None

def signing(msg, sign_key):
    return None

for x in range(1, 20):
    print generate_RSA_keys(257)
