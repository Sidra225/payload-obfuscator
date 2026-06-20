import argparse
from techniques.xor_encode import xor_decode
from techniques.base64_layer import b64_decode
from techniques.caesar_shift import caesar_decode

def deobfuscate(data: bytes, xor_key: int, caesar_shift: int) -> bytes:
    step1 = b64_decode(data)
    step2 = caesar_decode(step1, caesar_shift)
    step3 = xor_decode(step2, xor_key)
    return step3

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Obfuscated file path")
    parser.add_argument("--xor-key", type=int, default=65)
    parser.add_argument("--shift", type=int, default=13)
    parser.add_argument("--output", default="recovered.txt")
    args = parser.parse_args()

    with open(args.input, "rb") as f:
        data = f.read()

    result = deobfuscate(data, args.xor_key, args.shift)

    with open(args.output, "wb") as f:
        f.write(result)

    print(f"[+] Recovered! Saved to {args.output}")

if __name__ == "__main__":
    main()