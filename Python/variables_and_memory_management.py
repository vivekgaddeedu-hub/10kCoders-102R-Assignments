"""
=============================================================================
Assignment: Variables and Memory Management in Python
Course / Organization: 10kCoders - 102R
Objective:
    Understand and practice working with variables, data types, and memory 
    management in Python. Explore variable declaration, dynamic typing,
    numeric operations, object identity with id(), and variable scoping.
=============================================================================
"""

import sys


def print_header(title: str) -> None:
    """Helper function to print formatted section headers."""
    separator = "=" * 75
    print(f"\n{separator}")
    print(f" {title.upper()} ")
    print(f"{separator}\n")


def task_1_declare_and_initialize():
    """
    Task 1:
    Declare and initialize variables of different data types (int, float, str, bool)
    and observe how Python assigns memory to these variables.
    """
    print_header("Task 1: Variable Declaration & Memory Allocation")

    # Declaring variables of different primitive/core data types
    var_int = 42
    var_float = 98.6
    var_str = "Hello, Python!"
    var_bool = True

    variables = [
        ("Integer (int)", "var_int", var_int),
        ("Float (float)", "var_float", var_float),
        ("String (str)", "var_str", var_str),
        ("Boolean (bool)", "var_bool", var_bool),
    ]

    print(f"{'Data Type':<18} | {'Variable Name':<12} | {'Value':<18} | {'Type':<12} | {'Memory ID (id())':<16} | {'Size (bytes)':<10}")
    print("-" * 95)

    for dtype, name, val in variables:
        mem_id = id(val)
        size = sys.getsizeof(val)
        print(f"{dtype:<18} | {name:<12} | {str(val):<18} | {type(val).__name__:<12} | {mem_id:<16} | {size:<10}")

    print("\nObservation on Memory Allocation:")
    print("1. In Python, variables do not store values directly; they store references (memory addresses) to objects.")
    print("2. id() returns the identity/memory address where the object is stored in CPython.")
    print("3. sys.getsizeof() shows the memory footprint in bytes, including PyObject overhead.")


def task_2_assign_and_reassign():
    """
    Task 2:
    Practice assigning and reassigning values to variables,
    noting any changes in data types.
    """
    print_header("Task 2: Dynamic Typing and Reassignment")

    sample_var = 100
    print(f"[Initial Assignment]   Value: {sample_var!r:<20} | Type: {type(sample_var).__name__:<10} | id: {id(sample_var)}")

    # Reassigning to a float
    sample_var = 99.99
    print(f"[Reassigned to Float]  Value: {sample_var!r:<20} | Type: {type(sample_var).__name__:<10} | id: {id(sample_var)}")

    # Reassigning to a string
    sample_var = "Dynamic Typing"
    print(f"[Reassigned to String] Value: {sample_var!r:<20} | Type: {type(sample_var).__name__:<10} | id: {id(sample_var)}")

    # Reassigning to a boolean
    sample_var = False
    print(f"[Reassigned to Bool]   Value: {sample_var!r:<20} | Type: {type(sample_var).__name__:<10} | id: {id(sample_var)}")

    # Reassigning to a list (collection)
    sample_var = [1, 2, 3]
    print(f"[Reassigned to List]   Value: {str(sample_var):<20} | Type: {type(sample_var).__name__:<10} | id: {id(sample_var)}")

    print("\nObservation on Dynamic Typing:")
    print("1. Python is dynamically typed: variable types are checked and determined at runtime.")
    print("2. Reassigning a variable changes the reference to point to a completely new object in memory.")
    print("3. Notice that id(sample_var) changes with each reassignment as new objects are created/referenced.")
    print("4. When an object's reference count drops to 0, Python's garbage collector frees the memory.")


def task_3_personal_information():
    """
    Task 3:
    Create a set of variables to store personal information
    (name, age, height, employment status) using appropriate data types.
    """
    print_header("Task 3: Personal Information Variables")

    # Storing personal information with appropriate types
    name: str = "Vivek Gadde"          # String: textual representation
    age: int = 22                      # Integer: whole number
    height: float = 5.9                # Float: decimal value in feet
    is_employed: bool = True           # Boolean: binary state (True/False)

    print("Personal Profile:")
    print(f"  • Name              : {name} (type: {type(name).__name__})")
    print(f"  • Age               : {age} years (type: {type(age).__name__})")
    print(f"  • Height            : {height} ft (type: {type(height).__name__})")
    print(f"  • Employment Status : {'Employed' if is_employed else 'Unemployed'} (raw: {is_employed}, type: {type(is_employed).__name__})")

    # Formatted summary card
    status_str = "Employed" if is_employed else "Not Employed"
    print("\nFormatted Summary:")
    print(f"  Candidate {name} is {age} years old, {height} feet tall, and is currently {status_str}.")


def task_4_numeric_arithmetic_operations():
    """
    Task 4:
    Use Python to perform basic arithmetic operations with variables
    of numeric data types (int, float) and observe how the results
    are stored and represented.
    """
    print_header("Task 4: Numeric Operations & Type Coercion")

    int_a = 25
    int_b = 4
    float_x = 10.5
    float_y = 2.5

    operations = [
        ("int + int", int_a, "+", int_b, int_a + int_b),
        ("int - int", int_a, "-", int_b, int_a - int_b),
        ("int * int", int_a, "*", int_b, int_a * int_b),
        ("int / int (division)", int_a, "/", int_b, int_a / int_b),
        ("int // int (floor div)", int_a, "//", int_b, int_a // int_b),
        ("int % int (modulo)", int_a, "%", int_b, int_a % int_b),
        ("int ** int (power)", int_b, "**", 3, int_b ** 3),
        ("int + float (implicit coercion)", int_a, "+", float_x, int_a + float_x),
        ("float * float", float_x, "*", float_y, float_x * float_y),
        ("float / float", float_x, "/", float_y, float_x / float_y),
    ]

    print(f"{'Operation':<32} | {'Expression':<22} | {'Result':<12} | {'Result Type':<12}")
    print("-" * 85)

    for desc, operand1, op, operand2, result in operations:
        expr = f"{operand1} {op} {operand2}"
        print(f"{desc:<32} | {expr:<22} | {str(result):<12} | {type(result).__name__:<12}")

    print("\nObservation on Representation & Implicit Coercion:")
    print("1. Standard division ('/') always produces a float in Python 3, even when dividing integers evenly (e.g. 10 / 2 -> 5.0).")
    print("2. When mixing an int and a float (e.g. 25 + 10.5), Python implicitly converts the int to a float (type promotion).")
    print("3. Floating-point numbers are represented in IEEE 754 format, which may introduce minor binary precision quirks:")
    test_quirk = 0.1 + 0.2
    print(f"   Example: 0.1 + 0.2 = {test_quirk} (not exact 0.3 due to binary float representation).")


def task_5_id_experimentation_and_memory():
    """
    Task 5:
    Experiment with the id() function to explore how Python manages
    memory for variables, especially when assigning the same value
    to multiple variables.
    """
    print_header("Task 5: Memory Management & the id() Function")

    # Case 1: Small Integer Caching (-5 to 256)
    print("--- Case 1: Integer Caching / Interning (Small vs Large Integers) ---")
    val_1 = 100
    val_2 = 100
    print(f"val_1 = 100 -> id: {id(val_1)}")
    print(f"val_2 = 100 -> id: {id(val_2)}")
    print(f"Do val_1 and val_2 share the exact same memory address? {id(val_1) == id(val_2)} (val_1 is val_2: {val_1 is val_2})")
    print("Explanation: CPython pre-allocates and reuses integer objects in the range [-5, 256].")

    # Case 2: String Interning
    print("\n--- Case 2: String Interning ---")
    str_1 = "python_rule"
    str_2 = "python_rule"
    print(f"str_1 = 'python_rule' -> id: {id(str_1)}")
    print(f"str_2 = 'python_rule' -> id: {id(str_2)}")
    print(f"str_1 is str_2? {str_1 is str_2} (Shared memory address: {id(str_1) == id(str_2)})")
    print("Explanation: Short, immutable identifier-like strings are automatically interned by Python.")

    # Case 3: Mutable objects (Lists) with same content
    print("\n--- Case 3: Mutable Objects (Lists) vs Aliasing ---")
    list_x = [1, 2, 3]
    list_y = [1, 2, 3]
    list_z = list_x  # Reference alias

    print(f"list_x = [1, 2, 3] -> id: {id(list_x)}")
    print(f"list_y = [1, 2, 3] -> id: {id(list_y)}")
    print(f"list_z = list_x    -> id: {id(list_z)}")
    print(f"list_x == list_y (value equality):   {list_x == list_y}")
    print(f"list_x is list_y (identity equality): {list_x is list_y} (Different memory locations!)")
    print(f"list_x is list_z (identity equality): {list_x is list_z} (Same reference / alias!)")

    # Modifying list_z reflects in list_x
    list_z.append(4)
    print("\nAfter executing list_z.append(4):")
    print(f"  list_x is now: {list_x}")
    print(f"  list_y is now: {list_y}")
    print(f"  list_z is now: {list_z}")
    print("Key Takeaway: '==' checks for value equality, while 'is' (and id()) checks for object identity in memory.")


def task_6_variable_scope_demonstration():
    """
    Task 6:
    Write a short Python script to demonstrate understanding of variable
    scope by declaring variables within and outside of a conditional block,
    then print their values from different scopes to see accessibility.
    """
    print_header("Task 6: Variable Scope (Conditional Blocks & Functions)")

    # 1. Variable declared outside conditional block
    outer_var = "I was declared OUTSIDE the conditional block (Global/Enclosing Scope)"
    condition = True

    print(f"Before if block: outer_var = '{outer_var}'")

    if condition:
        # Variable declared inside conditional block
        inner_var = "I was declared INSIDE the 'if' block"
        # Accessing outer variable inside the block
        print(f"\nInside if block:")
        print(f"  Accessible: outer_var = '{outer_var}'")
        print(f"  Accessible: inner_var = '{inner_var}'")
        
        # Modifying outer variable inside the block
        outer_var = "Modified inside the 'if' block"

    # Testing accessibility outside the conditional block
    print(f"\nOutside if block:")
    print(f"  Accessible: outer_var = '{outer_var}'")
    print(f"  Accessible: inner_var = '{inner_var}'")

    print("\nCRITICAL PYTHON SCOPE RULE:")
    print("Unlike languages like C, C++, or Java, 'if' blocks (conditionals), 'for' loops,")
    print("and 'while' loops DO NOT create a new local scope in Python!")
    print("Variables defined inside an executed conditional block remain accessible in the outer scope.")

    # What happens if a conditional block does NOT execute?
    print("\nDemonstrating unexecuted conditional block:")
    if False:
        unexecuted_var = "You will never reach me"

    try:
        # Dynamically evaluate 'unexecuted_var' to demonstrate runtime NameError without triggering static analyzer unbound name errors
        eval("unexecuted_var")
    except NameError as e:
        print(f"  Attempting to access 'unexecuted_var' -> NameError caught: {e}")
        print("  Explanation: If the block never executes, the variable is never bound/created in the namespace.")

    # Contrast with function scope
    print("\n--- Contrast: Function Scope (Local vs Global) ---")
    def sample_function():
        local_var = "I exist ONLY inside sample_function()"
        print(f"  Inside function: local_var = '{local_var}'")

    sample_function()
    try:
        # Dynamically evaluate 'local_var' outside its function to demonstrate scope isolation cleanly
        eval("local_var")
    except NameError as e:
        print(f"  Outside function: NameError caught: {e}")
        print("  Explanation: Unlike conditionals, functions DO introduce a local scope (LEGB rule: Local, Enclosing, Global, Built-in).")


def main():
    """Main execution function running all assignment tasks sequentially."""
    print("=============================================================================")
    print("    10kCoders - Python Assignment: Variables & Memory Management")
    print("=============================================================================")
    task_1_declare_and_initialize()
    task_2_assign_and_reassign()
    task_3_personal_information()
    task_4_numeric_arithmetic_operations()
    task_5_id_experimentation_and_memory()
    task_6_variable_scope_demonstration()
    print_header("Assignment Completed Successfully")


if __name__ == "__main__":
    main()
