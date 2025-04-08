# Syntax Plan

## macros
```jlk
defmacro say
def hello print("Hello, World!")
say
hello
```

## Statements

### `if` statements
```jlk
if True:
    print("something")
```

### `sync` statements
```jlk
sync --> %if%:
    svar.State(self)
```

### `else` statements
```jlk
if <something>:
    ...
    else(<args>) {
        <expression>
    }
```

## Variables

### `eval` variable
```jlk
claaf Module {
    def type = ...
    eval a = num"1"
    eval e = num"6"

    def sum alias(expression === var1 "+" "var2" then return Result)

    sum a + e
} Mod;
```

### `let` variable
```jlk
let you = %name
let bff = %name

let name = {
    definex "you" = "Miguel"
    definex "bff" = "Johnny"
}

out(you, " is ", bff + "%'s%", "BFF.")
```


<!--I don't know!!-->

## Definers

### `claaf` definer

```javascript
const claaf = class();

// claaf is the same thing as class in other langs

claaf Fun {
    const fun = "yay";
    console.log(fun);
}
```

### `def` definer

```python
name = "John"

def sum alias === { expr() }
def greet alias === { print(name) }
```

### `definex` definer
Can be used with `let` variables, and in some cases define a mutable and/or constant value for a variable.

### `defmacro` definer
It's used to define a macro for a DSL importing and/or exportion