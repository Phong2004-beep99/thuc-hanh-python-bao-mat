class RailFenceCipher:
    def __init__(self):
        pass

    def encrypt(self, text: str, rails: int) -> str:
        fence = [['' for _ in range(len(text))] for _ in range(rails)]
        rail = 0
        direction = 1

        for idx, char in enumerate(text):
            fence[rail][idx] = char
            rail += direction

            if rail == 0 or rail == rails - 1:
                direction *= -1

        result = ''.join([''.join(row) for row in fence])
        return result

    def decrypt(self, cipher_text: str, rails: int) -> str:
        fence = [['' for _ in range(len(cipher_text))] for _ in range(rails)]
        rail = 0
        direction = 1

        # Đánh dấu vị trí các ký tự
        for i in range(len(cipher_text)):
            fence[rail][i] = '*'
            rail += direction
            if rail == 0 or rail == rails - 1:
                direction *= -1

        # Điền các ký tự vào đúng vị trí
        idx = 0
        for r in range(rails):
            for c in range(len(cipher_text)):
                if fence[r][c] == '*' and idx < len(cipher_text):
                    fence[r][c] = cipher_text[idx]
                    idx += 1

        # Đọc lại văn bản giải mã
        result = []
        rail = 0
        direction = 1
        for i in range(len(cipher_text)):
            result.append(fence[rail][i])
            rail += direction
            if rail == 0 or rail == rails - 1:
                direction *= -1

        return ''.join(result)
