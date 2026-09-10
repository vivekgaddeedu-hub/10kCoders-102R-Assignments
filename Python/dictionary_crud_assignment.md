# Python Assignment: Dictionary Datatype & CRUD Operations

- **Course / Batch:** 10kCoders - 102R
- **Topic:** Python Dictionary Datatype and CRUD Operations
- **Executable Script:** [`dictionary_crud_assignment.py`](file:///Users/sudheergadde/Desktop/10kCoders-102R-Assignments/Python/dictionary_crud_assignment.py)

---

## 1. Objective

In this assignment, we implement a dictionary-based Employee Information Management System to practice basic **CRUD** (Create, Read, Update, Delete) operations using Python's built-in `dict` datatype. 

The assignment reinforces:
1. Understanding Python dictionaries as hash tables with key-value pairs.
2. Managing structured records using nested dictionaries.
3. Writing clean, modular functions for each CRUD operation.
4. Implementing input validation and edge-case handling (e.g., duplicate entries, missing keys).

---

## 2. Employee Record Schema

Each employee record is stored as an inner dictionary with four core attributes:

| Key | Data Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `employee_id` | `str` | Unique primary identifier | `"EMP101"` |
| `name` | `str` | Full employee name | `"Alice Johnson"` |
| `age` | `int` | Age of employee in years | `29` |
| `department` | `str` | Assigned organizational team | `"Software Engineering"` |

The master database dictionary maps each `employee_id` to its corresponding employee record:
```python
employees_db = {
    "EMP101": {
        "employee_id": "EMP101",
        "name": "Alice Johnson",
        "age": 29,
        "department": "Software Engineering"
    },
    "EMP102": {
        "employee_id": "EMP102",
        "name": "Bob Smith",
        "age": 34,
        "department": "Data Science"
    }
}
```

---

## 3. CRUD Operations Breakdown

### 3.1 Create (Add a New Employee)
- **Concept:** Uses direct dictionary assignment `database[employee_id] = record`.
- **Validation:** Verifies that `employee_id` is unique (`employee_id not in database`) and that fields like `age` are positive integers.
- **Complexity:** Average $\mathcal{O}(1)$ time complexity.

```python
def create_employee(database, employee_id, name, age, department):
    if employee_id in database:
        print(f"Error: Employee {employee_id} already exists.")
        return False
    database[employee_id] = {
        "employee_id": employee_id,
        "name": name,
        "age": age,
        "department": department
    }
    return True
```

### 3.2 Read (Retrieve & Display)
- **Concept:** Uses `.get(key)` for safe single-record retrieval and `.items()` for iterating over all registered records.
- **Handling Missing Keys:** Using `.get()` avoids raising an unhandled `KeyError`.
- **Complexity:** Average $\mathcal{O}(1)$ for single lookup, $\mathcal{O}(N)$ for iterating over all $N$ records.

```python
def read_employee(database, employee_id=None):
    if employee_id is not None:
        return database.get(employee_id)
    for emp_id, record in database.items():
        print(record)
```

### 3.3 Update (Modify Existing Record)
- **Concept:** Locates the existing record via `database[employee_id]` and selectively updates only provided attributes.
- **Validation:** Verifies the target key exists before mutation; handles invalid updates gracefully.
- **Complexity:** Average $\mathcal{O}(1)$ time complexity.

```python
def update_employee(database, employee_id, name=None, age=None, department=None):
    if employee_id not in database:
        return False
    emp = database[employee_id]
    if name: emp["name"] = name
    if age: emp["age"] = age
    if department: emp["department"] = department
    return True
```

### 3.4 Delete (Remove Employee Record)
- **Concept:** Uses `.pop(key)` to atomically delete the key from the dictionary and return the removed record.
- **Handling Missing Keys:** Checks `if employee_id in database:` to prevent exceptions.
- **Complexity:** Average $\mathcal{O}(1)$ time complexity.

```python
def delete_employee(database, employee_id):
    if employee_id in database:
        return database.pop(employee_id)
    return None
```

---

## 4. Example Use Cases & Test Walkthrough

The script includes an automated demonstration suite [`run_crud_demonstration()`](file:///Users/sudheergadde/Desktop/10kCoders-102R-Assignments/Python/dictionary_crud_assignment.py#L182) covering standard execution and edge cases:

1. **Create Case:** Adds four employees across Engineering, Data Science, Product, and Cloud departments.
2. **Duplicate Prevention:** Prevents re-adding an existing ID (`EMP101`).
3. **Read All:** Formats all active records in a clean tabular view.
4. **Read Single:** Queries `EMP102` and handles queries for non-existent IDs (`EMP999`).
5. **Update Case:** Modifies Alice's department to *"Principal Architecture"* and increments age to `30`.
6. **Delete Case:** Removes Bob Smith (`EMP102`) and asserts deletion.
7. **Post-Delete Verification:** Renders final table showing remaining records.

---

## 5. Dictionary Algorithmic Performance

| Operation | Syntax | Average Time Complexity | Worst Case |
| :--- | :--- | :--- | :--- |
| **Insert / Create** | `d[key] = val` | $\mathcal{O}(1)$ | $\mathcal{O}(N)$ (hash collisions) |
| **Lookup / Read** | `d.get(key)` | $\mathcal{O}(1)$ | $\mathcal{O}(N)$ |
| **Update** | `d[key] = new_val` | $\mathcal{O}(1)$ | $\mathcal{O}(N)$ |
| **Delete** | `d.pop(key)` | $\mathcal{O}(1)$ | $\mathcal{O}(N)$ |
| **Iterate All** | `d.items()` | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
