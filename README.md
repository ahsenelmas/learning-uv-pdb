# 🐍 Learning Session 7: uv + pdb

This is a simple project created for **Learning Session 7** (task from Piotr Brudny).  
It demonstrates how to use **[uv](https://docs.astral.sh/uv/)** for dependency management and how to debug Python code with **pdb**.

---

## 📦 Setup

### 1. Install uv (Windows PowerShell)

```powershell
powershell -ExecutionPolicy Bypass -c "irm https://astral.sh/uv/install.ps1 | iex"
uv --version
````

### 2. Install Python with uv (optional)

```powershell
uv python install 3.12 --default
python --version
```

### 3. Initialize project (already done here)

```powershell
uv init learning-uv-pdb
cd learning-uv-pdb
```

---

## 📝 main.py

A small program with a **deliberate bug** to demonstrate debugging:

```python
def add(a, b):
    return a + b

def main():
    x = 1
    y = "2"  # BUG: string, not int
    import pdb; pdb.set_trace()  # breakpoint
    result = add(x, y)  # TypeError after you continue
    print("result:", result)

if __name__ == "__main__":
    main()
```

---

## 🐞 Debugging with pdb

Run the program:

```powershell
uv run main.py
```

You’ll drop into `(Pdb)` prompt. Try commands:

* `l` → list code
* `p x`, `p y` → inspect variables
* `n` → next line
* `s` → step into function
* `c` → continue
* `q` → quit

**Fix live in debugger:**

```text
(Pdb) y = 2
(Pdb) c
result: 3
```

---

## 🧪 Testing with pytest

Test file (`test_main.py`):

```python
from main import add

def test_add():
    assert add(1, 2) == 3
```

Run tests:

```powershell
uv run -m pytest -q
```

Drop into pdb automatically on a failure:

```powershell
uv run -m pytest --pdb -q
```

---

## 🌳 Show dependency tree

```powershell
uv tree
```

Output shows `pytest` and `ruff` as dependencies.

---

## ✅ Summary

* **uv**: manage Python, run scripts, show dependency tree
* **pdb**: debug code with breakpoints, inspect and fix variables live
* **pytest**: verify correctness of the `add()` function

