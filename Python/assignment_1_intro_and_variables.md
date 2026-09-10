# Python Assignment - 1: Introduction & Variables

| Information | Details |
| :--- | :--- |
| **Course / Batch** | 10kCoders - 102R |
| **Task Title** | Python Assignment - 1 |
| **Topic** | Introduction and Variables |
| **Instructor** | M. Ajay |
| **Date Assigned** | 15 – 06 – 2026 |
| **Deadline** | 16 – 06 – 2026 |
| **Mode** | Individual |
| **Status** | Completed |

---

## PART A — Multiple Choice Questions
**Choose the correct answer for each question. (15 × 1 = 15 Marks)**

---

### 1. What is a variable in Python?
- A) A fixed value  
- **B) A container to store data**  
- C) A keyword  
- D) A function  

> **Correct Answer:** **B) A container to store data**  
> **Explanation:** In Python, a variable is a named reference (or container) that points to a memory location storing a value or object.

---

### 2. Which of the following is a valid variable name?
- A) `1name`  
- **B) `name_1`**  
- C) `@name`  
- D) `class`  

> **Correct Answer:** **B) `name_1`**  
> **Explanation:** Identifiers cannot begin with a number (`1name`), cannot contain special characters like `@` (`@name`), and cannot be reserved keywords (`class`). `name_1` starts with a letter and contains only letters, digits, and underscores.

---

### 3. Python variables are declared using:
- A) `var` keyword  
- B) `int` keyword  
- **C) No keyword**  
- D) `define` keyword  

> **Correct Answer:** **C) No keyword**  
> **Explanation:** Python is dynamically typed. Variables do not require declaration keywords (like `var`, `int`, or `let`); they are declared automatically upon assigning a value with `=`.

---

### 4. Which rule is correct for variable naming?
- A) Can start with number  
- B) Can contain spaces  
- **C) Can start with underscore**  
- D) Can use special symbols like `@`  

> **Correct Answer:** **C) Can start with underscore**  
> **Explanation:** A variable name in Python must start with an alphabet (`a-z`, `A-Z`) or an underscore (`_`). It cannot start with numbers, contain spaces, or use special characters.

---

### 5. What is PVM in Python?
- **A) Python Virtual Machine**  
- B) Program Version Model  
- C) Python Variable Memory  
- D) Program Virtual Method  

> **Correct Answer:** **A) Python Virtual Machine**  
> **Explanation:** PVM stands for **Python Virtual Machine**. It is the interpreter component of Python that executes compiled bytecode.

---

### 6. PVM is responsible for:
- A) Writing code  
- **B) Executing bytecode**  
- C) Designing UI  
- D) Saving files  

> **Correct Answer:** **B) Executing bytecode**  
> **Explanation:** The Python compiler converts source code (`.py`) into bytecode (`.pyc`), and the PVM is the runtime engine responsible for executing that bytecode instruction by instruction.

---

### 7. Which of the following is a correct Python file name?
- A) `my-file.py`  
- B) `1file.py`  
- **C) `my_file.py`**  
- D) `file name.py`  

> **Correct Answer:** **C) `my_file.py`**  
> **Explanation:** According to PEP 8 conventions and Python's import rules, module names should be lowercase and can contain underscores. Hyphens (`-`), leading numbers (`1file`), and spaces are invalid identifier names and cause errors when imported.

---

### 8. What is a data type?
- A) Name of variable  
- **B) Type of data stored in variable**  
- C) Function name  
- D) File format  

> **Correct Answer:** **B) Type of data stored in variable**  
> **Explanation:** A data type defines the category and nature of the data stored in a variable, which dictates what operations can be performed on it and how it is represented in memory.

---

### 9. Which of the following is a primitive data type?
- A) `list`  
- B) `dict`  
- **C) `int`**  
- D) `set`  

> **Correct Answer:** **C) `int`**  
> **Explanation:** `int` is a primitive (scalar) data type representing a single whole number. `list`, `dict`, and `set` are non-primitive/collection data types.

---

### 10. Which of the following is NOT a primitive data type?
- A) `int`  
- B) `float`  
- **C) `list`**  
- D) `bool`  

> **Correct Answer:** **C) `list`**  
> **Explanation:** `int`, `float`, and `bool` store individual atomic values (primitive). A `list` is a compound/non-primitive data type that holds a sequence of multiple values.

---

### 11. Which data type is used to store True/False values?
- A) `int`  
- B) `str`  
- **C) `bool`**  
- D) `float`  

> **Correct Answer:** **C) `bool`**  
> **Explanation:** The `bool` (Boolean) data type represents logical truth values: `True` or `False`.

---

### 12. Which of the following is a non-primitive data type?
- A) `int`  
- B) `float`  
- **C) `tuple`**  
- D) `bool`  

> **Correct Answer:** **C) `tuple`**  
> **Explanation:** `tuple` is an ordered, immutable collection of multiple elements, making it a non-primitive data structure.

---

### 13. What is the default file extension for Python files?
- A) `.java`  
- **B) `.py`**  
- C) `.txt`  
- D) `.code`  

> **Correct Answer:** **B) `.py`**  
> **Explanation:** Python programs and scripts are saved with the standard `.py` file extension.

---

### 14. Which of the following is an example of a string?
- A) `10`  
- B) `3.14`  
- **C) `"Hello"`**  
- D) `True`  

> **Correct Answer:** **C) `"Hello"`**  
> **Explanation:** Text enclosed in quotation marks (single or double) is classified as a string (`str`) in Python.

---

### 15. Non-primitive data types are:
- A) Immutable only  
- B) Used to store single value  
- **C) Used to store multiple values**  
- D) Always numbers  

> **Correct Answer:** **C) Used to store multiple values**  
> **Explanation:** Non-primitive data types (e.g., lists, tuples, dictionaries, sets) are structured collections used to hold multiple values under a single reference name.

---

## PART B — Short Answer Questions
**Answer each question briefly and clearly. (5 × 3 = 15 Marks)**

---

### Question 1: What is a variable in Python?
**Answer:**

A **variable** in Python is a named reference (or identifier) that points to an object stored in computer memory. It acts as a label to store, access, and manipulate data throughout a program.

**Key Concepts:**
1. **Dynamic Declaration:** Python variables do not require an explicit type declaration (like `int x;` in C or Java). A variable is created automatically the moment a value is assigned to it using the assignment operator (`=`).
2. **Reference Mechanism:** In Python, everything is an object. Variables do not hold raw data directly; instead, they hold the memory address (reference) pointing to the object on the heap.
3. **Dynamic Typing:** Because a variable is merely a reference, it can point to an integer at one moment and later be reassigned to point to a string, float, or list without any type error.

```python
# Declaration and assignment
student_name = "Sudheer"    # points to a string object
roll_number = 101           # points to an integer object
percentage = 89.5           # points to a float object
is_enrolled = True          # points to a boolean object

# Dynamic Typing (Reassignment)
roll_number = "101-A"       # now points to a string object without error
```

---

### Question 2: What are the rules for naming variables?
**Answer:**

When defining variable names (identifiers) in Python, the following rules and conventions must be strictly followed:

**Mandatory Rules (Syntax Rules):**
1. **Allowed Characters:** Variable names may only contain letters (`a–z`, `A–Z`), digits (`0–9`), and underscores (`_`).
2. **First Character:** A variable name **must start with an alphabet letter or an underscore (`_`)**. It can **never begin with a digit** (e.g., `1total` is invalid, `total1` is valid).
3. **No Whitespace:** Variable names cannot contain spaces or tabs (e.g., `user name` is invalid; write `user_name`).
4. **No Special Symbols:** Special characters and punctuation marks (such as `@`, `$`, `%`, `-`, `!`, `*`, `&`) are strictly prohibited (e.g., `user@email` and `total-marks` are invalid).
5. **Case Sensitivity:** Python is case-sensitive. The variables `marks`, `Marks`, and `MARKS` are treated as three completely different variables.
6. **No Reserved Keywords:** You cannot use Python reserved keywords (such as `if`, `else`, `while`, `for`, `def`, `class`, `import`, `return`, `True`, `False`, `None`) as variable names.

**Best Practice Conventions (PEP 8):**
- Use lowercase words separated by underscores (`snake_case`) for variable names (e.g., `total_amount`, `first_name`).
- Choose meaningful, descriptive names rather than cryptic single letters (e.g., `student_age` instead of `x`).

---

### Question 3: What is PVM and what is its role?
**Answer:**

**PVM** stands for **Python Virtual Machine**. It is the runtime execution engine of the Python software implementation (CPython) that executes compiled Python bytecode.

**Execution Flow:**
```
Source Code (.py) ──> [Python Compiler] ──> Bytecode (.pyc) ──> [PVM (Interpreter)] ──> Machine Code / CPU
```

**Roles and Responsibilities of PVM:**
1. **Bytecode Execution:** When you run a Python script, the Python compiler first converts human-readable source code (`.py`) into intermediate, platform-independent **bytecode** (`.pyc`). The PVM reads, interprets, and executes these bytecode instructions line by line.
2. **Conversion to Machine Code:** The PVM translates intermediate bytecode into native binary instructions (machine code: `0s` and `1s`) that the underlying computer hardware and CPU understand.
3. **Platform Independence:** Python achieves platform independence through the PVM. While bytecode is identical across all systems, each operating system (Windows, macOS, Linux) has its own PVM that maps bytecode to that system's native hardware instructions.
4. **Runtime Memory & Resource Management:** PVM works alongside Python's memory manager and garbage collector to manage call stacks, object references, and memory allocation/deallocation during runtime.

---

### Question 4: What is a data type in Python?
**Answer:**

A **data type** in Python defines the classification, format, and nature of the value that a variable references in memory. It tells the Python interpreter:
1. What kind of value is stored (e.g., whole number, decimal number, text, boolean).
2. What operations can be legally performed on that data (e.g., mathematical addition vs string concatenation).
3. How much memory is allocated and how the value is represented internally.

**Key Characteristics:**
- **Dynamic Typing:** In Python, data types are bound to values (objects), not to variable names. You do not need to declare types explicitly; Python automatically infers the data type at runtime.
- **Type Inspection:** You can verify the data type of any variable using the built-in `type()` function.

```python
# Demonstrating data types in Python
x = 25              # int
y = 12.99           # float
name = "Python"     # str
is_active = True    # bool

print(type(x))          # Output: <class 'int'>
print(type(y))          # Output: <class 'float'>
print(type(name))       # Output: <class 'str'>
print(type(is_active))  # Output: <class 'bool'>

# Allowed operations depend on data types:
print(10 + 5)       # Addition -> 15
print("10" + "5")   # Concatenation -> "105"
```

---

### Question 5: Explain primitive and non-primitive data types with examples.
**Answer:**

In Python, data types are broadly categorized into two major categories: **Primitive Data Types** and **Non-Primitive Data Types**.

#### 1. Primitive (Scalar / Fundamental) Data Types
- **Definition:** Primitive data types represent atomic, single values. They cannot be divided into smaller data components.
- **Common Types & Examples:**
  - **`int` (Integer):** Represents whole numbers (positive, negative, or zero) without decimals.
    ```python
    age = 22
    temperature = -5
    ```
  - **`float` (Floating-Point):** Represents real numbers containing decimal points or exponential notation.
    ```python
    price = 199.99
    pi = 3.14159
    ```
  - **`str` (String):** Represents an immutable sequence of characters enclosed in quotes.
    ```python
    course = "Python Full Stack"
    ```
  - **`bool` (Boolean):** Represents logical truth values: either `True` or `False`.
    ```python
    is_passed = True
    has_submitted = False
    ```
  - **`complex`:** Represents complex numbers with a real and imaginary component.
    ```python
    z = 4 + 7j
    ```

#### 2. Non-Primitive (Compound / Collection) Data Types
- **Definition:** Non-primitive data types are structured data types capable of holding collections or groups of multiple values (homogeneous or heterogeneous) under a single variable name.
- **Common Types & Examples:**
  - **`list`:** An **ordered**, **mutable** (modifiable) collection of elements enclosed in square brackets `[]`. Allows duplicate elements.
    ```python
    skills = ["Python", "HTML", "CSS", "JavaScript"]
    skills.append("Django")   # Lists can be modified
    ```
  - **`tuple`:** An **ordered**, **immutable** (cannot be changed after creation) collection enclosed in parentheses `()`. Allows duplicate elements.
    ```python
    coordinates = (17.3850, 78.4867)   # Latitude and Longitude
    ```
  - **`set`:** An **unordered**, **mutable** collection of **unique** elements (no duplicates) enclosed in curly braces `{}`.
    ```python
    unique_ids = {101, 102, 103, 101}  # Automatically filters to {101, 102, 103}
    ```
  - **`dict` (Dictionary):** A collection of **key-value pairs** enclosed in curly braces `{}`. Keys must be unique and immutable.
    ```python
    student_profile = {
        "name": "Sudheer",
        "batch": "102R",
        "score": 95
    }
    ```

#### Comparison Summary Table:
| Property | Primitive Data Types | Non-Primitive Data Types |
| :--- | :--- | :--- |
| **Value Storage** | Stores a single atomic value | Stores multiple values / collections |
| **Structure** | Basic, indivisible units | Compound, structured collections |
| **Built-in Examples** | `int`, `float`, `str`, `bool`, `complex` | `list`, `tuple`, `dict`, `set` |
| **Mutability** | Scalar values (immutable references) | Mutable (`list`, `dict`, `set`) or Immutable (`tuple`) |
| **Use Case** | Single data points (e.g., age, price) | Grouping related data (e.g., item list, record) |
