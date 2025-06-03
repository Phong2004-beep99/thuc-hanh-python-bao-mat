from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere.vigenere_cipher import VigenereCipher
from cipher.railfence.railfence_cipher import RailFenceCipher
from cipher.playfair.playfair_cipher import PlayfairCipher
from cipher.transposition.transposition_cipher import TranspositionCipher





app = Flask(__name__)
caesar = CaesarCipher()
vigenere_cipher = VigenereCipher()
railfence_cipher = RailFenceCipher()
playfair_cipher = PlayfairCipher("HUTECH")  
trans_cipher = TranspositionCipher()




@app.route("/api/caesar/encrypt", methods=["POST"])
def encrypt():
    data = request.json
    plain_text = data["plain_text"]
    key = int(data["key"])
    encrypted = caesar.encrypt_text(plain_text, key)
    return jsonify({"encrypted_message": encrypted})

@app.route("/api/caesar/decrypt", methods=["POST"])
def decrypt():
    data = request.json
    cipher_text = data["cipher_text"]
    key = int(data["key"])
    decrypted = caesar.decrypt_text(cipher_text, key)
    return jsonify({"decrypted_message": decrypted})

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

@app.route("/api/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    data = request.json
    plain_text = data["plain_text"]
    encrypted = playfair_cipher.encrypt(plain_text)
    return jsonify({"encrypted_message": encrypted})

@app.route("/api/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    data = request.json
    cipher_text = data["cipher_text"]
    decrypted = playfair_cipher.decrypt(cipher_text)
    return jsonify({"decrypted_message": decrypted})

@app.route("/api/transposition/encrypt", methods=["POST"])
def trans_encrypt():
    data = request.json
    plain_text = data["plain_text"]
    key = int(data["key"])
    encrypted = trans_cipher.encrypt(plain_text, key)
    return jsonify({"encrypted_message": encrypted})

@app.route("/api/transposition/decrypt", methods=["POST"])
def trans_decrypt():
    data = request.json
    cipher_text = data["cipher_text"]
    key = int(data["key"])
    decrypted = trans_cipher.decrypt(cipher_text, key)
    return jsonify({"decrypted_message": decrypted})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
