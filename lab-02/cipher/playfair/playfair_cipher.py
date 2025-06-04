class PlayfairCipher:
    def __init__(self, key):
        self.matrix = self.generate_matrix(key)

    def generate_matrix(self, key):
        key = key.upper().replace('J', 'I')
        matrix = []
        used = set()
        for char in key:
            if char not in used and char.isalpha():
                used.add(char)
                matrix.append(char)
        for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
            if char not in used:
                matrix.append(char)
        return [matrix[i:i+5] for i in range(0, 25, 5)]

    def find_position(self, char):
        for i in range(5):
            for j in range(5):
                if self.matrix[i][j] == char:
                    return i, j
        return -1, -1

    def process_text(self, text):
        text = text.upper().replace('J', 'I')
        result = []
        i = 0
        while i < len(text):
            a = text[i]
            b = text[i+1] if i + 1 < len(text) else 'X'
            if a == b:
                result.append(a + 'X')
                i += 1
            else:
                result.append(a + b)
                i += 2
        return result

    def encrypt(self, text):
        pairs = self.process_text(text)
        cipher_text = ''
        for pair in pairs:
            a, b = pair[0], pair[1]
            row1, col1 = self.find_position(a)
            row2, col2 = self.find_position(b)
            if row1 == row2:
                cipher_text += self.matrix[row1][(col1 + 1) % 5]
                cipher_text += self.matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                cipher_text += self.matrix[(row1 + 1) % 5][col1]
                cipher_text += self.matrix[(row2 + 1) % 5][col2]
            else:
                cipher_text += self.matrix[row1][col2]
                cipher_text += self.matrix[row2][col1]
        return cipher_text

    def decrypt(self, text):
        pairs = self.process_text(text)
        plain_text = ''
        for pair in pairs:
            a, b = pair[0], pair[1]
            row1, col1 = self.find_position(a)
            row2, col2 = self.find_position(b)
            if row1 == row2:
                plain_text += self.matrix[row1][(col1 - 1) % 5]
                plain_text += self.matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                plain_text += self.matrix[(row1 - 1) % 5][col1]
                plain_text += self.matrix[(row2 - 1) % 5][col2]
            else:
                plain_text += self.matrix[row1][col2]
                plain_text += self.matrix[row2][col1]
        return plain_text

    
    def encrypt_text(self, text):
        return self.encrypt(text)

    def decrypt_text(self, text):
        return self.decrypt(text)
