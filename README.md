# PRODIGY_WD_02 - Pixel Manipulation for Image Encryption

## 🔐 Description
This tool demonstrates a basic encryption technique using pixel-level manipulation on images. It uses a simple XOR cipher to allow both encryption and decryption using the same key.

## 🚀 How to Run
1. Install dependencies:
   ```bash
   pip install pillow
   ```

2. Run the script:
   ```bash
   python main.py
   ```

3. Input:
   - Path to the image
   - Output file name
   - A numeric key (0-255)

## 🧠 Encryption Method
Each RGB value of the pixel is XORed with the provided key:
```
(R, G, B) => (R^key, G^key, B^key)
```

## ✅ Features
- Image encryption and decryption
- Lightweight and fast
- Works with PNG/JPG files

## 🛠 Example
```
Input: your_image.png
Key: 42
Encrypted output: encrypted_image.png
```

## 📄 License
MIT
