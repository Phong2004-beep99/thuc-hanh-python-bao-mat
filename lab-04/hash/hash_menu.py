# lab-04/hash/hash_menu.py

import md5_hash
import md5_custom
import sha3
import blake2

def menu():
    while True:
        print("\n===== MENU HASH =====")
        print("1. MD5 (hashlib)")
        print("2. MD5 (tự cài)")
        print("3. SHA3-256")
        print("4. BLAKE2b")
        print("0. Thoát")

        choice = input("Chọn hàm băm: ")

        if choice == "1":
            md5_hash.main()
        elif choice == "2":
            md5_custom.main()
        elif choice == "3":
            sha3.main()
        elif choice == "4":
            blake2.main()
        elif choice == "0":
            break
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    menu()
