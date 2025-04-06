# Secure Server Project

This project implements a secure HTTPS server with encryption and digital signature capabilities.

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

3. Run the setup script:
```bash
python setup.py
```

4. Run the server:
```bash
python secure_server.py
```

## Features
- HTTPS Secure Server
- Data Encryption/Decryption
- Digital Signatures
- Secure Storage

## File Structure
- `secure_server.py`: HTTPS server implementation
- `secure_storage.py`: Encryption/decryption utilities
- `sign_data.py`: Digital signature creation
- `verify_signature.py`: Digital signature verification
- `generate_keys.py`: RSA key pair generation
- `setup.py`: Initial project setup

## Security Note
This is a development setup with self-signed certificates. For production use, please use properly signed certificates from a trusted Certificate Authority.

#  Secure Data Storage & Transmission using Cryptography

This project demonstrates a secure and practical implementation of cryptographic techniques using Python. It ensures confidentiality, integrity, and authenticity for sensitive data through encryption, hashing, signing, and verification. A Flask-based HTTPS server is also included for secure transmission.

---

##  Features

-  **RSA Key Pair Generation** – Public and private key generation for signing and verification.
-  **AES Encryption/Decryption** – Symmetric encryption for secure data storage.
-  **SHA-256 Hashing** – Hash generation for data integrity verification.
-  **Digital Signature** – Sign data using private keys.
-  **Signature Verification** – Verify signatures using public keys.
-  **Self-Signed SSL Certificate Generator** – Easily generate `cert.pem` and `key.pem`.

---

##  Technologies Used

- Python 3
- Flask
- `cryptography` library
- OpenSSL (for HTTPS support)
- VS Code + GitHub

---

##  Project Structure

```
├── generate_keys.py           # Generates RSA private/public key pair
├── secure_storage.py          # AES encryption, decryption, and hashing
├── sign_data.py               # Digitally signs a message
├── verify_signature.py        # Verifies the digital signature
├── secure_server.py           # HTTPS server using Flask
├── generate_ssl.py            # Generates self-signed SSL certificates
├── private_key.pem            # RSA Private Key
├── public_key.pem             # RSA Public Key
├── cert.pem                   # SSL Certificate (self-signed)
└── key.pem                    # SSL Private Key

```

---

##  How to Run

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Install dependencies**
   ```bash
   pip install cryptography flask
   ```

3. **Generate Keys and SSL Cert**
   ```bash
   python generate_keys.py
   python generate_ssl.py
   ```

4. **Encrypt/Decrypt Example**
   ```bash
   python secure_storage.py
   ```

5. **Sign & Verify Data**
   ```bash
   python sign_data.py
   python verify_signature.py
   ```

6. **Run Secure HTTPS Server**
   ```bash
   python secure_server.py
   ```


---

##  Project Objectives

- Implement robust cryptographic primitives using Python.
- Demonstrate secure data transmission via HTTPS.
- Ensure data integrity with hashing and signatures.
- Build a self-contained and beginner-friendly security module.

---

##  Future Enhancements

-  Integrate user authentication (JWT).
-  Host the HTTPS server on a cloud platform (Heroku, Render, etc.).
-  Create a Python package or CLI tool for cryptographic operations.
-  Add unit testing and input validation.
-  Add a frontend interface for uploading and encrypting files.

---



