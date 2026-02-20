# 🔐 Weighted Random Password Generator

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Stars](https://img.shields.io/github/stars/yourusername/password-generator?style=social)
![Forks](https://img.shields.io/github/forks/yourusername/password-generator?style=social)

A **secure and customizable password generator** built in Python that creates **strong, random passwords** with letters, numbers, and symbols. Perfect for **portfolio projects, learning Python, or real-world use**.  

This generator uses **weighted probabilities** to control character frequency, making passwords **both secure and human-friendly**.

---

## ✨ Features

- 🔹 Generate passwords of **adjustable length** (default: 16 characters)  
- 🔹 **Weighted randomness:** Letters, numbers, and symbols appear based on assigned probabilities  
- 🔹 **Randomized letter casing:** Uppercase and lowercase letters appear unpredictably  
- 🔹 **Safe symbol selection:** Uses widely accepted symbols for maximum compatibility  
- 🔹 High-security output **resistant to brute-force attacks**  
- 🔹 Modular, easy-to-read Python code for learning or customization  

---

## ⚙️ How It Works

```text
Letters (a-z, A-Z)      Numbers (0-9)      Symbols (!@#$%^&*)
        │                      │                  │
        └─── Weighted Choice ──┘                  │
                │                                │
                └── Pick Random Character ───────┘
                            │
                   Random Upper/Lower Case
                            │
                     Repeat Until Length
````

Step-by-step:

1. Define **character sets**: letters, numbers, and symbols
2. Assign **weights** to each set to control their frequency
3. Randomly select a **character set** based on weights
4. Pick a **random character** from the chosen set
5. If the character is a letter, randomly **capitalize it**
6. Repeat until the password reaches the desired length

This ensures **strong randomness** while making passwords readable.

---

## 💻 Example Output

```
cfxlq1*d51h09_g5
XtWlN36N9U7pk23P
NNP(O92r0q7@IN^4
a29Ahg_#wjN61Lk*
```

---

## 🔒 Security Considerations

* Uses Python’s `random` module — good for learning and general use
* Can be upgraded to **`secrets` module** for cryptographic security
* Adjustable length and weights allow a **balance of strength and memorability**
* Recommended length: **16–20 characters** for strong passwords

---

## 🛠️ Potential Improvements

* ✅ Switch to **`secrets` module** for cryptographically secure passwords
* ✅ Enforce **at least one number and one symbol** per password
* ✅ Allow user-defined **custom character sets**
* ✅ Add **CLI or GUI interface** for easier usage

---

## 🧰 Technologies

* **Python 3.x**
* Standard libraries: `random`, `string`

---

## 🚀 Usage

1. Clone the repository:

```bash
git clone https://github.com/yourusername/password-generator.git
```

2. Navigate to the project folder:

```bash
cd password-generator
```

3. Run the generator:

```bash
python Lab1_intro.py
```

4. Copy the generated password for secure use 🔑

---

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 💡 Summary

This project demonstrates a **strong understanding of password security, randomness, and weighted probability**, making it an excellent addition to any **portfolio or GitHub showcase**.

