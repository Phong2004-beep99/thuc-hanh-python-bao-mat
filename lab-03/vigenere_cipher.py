import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.vigenere import Ui_MainWindow
import requests

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "./platforms"

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def is_valid_input(self, text):
        return text.isalpha()

    def show_error(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Lỗi nhập liệu")
        msg.setText(message)
        msg.exec_()

    def call_api_encrypt(self):
        plain_text = self.ui.txt_plain_text.toPlainText()
        key = self.ui.txt_key.text()

        if not self.is_valid_input(plain_text):
            self.show_error("Plain Text chỉ được chứa chữ cái A–Z, không có số hoặc ký tự đặc biệt.")
            return
        if not self.is_valid_input(key):
            self.show_error("Key chỉ được chứa chữ cái A–Z.")
            return

        url = "http://127.0.0.1:5000/api/vigenere/encrypt"
        payload = {
            "plain_text": plain_text,
            "key": key
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher_text.setText(data["encrypted_message"])
        except Exception as e:
            print("LỖI GỌI API:", e)

    def call_api_decrypt(self):
        cipher_text = self.ui.txt_cipher_text.toPlainText()
        key = self.ui.txt_key.text()

        if not self.is_valid_input(cipher_text):
            self.show_error("Cipher Text chỉ được chứa chữ cái A–Z.")
            return
        if not self.is_valid_input(key):
            self.show_error("Key chỉ được chứa chữ cái A–Z.")
            return

        url = "http://127.0.0.1:5000/api/vigenere/decrypt"
        payload = {
            "cipher_text": cipher_text,
            "key": key
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain_text.setText(data["decrypted_message"])
        except Exception as e:
            print("LỖI GỌI API:", e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
