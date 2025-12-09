# Documentation of Learning **Python** Programming Language

---

## What is **Python**?

- **Python** is a high-level, general-purpose programming language known for its **simplicity**, **readability**, and **versatility**.
    
- It is widely used in many fields such as automation, data science, web development, AI, networking, cybersecurity, and more.
    

### Key Features:

- **Beginner-friendly syntax** → very easy to read and write
    
- **Huge standard library** → built-in modules for almost everything
    
- **Cross-platform** → runs on Windows, macOS, Linux, and more
    
- **Large ecosystem** → thousands of libraries (NumPy, Flask, TensorFlow, etc.)
    
- **Interpreted language** → runs without compiling
    
- **Dynamic typing** → variable types are determined at runtime
    

### What it's used for:

- Automation & scripting
    
- Web development (Django, Flask, FastAPI)
    
- Data analysis & visualization
    
- Machine learning & AI
    
- Networking tools
    
- Cybersecurity scripts
    
- Game development
    
- Desktop & GUI apps
    

### Why it matters:

- Python is one of the most widely used languages globally due to its flexibility and ease of use.
    
- Ideal for beginners and professionals alike.
    
- Massive community support and continuous improvements.
    
- Used by NASA, Google, Meta, Amazon, and many major tech companies.
    

---

## Download Python:

Official download page:  
[https://www.python.org/downloads/](https://www.python.org/downloads/)

Or use:

- Linux/macOS: `sudo apt install python3` or already installed
    
- Windows Store: Install Python 3.x from Microsoft Store
    
- `pyenv` for managing multiple versions
    

---

## Creating and Running Python Files

- Python files use the `.py` extension
    
- Run a Python file using:
    
    `python3 filename.py`
    
    or on Windows
    
    `python filename.py`
    

### Example:

`print("Hello, Python!")`

Run it:

`python3 hello.py`

---

## Using **pip** — Python Package Manager

Install packages:

`pip install package_name`

Check installed packages:

`pip list`

Upgrade pip:

`pip install --upgrade pip`

---

## Creating Virtual Environments (Recommended)

Python projects often need isolated environments.

### Create venv:

`python3 -m venv myenv`

### Activate venv:

- Linux/macOS:
    
    `source myenv/bin/activate`
    
- Windows:
    
    `myenv\Scripts\activate`
    

### Deactivate:

`deactivate`

---

## Using **requirements.txt**

Export installed libraries:

`pip freeze > requirements.txt`

Install from file:

`pip install -r requirements.txt`

---

## Using **Jupyter Notebook** (Optional but Helpful)

Install:

`pip install jupyter`

Run:

`jupyter notebook`

Useful for data science, explanations, and interactive coding.

---

## Basic Python Program Structure

`def main():     print("Python program running!")  if __name__ == "__main__":     main()`

---

## Back to [README](../../../../README.md) Mainpage