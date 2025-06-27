# PassChecker
🔐 Check if your passwords have been exposed in data breaches using the "Have I Been Pwned" API. Simple SHA1-based checker in Python.

# Password Leak Checker 🔒

This Python script checks if your passwords have been exposed in known data breaches using the **Have I Been Pwned** API.

## 📂 How it Works

1. Reads passwords from a `password.txt` file.
2. Converts each password to a SHA1 hash.
3. Sends only the **first 5 characters** of the hash to the API (K-Anonymity).
4. Matches the rest of the hash locally.
5. Reports how many times each password has appeared in breaches.

## 🚀 Usage

1. Create a `password.txt` file with one password per line.
2. Run the script:

```bash
python your_script_name.py
📦 Requirements
Python 3

requests library (pip install requests)

⚠️ Warning
This tool does not share your full password online. It uses K-anonymity for privacy.
