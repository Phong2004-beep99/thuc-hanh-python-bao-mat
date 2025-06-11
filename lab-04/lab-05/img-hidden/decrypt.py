from PIL import Image

def decode_image(image_path):
    img = Image.open(image_path)
    width, height = img.size
    binary_data = ''
    
    for row in range(height):
        for col in range(width):
            r, g, b = img.getpixel((col, row))
            binary_data += str(r & 1)

    # Chuyển chuỗi nhị phân thành ký tự
    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    decoded_message = ''
    for byte in all_bytes:
        if byte == '11111110':  # EOF marker
            break
        decoded_message += chr(int(byte, 2))

    print("Thông điệp được giấu là:", decoded_message)

if __name__ == "__main__":
    image_path = input("Nhập đường dẫn ảnh mã hóa (ví dụ: encoded_image.png): ")
    decode_image(image_path)
