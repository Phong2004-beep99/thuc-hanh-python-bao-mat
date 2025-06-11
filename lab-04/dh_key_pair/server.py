from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

# Generate DH parameters
parameters = dh.generate_parameters(generator=2, key_size=2048)

# Generate server's private key
private_key = parameters.generate_private_key()

# Get server's public key
public_key = private_key.public_key()

# Serialize server's public key and save to file
with open("server_public_key.pem", "wb") as f:
    f.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))

print("[Server] Public key generated and saved to server_public_key.pem")
