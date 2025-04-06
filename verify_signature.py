from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding


with open("public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())


with open("signature.sig", "rb") as f:
    signature = f.read()


def verify_signature(data, signature):
    try:
        public_key.verify(
            signature,
            data.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH,
            ),
            hashes.SHA256(),
        )
        return True
    except:
        return False

# Example usage
message = "Important transaction details"
if verify_signature(message, signature):
    print("Signature is VALID! Data is authentic.")
else:
    print("Signature is INVALID! Data may be tampered.")
