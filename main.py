from PIL import Image 
import os

def encrypt_decrypt_image(input_path, output_path, key):
    try:
        image = Image.open(input_path)
        image = image.convert("RGB")
        pixels = image.load()

        width, height = image.size
        for i in range(width):
            for j in range(height):
                r, g, b = pixels[i, j]
                pixels[i, j] = (r ^ key, g ^ key, b ^ key)

        image.save(output_path)
        print(f"Success: Output saved to '{output_path}'")
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("=== Image Encryption/Decryption Tool ===")
    input_path = input("Enter image file path: ")
    output_path = input("Enter output file name (e.g. encrypted.png): ")
    try:
        key = int(input("Enter encryption/decryption key (0-255): "))
        if not (0 <= key <= 255):
            raise ValueError("Key must be between 0 and 255")
    except ValueError as e:
        print(f"Invalid key: {e}")
        return

    encrypt_decrypt_image(input_path, output_path, key)

if __name__ == "__main__":
    main()
