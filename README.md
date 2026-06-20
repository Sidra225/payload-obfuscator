# Payload Obfuscation Tool 🔐

An educational Python tool that demonstrates how layered encoding techniques 
work to modify payload signatures — for understanding AV evasion concepts.

> ⚠️ **Disclaimer**: This tool is strictly for educational purposes. 
> It is intended to help cybersecurity students understand how encoding 
> works at a byte level. Do not use against any system without explicit permission.

---

## 🔧 Techniques Implemented

| Technique | Description |
|---|---|
| XOR Encoding | Flips every byte using a numeric key |
| Caesar Byte Shift | Shifts every byte value by a fixed amount |
| Base64 Encoding | Converts binary data into readable text |

---

## 📁 Project Structure 

payload-obfuscator/

├── obfuscator.py        # Main encoding tool

├── deobfuscator.py      # Reverses the encoding

├── techniques/

│   ├── xor_encode.py    # XOR encode/decode

│   ├── base64_layer.py  # Base64 encode/decode

│   └── caesar_shift.py  # Caesar shift encode/decode

├── samples/

│   └── test_payload.txt # Dummy test input

└── README.md
---

## How It Works

Input → XOR Encode → Caesar Shift → Base64 → Obfuscated Output

↓

Original Output ← XOR Decode ← Caesar Decode ← Base64 Decode

Each encoding layer changes the byte signature of the input, 
demonstrating why simple signature-based AV detection can be bypassed.

---

##  Usage

**Obfuscate:**
```bash
python obfuscator.py samples/test_payload.txt --xor-key 65 --shift 13
```

**Deobfuscate:**
```bash
python deobfuscator.py obfuscated.txt --xor-key 65 --shift 13
```

---

## Defensive Takeaway

Blue teamers can detect obfuscated payloads by:
- **Entropy analysis** — encoded content has unusually high entropy
- **Behavioral detection** — monitor execution, not just signatures
- **Heuristic scanning** — flag files with multiple encoding layers


