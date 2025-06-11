# lab-04/lab-05/img-hidden/main.py

from PIL import Image
from bit_tools import text_to_bits, bits_to_text
from img_handler import set_lsb, get_lsb

if __name__ == "__main__":
    while True:
        print("\n=== MENU ===")
        print("1. Giấu tin vào ảnh")
        print("2. Giải mã ảnh")
        print("0. Thoát")

        choice = input("Chọn: ")

        if choice == "1":
            path = input("Nhập ảnh gốc (image.jpg): ")
            message = input("Nhập thông điệp cần giấu: ")
            output = "encoded.png"

            img = Image.open(path)
            bits = text_to_bits(message + chr(254))  # EOF = 11111110
            encoded_img = set_lsb(img, bits)
            encoded_img.save(output)
            print(f"Đã lưu ảnh mã hóa tại: {output}")

        elif choice == "2":
            path = input("Nhập ảnh mã hóa (encoded.png): ")
            img = Image.open(path)
            bits = get_lsb(img)

            byte_list = [bits[i:i+8] for i in range(0, len(bits), 8)]
            message = ""
            for b in byte_list:
                if b == "11111110":  # EOF
                    break
                message += chr(int(b, 2))

            print("Thông điệp đã giấu:", message)

        elif choice == "0":
            break
        else:
            print("Lựa chọn không hợp lệ.")
