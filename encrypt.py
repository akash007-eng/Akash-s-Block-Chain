from cryptography.fernet import Fernet

def encrypt_file(file_path):
    key = Fernet.generate_key()
    cipher = Fernet(key)

    with open(file_path, "rb") as f:
        data = f.read()

    encrypted = cipher.encrypt(data)

    with open(file_path + ".enc", "wb") as f:
        f.write(encrypted)

    return key