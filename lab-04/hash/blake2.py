import hashlib

def get_blake2_hash(message):
    blake2 = hashlib.blake2b()
    blake2.update(message.encode())
    return blake2.hexdigest()

if __name__ == "__main__":
    message = input("Nhập chuỗi cần băm (BLAKE2b): ")
    print("BLAKE2b Hash:", get_blake2_hash(message))
