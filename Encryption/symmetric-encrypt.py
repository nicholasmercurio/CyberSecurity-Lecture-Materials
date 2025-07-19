from cryptography.fernet import Fernet

# Generate a random encryption key
key = Fernet.generate_key()

# Create a Fernet cipher object with the key
cipher_suite = Fernet(key)

# Message to be encrypted
message = b"Hello, this is a secret message."

# Encryption
cipher_text = cipher_suite.encrypt(message)

# Decryption
plain_text = cipher_suite.decrypt(cipher_text)

# Display the results
print("Original Message:", message.decode())
print("Encrypted Message:", cipher_text)
print("Decrypted Message:", plain_text.decode())