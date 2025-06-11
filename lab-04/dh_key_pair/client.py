from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

# Load server's public key
with open("server_public_key.pem", "rb") as f:
    server_public_key = serialization.load_pem_public_key(f.read())

# Generate parameters from server's key
parameters = server_public_key.public_numbers().parameter_numbers
params = dh.DHParameterNumbers(parameters.p, parameters.g).parameters()

# Generate client's private key
client_private_key = params.generate_private_key()

# Generate client's public key
client_public_key = client_private_key.public_key()

# Compute shared secret
shared_key = client_private_key.exchange(server_public_key)

print("[Client] Shared key generated successfully.")
print("[Client] Shared secret (hex):", shared_key.hex())
