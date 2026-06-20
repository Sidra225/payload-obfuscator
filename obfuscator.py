import argparse
from techniques.xor_encode import xor_encode
from techniques.base64_layer import b64_encode
from techniques.caesar_shift import caesar_encode

def obfuscate(payload: bytes, xor_key: int, caesar_shift: int) -> bytes:
    step1 = xor_encode(payload, xor_key)
    step2 = caesar_encode(step1, caesar_shift)
    step3 = b64_encode(step2)
    return step3

def main():
    parser = argparse.ArgumentParser(description="Payload Obfuscation Tool - Educational")
    parser.add_argument("input", help="Input file path")
    parser.add_argument("--xor-key", type=int, default=65)
    parser.add_argument("--shift", type=int, default=13)
    parser.add_argument("--output", default="obfuscated.txt")
    args = parser.parse_args()

    with open(args.input, "rb") as f:
        payload = f.read()

    result = obfuscate(payload, args.xor_key, args.shift)

    with open(args.output, "wb") as f:
        f.write(result)

    print(f"[+] Done! Saved to {args.output}")
    print(f"[+] XOR key used: {args.xor_key} | Caesar shift: {args.shift}")

if __name__ == "__main__":
    main()