from string import ascii_uppercase

ALPHABET = list(ascii_uppercase)

class VigenereCipher:
    def __init__(self):
        self.alphabet = ALPHABET

    def _extend_key(self, text, key):
        key = key.upper()
        repeats = len(text) // len(key) + 1
        return (key * repeats)[:len(text)]

    def encrypt(self, text: str, key: str) -> str:
        text = text.upper()
        extended_key = self._extend_key(text, key)
        encrypted = []

        for i in range(len(text)):
            if text[i] in self.alphabet:
                t_idx = self.alphabet.index(text[i])
                k_idx = self.alphabet.index(extended_key[i])
                encrypted_char = self.alphabet[(t_idx + k_idx) % 26]
                encrypted.append(encrypted_char)
            else:
                encrypted.append(text[i])  # giữ nguyên ký tự đặc biệt

        return "".join(encrypted)

    def decrypt(self, cipher_text: str, key: str) -> str:
        cipher_text = cipher_text.upper()
        extended_key = self._extend_key(cipher_text, key)
        decrypted = []

        for i in range(len(cipher_text)):
            if cipher_text[i] in self.alphabet:
                c_idx = self.alphabet.index(cipher_text[i])
                k_idx = self.alphabet.index(extended_key[i])
                decrypted_char = self.alphabet[(c_idx - k_idx + 26) % 26]
                decrypted.append(decrypted_char)
            else:
                decrypted.append(cipher_text[i])

        return "".join(decrypted)
