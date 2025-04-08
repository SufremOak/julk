# julk_interpreter.py

import json

class JulkRuntime:
    def __init__(self):
        self.functions = {}
        self.macros = {}

    def register_function(self, name, body):
        self.functions[name] = body
        print(f"[julk] Registered function '{name}'")

    def register_macro(self, name):
        # Simple macro transformer example
        def transformer():
            print("You said the magic word!")
        self.macros[name] = transformer
        print(f"[julk] Registered macro '{name}'")

    def call(self, name):
        if name in self.functions:
            print(f"[julk] Executing {name}: {self.functions[name]}")
        elif name in self.macros:
            self.macros[name]()
        else:
            print(f"[julk] Unknown symbol: {name}")

    def run(self, program):
        for entry in program:
            etype = entry["type"]

            if etype == "macro":
                self.register_macro(entry["name"])
            elif etype == "function":
                self.register_function(entry["name"], entry["body"])
            elif etype == "call_or_macro":
                self.call(entry["name"])
            elif etype == "expression":
                print(f"[julk] Evaluating expression: {entry['expr']}")
            else:
                print(f"[julk] Unknown entry type: {etype}")


if __name__ == "__main__":
    with open("compiled.julk.json") as f:
        program = json.load(f)

    rt = JulkRuntime()
    rt.run(program)
