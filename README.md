# 🔐 Password Hash Cracking with John the Ripper

This project demonstrates **password strength testing and hash cracking** using **John the Ripper** in **Kali Linux**.
It includes scripts for generating weak and strong password hashes, testing them against a cracking tool, and analyzing the results.

---

## 📂 Project Structure

```
.
├── weak_hashes.txt          # Weak password hashes
├── strong_hashes.txt        # Stronger password hashes
├── crack_weak_reults        # Result of weak password cracking by Jtr
├── crack_strong_reults      # Result of strong password cracking by Jtr
├── make_hashes.py           # Python script to extract only hashes
├── Screenshot.png           # Screenshot of kali linux
└── README.md                # Documentation
```

---

## ⚡ Features

* Generate weak and strong password hashes using Python.
* Separate username-hash pairs and raw hash-only files.
* Crack weak hashes using **John the Ripper**.
* Demonstrates how weak passwords are easily broken compared to strong ones.

---

## 🛠️ Tools & Technologies

* **Python** (for generating and formatting hashes)
* **John the Ripper (JtR)** (for cracking)
* **Kali Linux** (testing environment)
* **VirtualBox/VMware** (optional, for running Kali VM)

---

## 📜 Usage

### 1️⃣ Generate Hash Files

Run the Python script to generate both weak and strong hashes:

```bash
python3 make_hashes.py
```

This creates:

* `weak_hashes.txt`
* `strong_hashes.txt`

### 3️⃣2️⃣ Crack Weak Hashes with John

Run John on the weak hashes:

```bash
john --wordlist=/usr/share/wordlists/rockyou.txt weak_only_hashes.txt
```

View cracked results:

```bash
john --show weak_only_hashes.txt
```

Expected output (example):

```
weak_user1:123456
weak_user2:password
weak_user3:qwerty
...
```

---

## 📸 Screenshots

<img width="1590" height="760" alt="Screenshot_2025-08-25_19_35_07" src="https://github.com/user-attachments/assets/bc071e60-f610-4b7a-b771-d2dd8d1b3ab8" />


---

## 🔍 Learning Outcomes

* Difference between **weak** and **strong** password security.
* How **hash cracking tools** like John the Ripper work.
* Why **secure password policies** are critical.
* Practical experience with **hash formats, cracking wordlists, and VM file sharing**.

---

## 🚀 Future Improvements

* Add support for **SHA-256, SHA-512** hashes.
* Implement **rainbow table attacks**.
* Create a **web-based dashboard** to visualize cracking results.

---

## 👨‍💻 Author

**Daksh Sharma**

* 🎓 Information Technology & Engineering, MAIT Delhi
* 🌐 Passionate about Cybersecurity & Web Development
* ⚡ Exploring password security & ethical hacking tools
