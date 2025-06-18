from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayfairCipher

app = Flask(__name__)

caesar = CaesarCipher()
vigenere = VigenereCipher()
railfence = RailFenceCipher()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/caesar", methods=["GET", "POST"])
def caesar_page():
    result = ""
    if request.method == "POST":
        if "inputPlainText" in request.form:  # Encrypt
            text = request.form["inputPlainText"]
            key = int(request.form["inputKeyPlain"])
            result = caesar.encrypt_text(text, key)
        elif "inputCipherText" in request.form:  # Decrypt
            text = request.form["inputCipherText"]
            key = int(request.form["inputKeyCipher"])
            result = caesar.decrypt_text(text, key)
    return render_template("caesar.html", result=result)

@app.route("/vigenere", methods=["GET", "POST"])
def vigenere_page():
    result = ""
    if request.method == "POST":
        if "inputPlainText" in request.form:
            text = request.form["inputPlainText"]
            key = request.form["inputKeyPlain"]
            result = vigenere.encrypt_text(text, key)
        elif "inputCipherText" in request.form:
            text = request.form["inputCipherText"]
            key = request.form["inputKeyCipher"]
            result = vigenere.decrypt_text(text, key)
    return render_template("vigenere.html", result=result)

@app.route("/railfence", methods=["GET", "POST"])
def railfence_page():
    result = ""
    if request.method == "POST":
        if "inputPlainText" in request.form:
            text = request.form["inputPlainText"]
            key = int(request.form["inputKeyPlain"])
            result = railfence.encrypt_text(text, key)
        elif "inputCipherText" in request.form:
            text = request.form["inputCipherText"]
            key = int(request.form["inputKeyCipher"])
            result = railfence.decrypt_text(text, key)
    return render_template("railfence.html", result=result)

@app.route("/playfair", methods=["GET", "POST"])
def playfair_page():
    result = ""
    if request.method == "POST":
        if "inputPlainText" in request.form:
            text = request.form["inputPlainText"]
            key = request.form["inputKeyPlain"]
            cipher = PlayfairCipher(key)
            result = cipher.encrypt_text(text)
        elif "inputCipherText" in request.form:
            text = request.form["inputCipherText"]
            key = request.form["inputKeyCipher"]
            cipher = PlayfairCipher(key)
            result = cipher.decrypt_text(text)
    return render_template("playfair.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
