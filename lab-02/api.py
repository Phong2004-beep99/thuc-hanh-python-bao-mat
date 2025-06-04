from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere.vigenere_cipher import VigenereCipher
from cipher.railfence.railfence_cipher import RailFenceCipher
from cipher.playfair.playfair_cipher import PlayfairCipher

app = Flask(__name__)

# Khởi tạo các đối tượng cố định (ngoại trừ Playfair phải khởi tạo theo key người dùng)
caesar = CaesarCipher()
vigenere_cipher = VigenereCipher()
railfence_cipher = RailFenceCipher()

# Caesar Cipher
@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data["plain_text"]
    key = int(data["key"])
    encrypted = caesar.encrypt_text(plain_text, key)
    return jsonify({"encrypted_message": encrypted})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data["cipher_text"]
    key = int(data["key"])
    decrypted = caesar.decrypt_text(cipher_text, key)
    return jsonify({"decrypted_message": decrypted})


# Vigenère Cipher
@app.route("/api/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    data = request.json
    plain_text = data["plain_text"]
    key = data["key"]
    encrypted = vigenere_cipher.encrypt(plain_text, key)
    return jsonify({"encrypted_message": encrypted})

@app.route("/api/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    data = request.json
    cipher_text = data["cipher_text"]
    key = data["key"]
    decrypted = vigenere_cipher.decrypt(cipher_text, key)
    return jsonify({"decrypted_message": decrypted})


# Rail Fence Cipher
@app.route("/api/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    data = request.json
    plain_text = data["plain_text"]
    key = int(data["key"])
    encrypted = railfence_cipher.encrypt(plain_text, key)
    return jsonify({"encrypted_message": encrypted})

@app.route("/api/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    data = request.json
    cipher_text = data["cipher_text"]
    key = int(data["key"])
    decrypted = railfence_cipher.decrypt(cipher_text, key)
    return jsonify({"decrypted_message": decrypted})


# Playfair Cipher (khởi tạo mỗi lần theo key người dùng)
@app.route("/api/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    data = request.json
    plain_text = data["plain_text"]
    key = data["key"]
    cipher = PlayfairCipher(key)
    encrypted = cipher.encrypt(plain_text)
    return jsonify({"encrypted_message": encrypted})

@app.route("/api/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    data = request.json
    cipher_text = data["cipher_text"]
    key = data["key"]
    cipher = PlayfairCipher(key)
    decrypted = cipher.decrypt(cipher_text)
    return jsonify({"decrypted_message": decrypted})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
