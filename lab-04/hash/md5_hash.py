import hashlib

def get_md5_hash(message):
    md5 = hashlib.md5()
    md5.update(message.encode())
    return md5.hexdigest()

if __name__ == "__main__":
    message = input("Nhập chuỗi cần băm (MD5): ")
    print("MD5 Hash:", get_md5_hash(message))
