from PIL import Image
import sys

def encode_image(image_path, message, output_path):
    img = Image.open(image_path)
    encoded = img.copy()
    width, height = img.size
    index = 0

    # Chuyển thông điệp thành chuỗi nhị phân
    binary_message = ''.join(format(ord(c), '08b') for c in message)
    binary_message += '1111111111111110'  # EOF marker

    for row in range(height):
        for col in range(width):
            if index < len(binary_message):
                r, g, b = img.getpixel((col, row))
                r = (r & ~1) | int(binary_message[index])
                encoded.putpixel((col, row), (r, g, b))
                index += 1
            else:
                break

    encoded.save(output_path)
    print(f"Thông điệp đã được giấu vào ảnh '{output_path}'.")

if __name__ == "__main__":
    image_path = input("Nhập đường dẫn ảnh gốc (ví dụ: image.jpg): ")
    message = input("Nhập thông điệp cần giấu: ")
    output_path = "encoded_image.png"
    encode_image(image_path, message, output_path)
