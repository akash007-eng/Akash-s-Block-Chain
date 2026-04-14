from flask import Flask, request, jsonify, send_from_directory
from blockchain_connect import contract, w3, account
import hashlib
import os

app = Flask(__name__, static_folder='Frontend', static_url_path='')

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ✅ Serve frontend
@app.route('/')
def home():
    return send_from_directory('Frontend', 'index.html')


# ✅ Upload API
@app.route('/upload', methods=['POST'])
def upload():
    try:
        file = request.files['file']

        if not file:
            return jsonify({"error": "No file uploaded"}), 400

        # Save file in uploads folder
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        # Read file
        with open(file_path, "rb") as f:
            file_data = f.read()

        # Generate hash
        file_hash = hashlib.sha256(file_data).hexdigest()

        print("Generated Hash:", file_hash)

        # Store hash in blockchain
        tx = contract.functions.storeHash(file_hash).transact({
            'from': account
        })

        receipt = w3.eth.wait_for_transaction_receipt(tx)

        print("Transaction Hash:", receipt.transactionHash.hex())

        return jsonify({
            "message": "File stored successfully",
            "hash": file_hash,
            "filename": file.filename
        })

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": str(e)}), 500


# ✅ Verify API
@app.route('/verify', methods=['POST'])
def verify():
    try:
        file = request.files['file']

        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        with open(file_path, "rb") as f:
            file_data = f.read()

        computed_hash = hashlib.sha256(file_data).hexdigest()

        count = contract.functions.getFileCount().call()

        if count == 0:
            return jsonify({"error": "No files on blockchain"}), 400

        stored_data = contract.functions.getFile(count - 1).call()
        stored_hash = stored_data[0]

        return jsonify({
            "computed_hash": computed_hash,
            "stored_hash": stored_hash,
            "status": "Authentic" if computed_hash == stored_hash else "Tampered"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ✅ Download API (REAL WORKING)
@app.route('/download', methods=['POST'])
def download():
    try:
        data = request.get_json()
        input_hash = data.get("hash")

        # Find matching file in uploads
        for filename in os.listdir(UPLOAD_FOLDER):
            file_path = os.path.join(UPLOAD_FOLDER, filename)

            with open(file_path, "rb") as f:
                file_data = f.read()

            file_hash = hashlib.sha256(file_data).hexdigest()

            if file_hash == input_hash:
                return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

        return jsonify({"error": "File not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ✅ Run server
if __name__ == "__main__":
    app.run(debug=True)