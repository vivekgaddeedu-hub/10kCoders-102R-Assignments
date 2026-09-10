"""
Python Assignment: Python Data Types Comprehensive Study
Date Assigned: 25-06-2026
Tech Stack: Python
Topic: Python Data Types (int, str, list, tuple, set, dict)
Author: Sudheer Gadde
Course: 10kCoders - 102R
"""

def section_header(title: str) -> None:
    """Prints a styled section header."""
    print("\n" + "=" * 70)
    print(f"  {title.upper()}")
    print("=" * 70)


def main():
    print("#" * 70)
    print("      PYTHON DATA TYPES COMPREHENSIVE ASSIGNMENT EXECUTION")
    print("      Date: 25-06-2026 | Course: 10kCoders - 102R")
    print("#" * 70)

    # -------------------------------------------------------------
    # 1. Integer (int)
    # -------------------------------------------------------------
    section_header("1. Integer (int)")
    int_example = 42
    big_int = 10**30  # Demonstrating arbitrary precision
    print(f"Example Value         : {int_example}")
    print(f"Data Type             : {type(int_example)}")
    print(f"Large Integer (No overflow): {big_int}")
    print("Key Features:")
    print(" - Represents whole numbers (positive, negative, or zero).")
    print(" - Immutable (cannot be changed in memory after creation).")
    print(" - Arbitrary precision in Python 3 (size limited only by available RAM).")

    # -------------------------------------------------------------
    # 2. String (str)
    # -------------------------------------------------------------
    section_header("2. String (str)")
    str_example = "Hello, Python!"
    print(f"Example Value         : {str_example!r}")
    print(f"Data Type             : {type(str_example)}")
    print(f"Indexing (Index 0)    : {str_example[0]}")
    print(f"Slicing (0 to 5)      : {str_example[0:5]}")
    print("Key Features:")
    print(" - Immutable sequence of Unicode characters.")
    print(" - Enclosed in single, double, or triple quotes.")
    print(" - Supports zero-based indexing and slicing.")

    # -------------------------------------------------------------
    # 3. List (list)
    # -------------------------------------------------------------
    section_header("3. List (list)")
    list_example = ["Python", 3.12, True, "Python"]  # allows duplicates
    print(f"Example Value         : {list_example}")
    print(f"Data Type             : {type(list_example)}")
    # Mutability check
    list_example.append("10kCoders")
    list_example[1] = 3.13
    print(f"After Mutation        : {list_example}")
    print("Key Features:")
    print(" - Ordered collection of heterogeneous elements.")
    print(" - Mutable (elements can be added, changed, or removed in place).")
    print(" - Allows duplicate items.")
    print(" - Supports indexing and slicing.")

    # -------------------------------------------------------------
    # 4. Tuple (tuple)
    # -------------------------------------------------------------
    section_header("4. Tuple (tuple)")
    tuple_example = (10, "Secure", 99.5, 10)  # allows duplicates
    print(f"Example Value         : {tuple_example}")
    print(f"Data Type             : {type(tuple_example)}")
    print(f"Indexing (Index 1)    : {tuple_example[1]}")
    print("Key Features:")
    print(" - Ordered, immutable sequence of heterogeneous elements.")
    print(" - Once created, elements cannot be modified, added, or removed.")
    print(" - Allows duplicate items.")
    print(" - Supports indexing and slicing.")
    print(" - Memory efficient and can be used as dictionary keys if items are immutable.")

    # -------------------------------------------------------------
    # 5. Set (set)
    # -------------------------------------------------------------
    section_header("5. Set (set)")
    # Duplicate 'apple' and 'banana' are passed
    set_example = {"apple", "banana", "cherry", "apple", "banana"}
    print(f"Defined with duplicates: {{'apple', 'banana', 'cherry', 'apple', 'banana'}}")
    print(f"Resulting Set         : {set_example} (Duplicates removed automatically)")
    print(f"Data Type             : {type(set_example)}")
    set_example.add("orange")
    print(f"After set.add('orange'): {set_example}")
    print("Key Features:")
    print(" - Unordered collection of unique, hashable elements.")
    print(" - Automatically deduplicates elements.")
    print(" - Mutable (can add/remove elements), but does not allow mutable elements.")
    print(" - Does NOT support indexing or slicing.")

    # -------------------------------------------------------------
    # 6. Dictionary (dict)
    # -------------------------------------------------------------
    section_header("6. Dictionary (dict)")
    dict_example = {"id": 101, "name": "Sudheer", "role": "Developer"}
    print(f"Example Value         : {dict_example}")
    print(f"Data Type             : {type(dict_example)}")
    dict_example["role"] = "Full Stack Engineer"  # updating value
    dict_example["batch"] = "102R"                 # adding new key-value pair
    print(f"After Mutation        : {dict_example}")
    print("Key Features:")
    print(" - Key-value pair mapping structure enclosed in curly braces {}.")
    print(" - Keys must be unique and immutable (hashable).")
    print(" - Values can be duplicates, mutable, and of any data type.")
    print(" - Maintains insertion order (guaranteed in Python 3.7+).")
    print(" - Mutable; supports fast O(1) average lookup via keys.")

    # -------------------------------------------------------------
    # 7. Mutability Classification
    # -------------------------------------------------------------
    section_header("7. Mutability Classification")
    print("• MUTABLE Data Types    : list, dict, set")
    print("  (Can be changed in place without creating a new object)")
    print("\n• IMMUTABLE Data Types  : int, float, str, tuple, bool, complex, frozenset")
    print("  (Cannot be changed in place; modifications create new objects in memory)")

    # -------------------------------------------------------------
    # 8. Duplicate Values Classification
    # -------------------------------------------------------------
    section_header("8. Duplicate Values Support")
    print("• ALLOWS Duplicates     : list, tuple, str (repeated characters), dict (values only)")
    print("• DISALLOWS Duplicates  : set, dict (keys must be unique)")

    # -------------------------------------------------------------
    # 9. Insertion Order Preservation
    # -------------------------------------------------------------
    section_header("9. Insertion Order Preservation")
    print("• MAINTAINS Order       : list, tuple, str, dict (Python 3.7+)")
    print("• DOES NOT Maintain     : set (unordered, hashed)")

    # -------------------------------------------------------------
    # 10. Indexing and Slicing Support
    # -------------------------------------------------------------
    section_header("10. Indexing and Slicing Support")
    print("• SUPPORTS Index/Slice  : str, list, tuple (Sequence types with positional indices)")
    print("• DOES NOT Support      : int (scalar), set (unordered), dict (keyed lookup, not indexed)")

    # -------------------------------------------------------------
    # 11. Type Check Verification for Each Data Type
    # -------------------------------------------------------------
    section_header("11. Example of Each Data Type with type()")
    data_samples = [
        ("Integer", 100),
        ("String", "Python 3"),
        ("List", [1, 2, 3]),
        ("Tuple", (1, 2, 3)),
        ("Set", {1, 2, 3}),
        ("Dictionary", {"a": 1, "b": 2})
    ]
    print(f"{'Category':<15} | {'Value Representation':<25} | {'type() Result':<25}")
    print("-" * 70)
    for category, val in data_samples:
        print(f"{category:<15} | {str(val):<25} | {str(type(val)):<25}")

    # -------------------------------------------------------------
    # 12. Feature Comparison Table
    # -------------------------------------------------------------
    section_header("12. Comparison Table Across Data Types")
    col_w = [8, 11, 10, 12, 16, 10]
    headers = ["Type", "Mutable?", "Ordered?", "Duplicates?", "Index/Slice?", "Syntax"]
    row_fmt = f"{headers[0]:<{col_w[0]}} | {headers[1]:<{col_w[1]}} | {headers[2]:<{col_w[2]}} | {headers[3]:<{col_w[3]}} | {headers[4]:<{col_w[4]}} | {headers[5]:<{col_w[5]}}"
    print(row_fmt)
    print("-" * 78)

    table_data = [
        ("int", "Immutable", "N/A", "N/A", "No", "42"),
        ("str", "Immutable", "Yes", "Yes", "Yes", "'text'"),
        ("list", "Mutable", "Yes", "Yes", "Yes", "[1, 2]"),
        ("tuple", "Immutable", "Yes", "Yes", "Yes", "(1, 2)"),
        ("set", "Mutable", "No", "No", "No", "{1, 2}"),
        ("dict", "Mutable", "Yes (3.7+)", "Keys:No / Val:Yes", "Key Lookup", "{k: v}")
    ]
    for row in table_data:
        print(f"{row[0]:<{col_w[0]}} | {row[1]:<{col_w[1]}} | {row[2]:<{col_w[2]}} | {row[3]:<{col_w[3]}} | {row[4]:<{col_w[4]}} | {row[5]:<{col_w[5]}}")

    print("\n" + "#" * 70)
    print("           ALL 12 QUESTIONS EXECUTED AND VERIFIED")
    print("#" * 70 + "\n")


if __name__ == "__main__":
    main()
