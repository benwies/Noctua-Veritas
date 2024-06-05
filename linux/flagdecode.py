def decode_key(encoded):
    decoded = ""
    for char in encoded:
        decoded += chr(ord(char) - 1) 
    return decoded

encoded_key = "uftu"

decoded_key = decode_key(encoded_key)

print("Decoded key:", decoded_key)
