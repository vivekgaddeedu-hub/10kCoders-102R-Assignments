"""
Python Assignment - 1: Introduction & Variables
Instructor: M. Ajay
Topic: Introduction and Variables
Student: Sudheer Gadde
"""

import sys

def main():
    print("=" * 65)
    print("      PYTHON ASSIGNMENT - 1: INTRODUCTION & VARIABLES DEMO")
    print("=" * 65)

    # -------------------------------------------------------------
    # PART A & B Concepts Demonstration
    # -------------------------------------------------------------

    # 1. Variables & Dynamic Typing
    print("\n[1] Variable Creation and Dynamic Typing:")
    sample = 100
    print(f"  sample = {sample!r} -> type: {type(sample).__name__}, id: {id(sample)}")
    sample = 99.95
    print(f"  sample = {sample!r} -> type: {type(sample).__name__}, id: {id(sample)}")
    sample = "Dynamic in Python"
    print(f"  sample = {sample!r} -> type: {type(sample).__name__}, id: {id(sample)}")
    sample = True
    print(f"  sample = {sample!r} -> type: {type(sample).__name__}, id: {id(sample)}")

    # 2. Variable Naming Rules Demonstration
    print("\n[2] Variable Naming Rules (Valid Identifiers):")
    valid_name_1 = "Valid with letter and digit"
    _hidden_variable = "Valid starting with underscore"
    student_total_score = 98.5
    print(f"  valid_name_1: {valid_name_1}")
    print(f"  _hidden_variable: {_hidden_variable}")
    print(f"  student_total_score: {student_total_score}")

    # Checking identifier validity programmatically
    test_identifiers = ["name_1", "1name", "@name", "class", "my_file", "my-file"]
    print("\n  Testing identifier validity using str.isidentifier():")
    for name in test_identifiers:
        is_valid = name.isidentifier()
        import keyword
        is_kw = keyword.iskeyword(name)
        status = "VALID" if (is_valid and not is_kw) else "INVALID"
        reason = "Keyword" if is_kw else ("Valid" if is_valid else "Illegal characters/starts with digit")
        print(f"    - {name:<12}: {status:<8} ({reason})")

    # 3. PVM Information
    print("\n[3] Python Interpreter & Virtual Machine Information:")
    print(f"  Python Version : {sys.version.split()[0]}")
    print(f"  Implementation : {sys.implementation.name.upper()} (CPython)")
    print(f"  Byte Order     : {sys.byteorder}")

    # 4. Primitive Data Types
    print("\n[4] Primitive Data Types (Single Atomic Values):")
    var_int = 42
    var_float = 3.14159
    var_str = "Hello, 10kCoders!"
    var_bool = True
    var_complex = 2 + 3j

    primitives = [
        ("int", var_int),
        ("float", var_float),
        ("str", var_str),
        ("bool", var_bool),
        ("complex", var_complex)
    ]
    for type_name, val in primitives:
        print(f"  {type_name:<8} : value = {str(val):<20} | type = {type(val).__name__:<8} | size = {sys.getsizeof(val)} bytes")

    # 5. Non-Primitive Data Types
    print("\n[5] Non-Primitive Data Types (Collections / Multiple Values):")
    var_list = [10, 20, 30, 40]
    var_tuple = ("Python", 3.12, True)
    var_dict = {"name": "Sudheer", "role": "Developer", "batch": "102R"}
    var_set = {101, 102, 103, 101}  # Automatically removes duplicate 101

    non_primitives = [
        ("list", var_list),
        ("tuple", var_tuple),
        ("dict", var_dict),
        ("set", var_set)
    ]
    for type_name, val in non_primitives:
        print(f"  {type_name:<8} : value = {str(val):<45} | type = {type(val).__name__:<8} | items = {len(val)}")

    print("\n" + "=" * 65)
    print("      ALL ASSIGNMENT 1 CHECKS AND EXAMPLES EXECUTED SUCCESSFULLY")
    print("=" * 65)

if __name__ == "__main__":
    main()
