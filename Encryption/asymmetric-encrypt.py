from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Generate a pair of RSA keys (public and private)
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Extract the public key
public_key = private_key.public_key()

# Message to be encrypted
message = b"Hello, this is a secret message."

# Encryption
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Decryption
decrypted_message = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Display the results
print("Original Message:", message.decode())
print("Encrypted Message:", ciphertext)
print("Decrypted Message:", decrypted_message.decode())