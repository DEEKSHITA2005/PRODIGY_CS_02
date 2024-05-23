from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    # Open the image
    img = Image.open(image_path)
    img_array = np.array(img)

    # Get image dimensions
    rows, cols, channels = img_array.shape

    # Apply encryption: Swap pixels and add key value
    encrypted_array = np.zeros_like(img_array)
    for i in range(rows):
        for j in range(cols):
            for c in range(channels):
                # Swap pixel values
                new_i, new_j = (i + key) % rows, (j + key) % cols
                encrypted_array[new_i, new_j, c] = (img_array[i, j, c] + key) % 256

    # Convert array back to image
    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.save(output_path)

def decrypt_image(encrypted_path, output_path, key):
    # Open the encrypted image
    encrypted_img = Image.open(encrypted_path)
    encrypted_array = np.array(encrypted_img)

    # Get image dimensions
    rows, cols, channels = encrypted_array.shape

    # Apply decryption: Reverse the encryption process
    decrypted_array = np.zeros_like(encrypted_array)
    for i in range(rows):
        for j in range(cols):
            for c in range(channels):
                # Reverse swap pixel values
                original_i, original_j = (i - key) % rows, (j - key) % cols
                decrypted_array[original_i, original_j, c] = (encrypted_array[i, j, c] - key) % 256

    # Convert array back to image
    decrypted_img = Image.fromarray(decrypted_array)
    decrypted_img.save(output_path)

# Example usage
if __name__ == "__main__":
    key = 10  # Simple integer key for encryption/decryption
    encrypt_image("input_image.jpg", "encrypted_image.png", key)
    decrypt_image("encrypted_image.png", "decrypted_image.jpg", key)
