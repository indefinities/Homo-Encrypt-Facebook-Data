# Microsoft PySEAL Library
# https://github.com/Lab41/PySEAL
# Working implementation of Homomorphic Encryption

import seal
from seal import EncryptionParameters, SEALContext, KeyGenerator, IntegerEncoder, Encryptor, Evaluator, Decryptor, \
    Ciphertext, Plaintext

# ============================================================================================
# SET PARAMETERS
# encryption parameters that set the invariant noise budget for each ciphertext
# invariant noise budget = determines the encryption quality

params = EncryptionParameters()

# three encryption parameters:
# - poly_modulus (polynomial modulus)
# - coeff_modulus ([ciphertext] coefficient modulus)
# - plain_modulus (plaintext modulus)

# recommended degrees for poly_modulus: 1024, 2048, 4096, 8192, 16384, 32768
params.set_poly_modulus("1x^2048 + 1")

# coefficient modulus determines noise budget in freshly encrypted ciphertext
# (bigger = more noise budget = lower security level)
# recommended security levels: 128-bit, 192-bit
# Number Theoretic Transform (NTT) for polynomial multiplications ratio:
# factors converted to 1 modulo 2*degree(poly_modulus)

# parameter: degree of polynomial modulus
params.set_coeff_modulus(seal.coeff_modulus_128(2048))

# noise budget in freshly encrypted ciphertext: log2(coeff_modulus/plain_modulus) (bits)
# noise budget in homomorphic encryption: log2(plain_modulus) + (other terms)

# plaintext modulus represented as any positive integer that determines size of plaintext data type
# small plaintext size enables good performance
params.set_plain_modulus(1 << 8)

# =============================================================================================
# pre-computed object with encryption parameters
context = SEALContext(params)


# Utilize encryption objects to perform a successful homomorphic encryption
def encryption(value):
    # IntegerEncoder with base 2
    encoder = IntegerEncoder(context.plain_modulus())

    # generate public/private keys
    keygen = KeyGenerator(context)
    public_key = keygen.public_key()
    secret_key = keygen.secret_key()

    # encrypts public key
    encryptor = Encryptor(context, public_key)

    # perform computations on ciphertexts
    evaluator = Evaluator(context)

    # decrypts secret key
    decryptor = Decryptor(context, secret_key)

    # perform encryptions
    plaintext = encoder.encode(value)

    # convert into encrypted ciphertext
    encrypt = Ciphertext()
    encryptor.encrypt(plaintext, encrypt)
    print("Encryption successful!")
    print("Encrypted ciphertext: " + (str)(value) + " as " + plaintext.to_string())

    # noise budget of fresh encryptions
    print("Noise budget: " + (str)(decryptor.invariant_noise_budget(encrypt)) + " bits")

    # decrypts result
    result = Plaintext()
    decryptor.decrypt(encrypt, result)
    print("Decryption successful!")

    print("Plaintext: " + result.to_string())

    # decode for original integer
    print("Original node: " + (str)(encoder.decode_int32(result)) + "\n")
