# Lab 04: Higher-Order Functions, map/filter, Decorators

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Dependencies](https://img.shields.io/badge/dependencies-none-brightgreen)

A hands-on demonstration of functional programming concepts in Python — covering higher-order functions, data transformations using `map` and `filter`, list comprehensions, and various decorator patterns including caching.

---

## 📁 Project Structure
```
lab04/
├── README.md
├── requirements.txt
├── report/
│   └── answers.md
└── src/
    └── main.py
```

---

## ⚙️ Requirements

- Python 3.10+
- External dependencies: None (`requirements.txt` is empty)

---

## 🛠️ Environment Setup

1. **Create** a virtual environment:
```bash
   python -m venv .venv
```

2. **Activate** the environment:
   - Windows: `.venv\Scripts\activate`
   - macOS / Linux: `source .venv/bin/activate`

3. **Install** dependencies:
```bash
   pip install -r requirements.txt
```

---

## 🚀 Running the Program
```bash
python src/main.py
```

---

## 🖨️ What the Program Prints

The program prints seven labeled sections (**A–G**), each demonstrating a specific functional programming or decorator concept.

| Section | Topic | Description |
|---------|-------|-------------|
| **A** | Higher-Order Function | Custom `apply` — processes a list via a passed function, without using built-in `map` |
| **B** | `map` | Squares numbers and converts integers to strings using `map` |
| **C** | `filter` | Extracts even numbers and values greater than 10 from a dataset |
| **D** | `map`/`filter` vs comprehension | Solves the same task two ways to show they produce identical results |
| **E** | Simple Decorator | `@call_counter` — tracks and prints how many times a function has been called |
| **F** | Decorator with Arguments | `@prefix` — takes a config string and prepends it to the function's return value |
| **G** | Caching Decorator | `@cache` on a recursive Tribonacci function to demonstrate memoization |

---

## 📝 Notes

- The caching demonstration highlights the significant performance difference between standard recursion and memoized recursion.
- All `map`/`filter` results are wrapped in `list()` for immediate display.
