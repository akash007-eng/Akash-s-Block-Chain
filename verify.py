from blockchain_connect import contract
import hashlib

file_path = "sample.txt"

# Read encrypted file
with open(file_path + ".enc", "rb") as f:
    encrypted_data = f.read()

computed_hash = hashlib.sha256(encrypted_data).hexdigest()

# Get latest file index
count = contract.functions.getFileCount().call()

stored_data = contract.functions.getFile(count - 1).call()
stored_hash = stored_data[0]

print("Computed Hash:", computed_hash)
print("Stored Hash:", stored_hash)

if computed_hash == stored_hash:
    print("✅ File is Authentic")
else:
    print("❌ File is Tampered")