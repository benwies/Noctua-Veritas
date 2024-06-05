def encode_key(key):
    encoded = ""
    for char in key:
        encoded += chr(ord(char) + 1) 
    return encoded

original_key = "test"

encoded_key = encode_key(original_key)

print("Obfuscated key:", encoded_key)
