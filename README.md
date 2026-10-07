# 💻 Programming for AI — Lab Repository
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
cd sec-g-2610997694-yashvi
```

---

## 📂 Folder Structure

Maintain a **separate folder for each individual lab**:

```text
sec-g-2610997694-yashvi/
├── README.md
│
├── Lab_01/                                <--- [Previous Lab Example]
│   └── solution.py                        (Only solution.py needed, no log required)
├── Lab_02/
│   └── solution.py
...
├── Lab_13/                                <--- [Upcoming Lab Example]
│   ├── solution.py                        (Your Python program)
│   └── log.txt                            (Your thoughts & error log)
└── Lab_14/
    ├── solution.py
    └── log.txt
```

---

## 📝 Learning & Error Log (`log.txt`) — For Lab 13 Onwards

For upcoming labs (starting from Lab 13), create a simple Notepad text file named **`log.txt`** in that lab's folder.

> 💬 **Tip:** Write casually in plain words just like you chat or take rough notes—no formal language needed! Just your honest thoughts, what went wrong, and how you fixed it. You can record one or multiple errors.

### Example `log.txt`:
```text
Lab Reflection:

1. Approach:
Used a while loop to keep taking input numbers until the user entered 0, and a for loop to calculate the sum.

2. Errors Faced:
- Error 1: Infinite loop! Program kept running and didn't stop.
  Fix: Realized I forgot to increment the counter `i += 1` inside the while loop.
- Error 2: IndentationError: expected an indented block.
  Fix: Corrected the 4-space tab indentation inside the loop body.

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
git commit -m "Add Lab 13 solution and log.txt"

# 3. Push to your repository
git push origin main
```

> 💡 **Multiple commits are completely fine!**  
> You can commit after each error, while trying fixes, or after completing. There is no limit on commits—multiple commits show your real problem-solving journey!
