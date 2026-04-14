# 🔐 Blockchain-Based Secure File Sharing System

A secure file sharing platform leveraging Blockchain technology, AES encryption, and SHA-256 hashing to ensure data confidentiality, integrity, and tamper-proof verification using a decentralized architecture.

---

## 🚀 Features
- 🔒 AES-based file encryption & decryption
- 🔑 SHA-256 hashing for integrity verification
- ⛓️ Blockchain storage for tamper-proof records
- 🌐 Decentralized file validation
- 📁 Secure upload & download system
- 🧾 Hash comparison for authenticity check

---

## 🛠️ Technologies Used
| Category | Technologies |
|----------|--------------|
| 💻 **Frontend** | HTML, CSS, JavaScript |
| ⚙️ **Backend** | Python (Flask) |
| 🔗 **Blockchain** | Ganache (Local Blockchain), Web3.py |
| 🔐 **Security** | AES Encryption, SHA-256 Hashing |
| 🗄️ **Database** | SQLite |
| 🧰 **Tools** | Ganache, MetaMask (optional), VS Code, Git & GitHub |

---

## 📂 Project Structure
SecureFileSharing/
│
├── Frontend/                # UI files
├── blockchain/              # Smart contracts
├── uploads/                 # Uploaded files
├── __pycache__/             # Python cache
│
├── auth.py                  # Authentication
├── upload.py                # Upload logic
├── download.py              # Download logic
├── encrypt.py               # AES encryption
├── decrypt.py               # AES decryption
├── verify.py                # Hash verification
├── blockchain_connect.py    # Blockchain interaction
│
├── users.db                 # Database
├── requirements.txt         # Dependencies
└── README.md                # Project documentation

⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/akash007-eng/Akash-s-Block-Chain.git
cd SecureFileSharing
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Start Ganache
Open Ganache
Start local blockchain
Copy RPC URL (usually: http://127.0.0.1:7545)
4️⃣ Run Application
python auth.py
5️⃣ Open in Browser
http://127.0.0.1:5000

🔄 Workflow
Upload file
File is encrypted using AES
Hash is generated using SHA-256
Hash stored on Blockchain
During download → hash is verified
File decrypted and provided if valid

👨‍💻 Authors
Akash Koka
GitHub: https://github.com/akash007-eng
