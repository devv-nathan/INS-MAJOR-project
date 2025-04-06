from flask import Flask
import ssl
import os
from OpenSSL import crypto

app = Flask(__name__)

def create_self_signed_cert():
    """Create self-signed SSL certificates if they don't exist."""
    if not (os.path.exists("cert.pem") and os.path.exists("key.pem")):
        # Generate key
        k = crypto.PKey()
        k.generate_key(crypto.TYPE_RSA, 2048)

        # Generate certificate
        cert = crypto.X509()
        cert.get_subject().C = "IN"
        cert.get_subject().ST = "Delhi"
        cert.get_subject().L = "New Delhi"
        cert.get_subject().O = "Organization"
        cert.get_subject().OU = "Organizational Unit"
        cert.get_subject().CN = "localhost"
        cert.set_serial_number(1000)
        cert.gmtime_adj_notBefore(0)
        cert.gmtime_adj_notAfter(365*24*60*60)  # Valid for one year
        cert.set_issuer(cert.get_subject())
        cert.set_pubkey(k)
        cert.sign(k, 'sha256')

        # Save certificate
        with open("cert.pem", "wb") as f:
            f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
        with open("key.pem", "wb") as f:
            f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, k))
        print("Generated new SSL certificates")

@app.route("/")
def home():
    return "Secure HTTPS Server!"

if __name__ == "__main__":
    create_self_signed_cert()
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
    app.run(ssl_context=context, host="127.0.0.1", port=5000)
