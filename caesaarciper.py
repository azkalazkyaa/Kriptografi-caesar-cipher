def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            if is_upper:
                shifted_char = shifted_char.upper()
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            if is_upper:
                shifted_char = shifted_char.upper()
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text

text = input('masukan kata deskripsi : ')
shift = 3

encrypted_text = caesar_encrypt(text, shift)
decrypted_text = caesar_decrypt(encrypted_text, shift)

print("Teks Terenkripsi: ", encrypted_text)
