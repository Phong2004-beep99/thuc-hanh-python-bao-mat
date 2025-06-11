from Crypto.Hash import SHA3_256

def get_sha3_hash(message):
    hash_obj = SHA3_256.new()
    hash_obj.update(message.encode())
    return hash_obj.hexdigest()

if __name__ == "__main__":
    message = input("Nhập chuỗi cần băm (SHA3-256): ")
    print("SHA3-256 Hash:", get_sha3_hash(message))
