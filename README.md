# 🎓 Student Lab Portfolio — BCA AI (2026 Batch)

**Student Name:** YASHVI  
**Roll Number:** `2610997694`  
**Section:** Section G  
**Batch:** BCA AI 2026 Batch  
**Repository:** `sec-g-2610997694-yashvi`  

---

## 🚀 Initial Setup (One-time only)

When you start for the first time, open your terminal (Command Prompt, PowerShell, or Git Bash) and clone this repository to your laptop/system:

```bash
git clone https://github.com/chitkara-bca-ai-2026/sec-g-2610997694-yashvi.git
```
*(After cloning, open the cloned folder in VS Code via **File → Open Folder**)*

---

## 📂 Repository Structure

This repository is your central coursework portfolio across lab courses. Keep your work organized inside their respective subject folders:

* **`Python/`** — Python Programming lab assignments and solutions.
* **`CST/`** — Client Side Technology (HTML, CSS, JS) lab exercises.

```text
sec-g-2610997694-yashvi/
├── README.md
│
├── Python/                                  <--- [Python Programming]
│   ├── Lab_01/
│   │   └── solution.py                      (No log needed for past labs)
│   ├── ...
│   ├── Lab_13/
│   │   ├── solution.py                      (Python program)
│   │   └── log.txt                          (Error & reflection log - Python only)
│   └── Lab_14/
│       ├── solution.py
│       └── log.txt
│
└── CST/                                     <--- [Client Side Technologies]
    ├── Lab_01/
    │   ├── html/
    │   │   └── index.html                   (HTML files inside html/)
    │   └── images/
    │       └── banner.png                   (Images inside images/)
    └── Lab_02/
        ├── html/
        │   └── index.html
        └── images/
            └── logo.png
```

---

## 📝 Learning & Error Log (`log.txt`) — Python Labs Only (Lab 13 Onwards)

> ⚠️ **Note:** `log.txt` is strictly required for **Python** labs starting from Lab 13. Your **CST** labs do **not** require a `log.txt` (unless your CST teacher asks for one).

For each Python lab (starting Lab 13), create a simple Notepad text file named **`log.txt`** inside that lab's folder (`Python/Lab_XX/log.txt`).

Write casually in plain words just like rough notes—record your honest thoughts, any syntax/logic bugs you encountered, and how you solved them:

### Example `log.txt`:
```text
Lab Reflection:

1. Approach:
Used a while loop to take input numbers until user entered 0, and a for loop to calculate the sum.

2. Errors Faced:
- Error 1: Infinite loop! Program kept running and didn't stop.
  Fix: Realized I forgot to increment the counter `i += 1` inside the while loop.
- Error 2: IndentationError: expected an indented block.
  Fix: Corrected 4-space tab indentation inside the loop body.

3. Output:
Tested with inputs 5, 10, 15, 0. Output printed: "Total Sum = 30".
```
*(If your code worked on the very first try without any bugs, simply write: "Ran on first attempt without errors!")*

---

## 🔄 Daily Git Commands

Whenever you add or update your code:

```bash
# 1. Stage your files
git add .

# 2. Commit your work
git commit -m "Add Python Lab 13 solution and log"

# 3. Push to your repository
git push origin main
```

> 💡 **Multiple commits are completely fine!**  
> You can commit after each error, while trying fixes, or after completing. There is no limit on commits—multiple commits show your real problem-solving journey!
