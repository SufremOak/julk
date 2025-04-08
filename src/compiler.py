# julk_compiler.py (Advanced Julk Compiler with CLI)

import json
import argparse
import sys
from pathlib import Path
import re

def compile_julk_to_json(julk_code: str):
    lines = [line.strip() for line in julk_code.strip().splitlines() if line.strip()]
    program = []
    current_block = []
    in_if = False

    def flush_if():
        nonlocal current_block, in_if
        if in_if:
            program.append({
                "type": "if",
                "condition": current_block[0][3:].strip(':'),
                "body": [l for l in current_block[1:]]
            })
            current_block = []
            in_if = False

    for line in lines:
        if line.startswith("defmacro "):
            flush_if()
            _, name = line.split(maxsplit=1)
            program.append({"type": "macro", "name": name})

        elif line.startswith("def "):
            flush_if()
            parts = line.split(" ", 2)
            if "alias(" in line:
                name = parts[1]
                program.append({"type": "alias_macro", "name": name, "rule": parts[2]})
            elif len(parts) == 3:
                name, body = parts[1], parts[2]
                program.append({"type": "function", "name": name, "body": body})

        elif line.startswith("let "):
            flush_if()
            _, rest = line.split("let ", 1)
            name, value = rest.split("=", 1)
            program.append({"type": "let", "name": name.strip(), "value": value.strip()})

        elif line.startswith("eval "):
            flush_if()
            _, rest = line.split("eval ", 1)
            name, expr = rest.split("=", 1)
            program.append({"type": "eval", "name": name.strip(), "expr": expr.strip()})

        elif line.startswith("definex "):
            flush_if()
            _, rest = line.split("definex ", 1)
            name, value = rest.split("=", 1)
            program.append({"type": "definex", "name": name.strip(), "value": value.strip()})

        elif line.startswith("claaf "):
            flush_if()
            match = re.match(r"claaf (\w+) \{(.+)\}\s*(\w+)?", line)
            if match:
                name, body, alias = match.groups()
                program.append({"type": "claaf", "name": name, "body": body.strip(), "alias": alias})

        elif line.startswith("sync -->"):
            flush_if()
            body = line.split("-->", 1)[1].strip().rstrip(":")
            program.append({"type": "sync", "body": body})

        elif line.startswith("if "):
            flush_if()
            current_block = [line]
            in_if = True

        elif in_if:
            if line.startswith("else"):
                match = re.match(r"else\((.*?)\) \{(.*?)\}", line)
                if match:
                    args, body = match.groups()
                    program[-1]["else"] = {"args": args.strip().split(","), "body": [body.strip()]}
                in_if = False
            else:
                current_block.append(line)

        elif "=" in line and not line.startswith("def"):
            flush_if()
            name, value = line.split("=", 1)
            program.append({"type": "assign", "name": name.strip(), "value": value.strip()})

        elif re.match(r"\w+\(.*\)", line):
            flush_if()
            name = line.split("(", 1)[0]
            args = re.findall(r"(\w+)=(\".*?\"|\'.*?\'|\S+)", line)
            arg_dict = {k: v.strip('"') for k, v in args}
            program.append({"type": "call", "name": name, "args": arg_dict})

        else:
            flush_if()
            program.append({"type": "call_or_macro", "name": line})

    flush_if()
    return program

def main():
    parser = argparse.ArgumentParser(description="Julk Compiler - Advanced")
    parser.add_argument("input", help="Input Julk source file (.jlk)")
    parser.add_argument("-o", "--output", default="compiled.julk.json", help="Output JSON file")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"[compiler] File not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    with open(input_path, "r") as f:
        julk_code = f.read()

    program = compile_julk_to_json(julk_code)

    with open(args.output, "w") as f:
        json.dump(program, f, indent=2)

    print(f"[compiler] Compiled {args.input} -> {args.output}")

if __name__ == "__main__":
    main()
