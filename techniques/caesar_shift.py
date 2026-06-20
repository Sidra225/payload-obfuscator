def caesar_encode(data: bytes, shift: int) -> bytes:
    return bytes([(b + shift) % 256 for b in data])

def caesar_decode(data: bytes, shift: int) -> bytes:
    return bytes([(b - shift) % 256 for b in data])