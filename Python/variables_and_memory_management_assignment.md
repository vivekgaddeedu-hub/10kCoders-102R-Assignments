# Assignment: Variables and Memory Management in Python

- **Course / Track:** 10kCoders - 102R
- **Topic:** Variables, Data Types, Dynamic Typing, and Memory Management in Python
- **Executable Script:** [`Python/variables_and_memory_management.py`](file:///Users/sudheergadde/Desktop/10kCoders-102R-Assignments/Python/variables_and_memory_management.py)

---

## 1. Objective

This assignment focuses on practicing and understanding variables and data types in Python. It explores how Python allocates memory to objects, how dynamic typing handles reassignment, how object identity works via `id()`, how arithmetic operations interact with numeric data types, and how variable scoping functions across conditional blocks and functions.

---

## 2. Theoretical Background

### 2.1 Variables as References (Not Memory Buckets)
In low-level languages like C or C++, a variable is a named memory location (a "bucket") that directly stores binary data of a fixed type. 
In Python, **everything is an object**. A variable is simply a **name (reference/pointer)** bound to an object in the Python heap:
- An integer `42` is a `PyLongObject` containing metadata (type pointer, reference count, value).
- A variable name like `x = 42` merely stores the memory address pointing to that `PyLongObject`.

### 2.2 Memory Management Mechanisms in CPython
1. **Reference Counting:** Every object maintains a count (`ob_refcnt`) of how many references point to it. When an object's reference count drops to 0, Python immediately deallocates the memory.
2. **Cyclic Garbage Collector:** A cyclic garbage collector detects and cleans up circular references (e.g., two objects referencing each other) that reference counting alone cannot resolve.
3. **Small Integer Caching (Interning):** CPython pre-allocates an array of integer objects for values in the range `[-5, 256]`. Whenever any variable is assigned an integer in this range, it points to the pre-existing cached object rather than creating a new one.
4. **String Interning:** Python automatically interns compile-time constant strings that look like valid Python identifiers.

### 2.3 Scoping in Python (LEGB Rule)
Python resolves names using the **LEGB** rule:
- **L**ocal: Inside the current function.
- **E**nclosing: In enclosing functions (closures).
- **G**lobal: Module-level variables.
- **B**uilt-in: Python built-in namespace (`print`, `id`, `len`, etc.).

> **Crucial Rule:** In Python, control structures like `if`, `for`, `while`, and `try-except` **do NOT create a new local scope**. Only functions, classes, and comprehensions create separate scopes.

---

## 3. Tasks & Implementation Details

### Task 1: Declare & Initialize Variables of Different Data Types
We declare four fundamental data types (`int`, `float`, `str`, `bool`) and inspect their values, data types (`type()`), memory addresses (`id()`), and memory consumption (`sys.getsizeof()`):

```python
import sys

var_int = 42
var_float = 98.6
var_str = "Hello, Python!"
var_bool = True
```

**Memory Observation:**
- `sys.getsizeof()` reveals the overhead of Python objects:
  - `int` (42) takes 28 bytes (includes reference count, type info, and arbitrary-precision structure).
  - `float` (98.6) takes 24 bytes.
  - `bool` (True) takes 28 bytes (in Python, `bool` is a subclass of `int`).
  - `str` takes 49+ bytes depending on character encoding and length.

---

### Task 2: Assigning and Reassigning Values (Dynamic Typing)
Python allows a variable name to point to an object of one type and later point to an object of an entirely different type:

```python
sample_var = 100               # int (id: A)
sample_var = 99.99             # float (id: B)
sample_var = "Dynamic Typing"  # str (id: C)
sample_var = False             # bool (id: D)
sample_var = [1, 2, 3]         # list (id: E)
```

**Observation:**
- With each reassignment, `id(sample_var)` changes. The old object's reference count is decremented; if zero, it is garbage collected.

---

### Task 3: Personal Information Storage
Using semantically appropriate data types:

```python
name: str = "Vivek Gadde"     # Textual data -> String
age: int = 22                 # Whole number -> Integer
height: float = 5.9           # Decimal measurement -> Float
is_employed: bool = True      # Binary state -> Boolean
```

---

### Task 4: Numeric Arithmetic Operations & Representation
Exploring arithmetic operations (`+`, `-`, `*`, `/`, `//`, `%`, `**`):

```python
int_a = 25
int_b = 4
float_x = 10.5

# Operations
addition = int_a + int_b            # 29 (int)
true_division = int_a / int_b       # 6.25 (float)
floor_division = int_a // int_b     # 6 (int)
modulo = int_a % int_b              # 1 (int)
power = int_b ** 3                  # 64 (int)
implicit_coercion = int_a + float_x # 35.5 (float)
```

**Key Findings:**
1. **Division (`/`):** In Python 3, `/` always yields a `float`, even when dividing cleanly (`4 / 2 -> 2.0`).
2. **Implicit Coercion (Type Promotion):** Mixing an `int` and a `float` promotes the integer to a float before evaluation.
3. **IEEE 754 Floating Point Representation:** Binary floating-point representation causes precision quirks such as `0.1 + 0.2 == 0.30000000000000004`.

---

### Task 5: Memory Management & the `id()` Function
Using `id()` to examine memory sharing and object identity:

#### 1. Small Integer Interning (`[-5, 256]`):
```python
val_1 = 100
val_2 = 100
print(val_1 is val_2)  # True -> Both point to the exact same pre-allocated object
```

#### 2. String Interning:
```python
str_1 = "python_rule"
str_2 = "python_rule"
print(str_1 is str_2)  # True -> Identical string constants share memory
```

#### 3. Mutable Objects vs Aliasing:
```python
list_x = [1, 2, 3]
list_y = [1, 2, 3]     # Separate object with same content
list_z = list_x        # Reference alias

print(list_x == list_y)  # True  (Value equality)
print(list_x is list_y)  # False (Different memory addresses)
print(list_x is list_z)  # True  (Exact same memory reference)
```

---

### Task 6: Variable Scope in Conditional Blocks vs Functions
Demonstrating that `if` blocks do **not** create a scope in Python:

```python
outer_var = "Declared outside"

if True:
    inner_var = "Declared inside if block"
    outer_var = "Modified inside if block"

# Both are accessible here:
print(outer_var)  # "Modified inside if block"
print(inner_var)  # "Declared inside if block" (Accessible!)
```

**Unexecuted Conditionals:**
If an `if` block condition evaluates to `False`, the assignment statement is never executed, and the variable name is never bound. Attempting to access it raises `NameError`.

**Contrast with Function Scope:**
Functions do establish a new local namespace:
```python
def my_function():
    local_var = "Local only"

# Outside:
# print(local_var) -> Raises NameError: name 'local_var' is not defined
```

---

## 4. How to Run the Script

Run the script from your terminal:

```bash
python3 Python/variables_and_memory_management.py
```

---

## 5. Summary & Key Takeaways

| Concept | Low-Level Languages (C/C++) | Python |
| :--- | :--- | :--- |
| **Variable Nature** | Fixed typed memory location (container) | Name/Tag referencing a heap object |
| **Typing** | Static (fixed at compile time) | Dynamic (checked and bound at runtime) |
| **Division Operator (`/`)** | Truncating integer division for ints | Always returns `float` |
| **Block Scope (`if` / `for`)**| Creates a new block scope | Does **not** create a new scope |
| **Object Caching** | Managed manually | Automatic integer & string interning |
| **Memory Cleanup** | Manual (`malloc`/`free`) or RAII | Automatic reference counting + cyclic GC |
