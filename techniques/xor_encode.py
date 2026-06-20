def xor_encode(data: bytes, key: int) -> bytes:
    return bytes([b ^ key for b in data])

def xor_decode(data: bytes, key: int) -> bytes:
    return xor_encode(data, key)