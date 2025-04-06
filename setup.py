import os
from generate_keys import generate_key_pair
from secure_server import create_self_signed_cert

def setup_project():
    print("Setting up the security project...")
    
    # Generate RSA keys for signing
    if not (os.path.exists("private_key.pem") and os.path.exists("public_key.pem")):
        generate_key_pair()
        print("Generated RSA key pair")
    
    # Generate SSL certificates
    if not (os.path.exists("cert.pem") and os.path.exists("key.pem")):
        create_self_signed_cert()
        print("Generated SSL certificates")
    
    print("\nSetup complete! You can now run the secure server and other scripts.")

if __name__ == "__main__":
    setup_project() 