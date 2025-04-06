from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os


key = os.urandom(32)  
iv = os.urandom(16)    

def encrypt_data(plaintext):
    """Encrypt data using AES-CBC."""
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padded_plaintext = plaintext.ljust(16 * ((len(plaintext) // 16) + 1))
    ciphertext = encryptor.update(padded_plaintext.encode()) + encryptor.finalize()
    return ciphertext

def decrypt_data(ciphertext):
    """Decrypt AES-encrypted data."""
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext.strip().decode()

def hash_data(data):
    """Generate SHA-256 hash."""
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(data.encode())
    return digest.finalize().hex()


plaintext = "Secure Data Storage Example"
ciphertext = encrypt_data(plaintext)
decrypted_text = decrypt_data(ciphertext)
hashed_text = hash_data(plaintext)

print(f"Original: {plaintext}")
print(f"Encrypted: {ciphertext.hex()}")
print(f"Decrypted: {decrypted_text}")
print(f"Hashed: {hashed_text}")
