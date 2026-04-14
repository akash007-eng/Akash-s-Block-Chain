from Crypto.Cipher import AES

def decrypt_file(enc_path, key):
    with open(enc_path, 'rb') as f:
        nonce = f.read(16)
        tag = f.read(16)
        ciphertext = f.read()

    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)

    with open("decrypted_file", 'wb') as f:
        f.write(data)
