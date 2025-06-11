# lab-04/lab-05/img-hidden/img_handler.py

from PIL import Image

def set_lsb(image, bits):
    img = image.copy()
    width, height = img.size
    index = 0

    for y in range(height):
        for x in range(width):
            if index < len(bits):
                r, g, b = img.getpixel((x, y))
                r = (r & ~1) | int(bits[index])
                img.putpixel((x, y), (r, g, b))
                index += 1
            else:
                return img
    return img

def get_lsb(image):
    bits = ''
    width, height = image.size
    for y in range(height):
        for x in range(width):
            r, g, b = image.getpixel((x, y))
            bits += str(r & 1)
    return bits
