# Python Assignment: Python Data Types Comprehensive Study

| Detail | Information |
| :--- | :--- |
| **Date** | 25-06-2026 |
| **Tech Stack** | Python |
| **Topic** | Python Data Types (`int`, `str`, `list`, `tuple`, `set`, `dict`) |
| **Course / Track** | 10kCoders - 102R |
| **Executable Script** | [`python_datatypes_assignment.py`](file:///Users/sudheergadde/Desktop/10kCoders-102R-Assignments/Python/python_datatypes_assignment.py) |

---

## 1. What is an Integer (`int`) in Python? Write its features with an example.

### Definition:
An **Integer (`int`)** in Python is a fundamental, primitive numeric data type that represents whole numbers without any fractional or decimal component. Integers can be positive, negative, or zero (`0`).

### Key Features:
1. **Arbitrary Precision:** In Python 3, integers have unbounded precision. Unlike languages with 32-bit or 64-bit integer limits (e.g., C/Java), Python integers can grow as large as the computer's available memory allows without integer overflow.
2. **Immutable:** Once created, an integer object's value in memory cannot be altered. Reassigning a variable points it to a newly created integer object.
3. **Number Base Support:** Integers can be represented in decimal, binary (prefix `0b`), octal (prefix `0o`), or hexadecimal (prefix `0x`).
4. **CPython Integer Interning:** CPython pre-allocates small integers in the range `[-5, 256]` in memory to optimize performance and reuse memory addresses.

### Example:
```python
# Integer declaration
age = 25
negative_temp = -12
large_num = 10**35  # Arbitrary precision: 100000000000000000000000000000000000

print(age)         # Output: 25
print(type(age))   # Output: <class 'int'>
```

---

## 2. What is a String (`str`) in Python? Write its features with an example.

### Definition:
A **String (`str`)** in Python is an immutable sequence of Unicode characters used to represent and manipulate textual data.

### Key Features:
1. **Enclosure Syntax:** Strings can be defined using single quotes (`'...'`), double quotes (`"..."`), or triple quotes (`'''...'''` / `"""..."""` for multi-line strings).
2. **Immutable:** Strings cannot be changed in place. Modifying a character via index assignment (e.g., `s[0] = 'H'`) raises a `TypeError`.
3. **Sequence Operations:** Supports zero-based positive indexing (`s[0]`), negative indexing (`s[-1]`), and slicing (`s[start:stop:step]`).
4. **Rich Built-in Methods:** Offers comprehensive built-in manipulation methods such as `.upper()`, `.lower()`, `.strip()`, `.split()`, `.replace()`, and `.join()`.

### Example:
```python
greeting = "Hello, Python!"

print(greeting)          # Output: Hello, Python!
print(type(greeting))    # Output: <class 'str'>
print(greeting[0])       # Output: 'H' (Indexing)
print(greeting[0:5])     # Output: 'Hello' (Slicing)
```

---

## 3. What is a List (`list`) in Python? Write its features with an example.

### Definition:
A **List (`list`)** is an ordered, mutable collection that can store heterogeneous (mixed) elements enclosed within square brackets `[]`.

### Key Features:
1. **Ordered:** Maintains the exact sequence of element insertion. Elements can be accessed by their numerical index position.
2. **Mutable:** Elements can be added (`.append()`, `.extend()`, `.insert()`), updated (`list[0] = new_val`), or deleted (`.pop()`, `.remove()`, `del`) in place without creating a new list object.
3. **Allows Duplicate Elements:** Can store multiple identical values at different index positions.
4. **Heterogeneous Elements:** Can hold integers, strings, floats, booleans, and nested data structures (lists, dicts) simultaneously.
5. **Supports Indexing & Slicing:** Fully supports zero-based indexing and slicing operations.

### Example:
```python
fruits = ["apple", "banana", "mango", "apple"]  # allows duplicates

# List mutation
fruits.append("orange")
fruits[1] = "blueberry"

print(fruits)        # Output: ['apple', 'blueberry', 'mango', 'apple', 'orange']
print(type(fruits))  # Output: <class 'list'>
```

---

## 4. What is a Tuple (`tuple`) in Python? Write its features with an example.

### Definition:
A **Tuple (`tuple`)** is an ordered, immutable sequence of heterogeneous elements enclosed within parentheses `()`.

### Key Features:
1. **Ordered:** Retains the exact position and insertion order of each element.
2. **Immutable (Write-Protected):** Once initialized, elements cannot be modified, added, or removed. This ensures data integrity and prevents unintended side-effects.
3. **Allows Duplicates:** Can hold identical values at multiple indices.
4. **Supports Indexing & Slicing:** Elements are accessible via integer indexing and slice notation.
5. **Hashable:** If all items inside a tuple are immutable, the tuple itself is hashable and can be used as a dictionary key or set element (unlike lists).
6. **Performance:** Tuples require less memory and exhibit faster iteration speeds than lists.

### Example:
```python
coordinates = (17.3850, 78.4867, 17.3850)  # Latitude, Longitude (allows duplicates)

print(coordinates)         # Output: (17.385, 78.4867, 17.385)
print(type(coordinates))   # Output: <class 'tuple'>
print(coordinates[1])      # Output: 78.4867
```

---

## 5. What is a Set (`set`) in Python? Write its features with an example.

### Definition:
A **Set (`set`)** is an unordered, mutable collection of unique, hashable (immutable) items enclosed in curly braces `{}` (or initialized via `set()`).

### Key Features:
1. **Unique Elements Only:** Automatically removes duplicate values upon insertion.
2. **Unordered:** Elements are not stored in any guaranteed sequence. Positions depend on internal hash table buckets.
3. **No Indexing or Slicing:** Because sets are unordered, subscripting via index (`s[0]`) is not supported and raises a `TypeError`.
4. **Mutable Container with Immutable Items:** The set itself is mutable (items can be added via `.add()` and removed via `.remove()`), but every element inside must be hashable/immutable.
5. **Mathematical Set Operations:** Native support for union (`|`), intersection (`&`), difference (`-`), and symmetric difference (`^`).
6. **Fast Membership Testing:** Checking `x in my_set` operates in $\mathcal{O}(1)$ average time.

### Example:
```python
colors = {"red", "green", "blue", "red", "blue"}  # duplicates automatically deduplicated

print(colors)        # Output: {'red', 'green', 'blue'}
print(type(colors))  # Output: <class 'set'>

colors.add("yellow")
print(colors)        # Output: {'red', 'green', 'blue', 'yellow'}
```

---

## 6. What is a Dictionary (`dict`) in Python? Write its features with an example.

### Definition:
A **Dictionary (`dict`)** is an associative collection of key-value pairs enclosed in curly braces `{key: value}` where each key maps to an associated value.

### Key Features:
1. **Key-Value Mapping:** Each element consists of a `key: value` pair. Values are retrieved via their unique key (`d[key]`).
2. **Keys Must Be Unique & Hashable:** Keys must be immutable types (`str`, `int`, `tuple`) and cannot contain duplicates. Assigning an existing key overwrites the previous value.
3. **Values Can Be Anything:** Values can be duplicates, mutable, nested dictionaries, lists, or any valid Python object.
4. **Maintains Insertion Order:** Starting in Python 3.7+, dictionaries are guaranteed by specification to preserve insertion order.
5. **Mutable:** Keys and values can be dynamically added, updated, or removed (`.pop()`, `del`).
6. **High Performance:** Key lookups, insertions, and deletions execute in $\mathcal{O}(1)$ average time complexity.

### Example:
```python
employee = {
    "employee_id": "EMP101",
    "name": "Sudheer Gadde",
    "age": 24,
    "department": "Engineering"
}

# Mutation
employee["department"] = "Full Stack Architecture"  # Update value
employee["skills"] = ["Python", "HTML", "JS"]       # Add new key-value pair

print(employee)        # Output: Full dictionary
print(type(employee))  # Output: <class 'dict'>
```

---

## 7. Which Python data types are mutable and which are immutable?

### Mutable Data Types:
Data types whose internal contents or values **can be modified in place** after creation without altering their identity/memory address (`id()`):
- **`list`**
- **`dict`**
- **`set`**
- *(also `bytearray`)*

### Immutable Data Types:
Data types whose values **cannot be altered in place** once created. Any modifying operation generates a brand-new object in memory:
- **`int`**
- **`float`**
- **`str`**
- **`tuple`**
- **`bool`**
- **`complex`**
- *(also `frozenset`, `bytes`)*

---

## 8. Which data types allow duplicate values?

### Allow Duplicates:
- **`list`:** Allows identical values at different index positions (e.g., `[1, 1, 2, 2]`).
- **`tuple`:** Allows identical values at different index positions (e.g., `(1, 1, 2, 2)`).
- **`str`:** Characters can repeat as many times as needed (e.g., `"banana"`).
- **`dict` (Values only):** Multiple distinct keys can share identical values (e.g., `{"math": 95, "science": 95}`).

### Disallow Duplicates:
- **`set`:** Strictly stores unique items. Duplicate entries are discarded automatically.
- **`dict` (Keys only):** Keys must be unique; duplicate keys overwrite previously assigned values.

---

## 9. Which data types maintain the insertion order?

### Maintain Insertion Order:
- **`str`:** Characters maintain the exact sequential order in which they were written.
- **`list`:** Elements preserve the exact sequence in which they were appended/inserted.
- **`tuple`:** Elements preserve the exact sequence specified at declaration.
- **`dict`:** Preserves the insertion order of keys (guaranteed since Python 3.7+).

### Do NOT Maintain Insertion Order:
- **`set`:** Elements are stored based on a hash table algorithm without preserving insertion order.

---

## 10. Which data types support indexing and slicing?

### Support Indexing & Slicing:
All **sequence** data types support numerical zero-based indexing (`obj[0]`, `obj[-1]`) and slicing (`obj[start:stop:step]`):
- **`str`** (e.g., `"Python"[0]` &rarr; `'P'`, `"Python"[1:4]` &rarr; `'yth'`)
- **`list`** (e.g., `[10, 20, 30][0]` &rarr; `10`, `[10, 20, 30][:2]` &rarr; `[10, 20]`)
- **`tuple`** (e.g., `(1, 2, 3)[-1]` &rarr; `3`, `(1, 2, 3)[1:]` &rarr; `(2, 3)`)

### Do NOT Support Indexing & Slicing:
- **`int`:** Scalar numeric type; not a sequence.
- **`set`:** Unordered collection; indexing raises `TypeError: 'set' object is not subscriptable`.
- **`dict`:** Associative array; accessed by **key name** (`dict[key]`), not by positional index or slice.

---

## 11. Write one example for each data type and print its type using the `type()` function.

```python
# Declarations
sample_int = 100
sample_str = "Python Programming"
sample_list = [10, 20, 30]
sample_tuple = (10, 20, 30)
sample_set = {10, 20, 30}
sample_dict = {"name": "Sudheer", "role": "Developer"}

# Printing values and their verified types
print("sample_int   :", sample_int, "->", type(sample_int))
print("sample_str   :", sample_str, "->", type(sample_str))
print("sample_list  :", sample_list, "->", type(sample_list))
print("sample_tuple :", sample_tuple, "->", type(sample_tuple))
print("sample_set   :", sample_set, "->", type(sample_set))
print("sample_dict  :", sample_dict, "->", type(sample_dict))
```

### Verified Output:
```text
sample_int   : 100                      -> <class 'int'>
sample_str   : Python Programming      -> <class 'str'>
sample_list  : [10, 20, 30]              -> <class 'list'>
sample_tuple : (10, 20, 30)              -> <class 'tuple'>
sample_set   : {10, 20, 30}              -> <class 'set'>
sample_dict  : {'name': 'Sudheer', ...}  -> <class 'dict'>
```

---

## 12. Comparison Table Across Python Data Types

| Feature | `int` | `str` | `list` | `tuple` | `set` | `dict` |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Classification** | Primitive / Numeric | Primitive / Sequence | Non-Primitive / Sequence | Non-Primitive / Sequence | Non-Primitive / Set | Non-Primitive / Mapping |
| **Syntax / Enclosure**| Plain number (e.g. `42`) | Quotes `'...'` or `"..."` | Square brackets `[...]` | Parentheses `(...)` | Curly braces `{...}` | Key-Value in `{k: v}` |
| **Mutability** | **Immutable** | **Immutable** | **Mutable** | **Immutable** | **Mutable** | **Mutable** |
| **Insertion Order** | N/A (Scalar) | **Maintained** | **Maintained** | **Maintained** | **Not Maintained** (Unordered) | **Maintained** (Python 3.7+) |
| **Allows Duplicates**| N/A (Single value) | **Yes** (Repeated chars) | **Yes** | **Yes** | **No** (Unique only) | Keys: **No** / Values: **Yes** |
| **Indexing & Slicing**| **No** | **Yes** (`s[0]`, `s[1:4]`)| **Yes** (`l[0]`, `l[1:3]`)| **Yes** (`t[0]`, `t[1:3]`)| **No** | **Key Lookup** (`d[key]`) |
| **Primary Use Case** | Arithmetic & counting | Text processing | Dynamic collections | Fixed records & keys | Deduplication & Venn sets | Fast key-based lookups |
