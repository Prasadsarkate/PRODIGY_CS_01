# 🔐 Caesar Cipher — PRODIGY_CS_01

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)
![Internship](https://img.shields.io/badge/Prodigy-InfoTech-purple?style=for-the-badge)

> **Task 01** — Prodigy InfoTech Cyber Security Internship

---

## 📌 Task Description

Create a Python program that can **encrypt and decrypt text** using the Caesar Cipher algorithm. Allow users to input a message and a shift value to perform encryption and decryption.

---

## 🔍 What is Caesar Cipher?

Caesar Cipher is one of the **oldest and simplest encryption techniques**. It works by shifting each letter in the plaintext by a fixed number of positions in the alphabet.

```
Original : H  E  L  L  O
Shift    : 3
Encrypted: K  H  O  O  R
```

- **Encryption** → shift letters forward
- **Decryption** → shift letters backward (same key)

---

## ✨ Features

- ✅ Encrypt any text message
- ✅ Decrypt any encrypted message
- ✅ Supports uppercase & lowercase letters
- ✅ Preserves spaces, numbers & special characters
- ✅ Input validation for shift value (0–25)
- ✅ Simple menu-driven interface

---

## 🛠️ Requirements

- Python 3.x
- No external libraries needed!

---

## ▶️ How to Run

```bash
# Clone the repository
git clone https://github.com/Prasadsarkate/PRODIGY_CS_01.git

# Navigate to folder
cd PRODIGY_CS_01

# Run the program
python caesar_cipher.py
```

---

## 💻 Usage Example

```
=============================================
        🔐 Caesar Cipher Program
=============================================

Options:
  1. Encrypt a message
  2. Decrypt a message
  3. Exit

Enter your choice (1/2/3): 1
Enter the message to encrypt: Hello World
Enter shift value (0-25): 3

✅ Encrypted Message: Khoor Zruog
```

```
Enter your choice (1/2/3): 2
Enter the message to decrypt: Khoor Zruog
Enter shift value (0-25): 3

✅ Decrypted Message: Hello World
```

---

## 🧠 How It Works

```python
# Core logic
def caesar_cipher(text, shift, mode='encrypt'):
    if mode == 'decrypt':
        shift = -shift
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26
            result.append(chr(base + shifted))
```

| Step | Action |
|------|--------|
| 1 | Take each character of the message |
| 2 | Check if it's a letter (skip others) |
| 3 | Shift it by key value using ASCII |
| 4 | Wrap around Z → A using modulo 26 |

---

## 📂 Project Structure

```
PRODIGY_CS_01/
│
├── caesar_cipher.py    # Main program
└── README.md           # Project documentation
```

---

## 📚 What I Learned

- Basics of **symmetric encryption**
- Working with **ASCII values** in Python
- How classical ciphers work in **cryptography**
- Building **menu-driven CLI** applications

---

## 👨‍💻 Author

**Prasad** — Cyber Security Intern @ Prodigy InfoTech

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://linkedin.com/in/prasadsarkate)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat&logo=github)](https://github.com/Prasadsarkate)

---

## 🏢 Internship

This project was completed as part of the **Prodigy InfoTech Cyber Security Internship**.

`#ProdigyInfoTech` `#Internship` `#CyberSecurity` `#Python` `#Cryptography`
