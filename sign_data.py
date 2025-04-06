import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding


with open("private_key.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(f.read(), password=None)


def sign_data(data):
    signature = private_key.sign(
        data.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH,
        ),
        hashes.SHA256(),
    )
    return signature


message = "Important transaction details"
signature = sign_data(message)


with open("signature.pem", "w") as f:
    f.write("-----BEGIN SIGNATURE-----\n")
    f.write(base64.b64encode(signature).decode() + "\n")
    f.write("-----END SIGNATURE-----\n")

    
print("Data Signed Successfully! (signature.sig saved)")
