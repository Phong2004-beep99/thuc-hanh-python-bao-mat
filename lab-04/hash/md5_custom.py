# lab-04/hash/md5_custom.py

def left_rotate(x, amount):
    x &= 0xFFFFFFFF
    return ((x << amount) | (x >> (32 - amount))) & 0xFFFFFFFF

def md5(message):
    import struct

    s = [7, 12, 17, 22] * 4 + [5, 9, 14, 20] * 4 + [4, 11, 16, 23] * 4 + [6, 10, 15, 21] * 4
    K = [int(abs(__import__('math').sin(i + 1)) * 2**32) & 0xFFFFFFFF for i in range(64)]

    msg_bytes = bytearray(message, 'utf-8')
    orig_len_bits = (8 * len(msg_bytes)) & 0xffffffffffffffff
    msg_bytes.append(0x80)
    while len(msg_bytes) % 64 != 56:
        msg_bytes.append(0)
    msg_bytes += orig_len_bits.to_bytes(8, byteorder='little')

    a0 = 0x67452301
    b0 = 0xefcdab89
    c0 = 0x98badcfe
    d0 = 0x10325476

    for chunk_offset in range(0, len(msg_bytes), 64):
        a, b, c, d = a0, b0, c0, d0
        chunk = msg_bytes[chunk_offset:chunk_offset + 64]
        M = list(struct.unpack('<16I', chunk))

        for i in range(64):
            if 0 <= i <= 15:
                f = (b & c) | (~b & d)
                g = i
            elif 16 <= i <= 31:
                f = (d & b) | (~d & c)
                g = (5*i + 1) % 16
            elif 32 <= i <= 47:
                f = b ^ c ^ d
                g = (3*i + 5) % 16
            else:
                f = c ^ (b | ~d)
                g = (7*i) % 16

            f = (f + a + K[i] + M[g]) & 0xFFFFFFFF
            a, d, c, b = d, c, b, (b + left_rotate(f, s[i])) & 0xFFFFFFFF

        a0 = (a0 + a) & 0xFFFFFFFF
        b0 = (b0 + b) & 0xFFFFFFFF
        c0 = (c0 + c) & 0xFFFFFFFF
        d0 = (d0 + d) & 0xFFFFFFFF

    result = sum(x << (32 * i) for i, x in enumerate([a0, b0, c0, d0]))
    return '{:032x}'.format(result)

if __name__ == "__main__":
    message = input("Nhập chuỗi cần băm (Tự cài MD5): ")
    print("MD5 Hash (custom):", md5(message))
