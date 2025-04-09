# 🧬 Julk

**Julk** is a DSL-extensible programming language and framework that compiles to **JSON**. It enables building domain-specific languages (DSLs), esolangs, and highly portable software. Julk code is parsed, compiled into structured JSON, and then interpreted by a Python runtime — making it flexible and platform-agnostic.

> ✨ Write code. 🔁 Compile to JSON. 🚀 Interpret anywhere.

---

## ✨ Features

- 🧠 **DSL-First Design** — Easily define new language constructs using macros and aliases.
- 📦 **JSON-Based Compilation** — Source code compiles into portable JSON format.
- 🧩 **Modular and Extensible** — Build DSLs, tools, and libraries in Julk itself.
- 🔁 **Cross-Language Runtime** — Python-based interpreter supports execution anywhere.
- 🎨 **Syntax Highlighting Support** — Available for VS Code, Vim, and TextMate.

---

## 🚀 Getting Started

### 🔧 Requirements

- Python 3.8+
- Optional: VS Code (for syntax support)

---

### 📥 Install

```bash
# use the install script (commin' soon)
git clone https://github.com/sufremoak/julk
cd julk
./scripts/install.sh --linux --prefix="/usr/bin" --pyenv="./.venv"
#                      ^^^^^           ^^^^^^^^
#                   Change this        customize
#                   you're not         if wanted
#                    in linux
```     

### 🛠 Example
Write a Julk file:

```jlk
defmacro say
def hello print("Hello, World!")
say
hello
```
Compile it to JSON:
```bash
python julk_compiler.py example.jlk -o output.json
```
Interpret the output:
```bash
python julk_interpreter.py output.json
```
### 🎨 Syntax Support
- ✅ VS Code (get the extension in the releases)
- ✅ Vim (julk.vim) <- Get in the releases
- ✅ TextMate

### 📘 License
MIT — See LICENSE

## 🤝 Contribute
Julk is in early development, and made by only one guy! — contributions, feedback, and language experiments are welcome! Feel free to open issues or pull requests.