# Microsoft PySEAL Library
# Working implementation of Homomorphic Encryption
import seal
from seal import EncryptionParameters, SEALContext, KeyGenerator, IntegerEncoder, Encryptor, Evaluator, Decryptor

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
params.set_poly_modulus(coeff_modulus_128bit(2048))

# noise budget in freshly encrypted ciphertext: log2(coeff_modulus/plain_modulus) (bits)
# noise budget in homomorphic encryption: log2(plain_modulus) + (other terms)

# plaintext modulus represented as any positive integer that determines size of plaintext data type
# small plaintext size enables good performance
params.set_plain_modulus(1 << 8)

# =============================================================================================
# pre-computed object with encryption parameters
context = SEALContext(params)


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
