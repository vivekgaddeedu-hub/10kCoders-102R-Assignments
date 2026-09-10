"""
Dictionary Datatype Assignment: Employee Management System (CRUD Operations)

Topic: Python Dictionary Datatype and CRUD Operations
Course / Track: 10kCoders - 102R
Objective:
    Practice working with the Python dictionary datatype by building a robust
    Employee Information Management System that performs basic CRUD
    (Create, Read, Update, Delete) operations.

Author: Sudheer Gadde
"""

from typing import Dict, Any, Optional


# =====================================================================
# CORE CRUD IMPLEMENTATIONS
# =====================================================================

def create_employee(
    database: Dict[str, Dict[str, Any]],
    employee_id: str,
    name: str,
    age: int,
    department: str
) -> bool:
    """
    [CREATE OPERATION]
    Adds a new employee record to the dictionary database.

    Args:
        database: The master dictionary holding all employee records.
        employee_id: Unique string identifier for the employee.
        name: Full name of the employee.
        age: Age of the employee (must be a positive integer).
        department: Department name where the employee works.

    Returns:
        bool: True if created successfully, False otherwise.
    """
    # Validation 1: Check if the employee ID already exists
    if employee_id in database:
        print(f"❌ [CREATE ERROR]: Employee with ID '{employee_id}' already exists!")
        return False

    # Validation 2: Ensure age is a valid positive integer
    if not isinstance(age, int) or age <= 0:
        print(f"❌ [CREATE ERROR]: Invalid age '{age}'. Age must be a positive integer.")
        return False

    # Validation 3: Ensure non-empty strings for text fields
    if not name.strip() or not department.strip():
        print("❌ [CREATE ERROR]: Name and department cannot be empty strings.")
        return False

    # Create employee dictionary record
    new_employee: Dict[str, Any] = {
        "employee_id": employee_id.strip(),
        "name": name.strip(),
        "age": age,
        "department": department.strip()
    }

    # Store into master dictionary using employee_id as the primary key
    database[employee_id.strip()] = new_employee
    print(f"✅ [CREATE SUCCESS]: Added Employee '{name}' (ID: {employee_id}) to '{department}'.")
    return True


def read_employee(
    database: Dict[str, Dict[str, Any]],
    employee_id: Optional[str] = None
) -> Optional[Dict[str, Any]]:
    """
    [READ OPERATION]
    Retrieves and displays employee information from the dictionary database.
    - If employee_id is provided: Fetches and displays that specific employee.
    - If employee_id is None: Displays all employees in a formatted table.

    Args:
        database: The master dictionary holding all employee records.
        employee_id: Optional ID of a specific employee to retrieve.

    Returns:
        Optional[Dict[str, Any]]: The employee dictionary if found, or None.
    """
    # Case 1: Read specific employee
    if employee_id is not None:
        emp = database.get(employee_id)
        if emp:
            print(f"\n📄 [READ RESULT]: Found Record for Employee ID: {employee_id}")
            print(f"    - Employee ID : {emp['employee_id']}")
            print(f"    - Full Name   : {emp['name']}")
            print(f"    - Age         : {emp['age']}")
            print(f"    - Department  : {emp['department']}")
            return emp
        else:
            print(f"⚠️ [READ NOTICE]: No employee found with ID '{employee_id}'.")
            return None

    # Case 2: Read and display all employees
    print("\n" + "=" * 65)
    print("                 ALL REGISTERED EMPLOYEES")
    print("=" * 65)

    if not database:
        print("  (The employee database is currently empty.)")
        print("=" * 65)
        return None

    # Header
    print(f"{'ID':<10} | {'Name':<22} | {'Age':<5} | {'Department':<20}")
    print("-" * 65)

    # Iterating over dictionary items
    for emp_id, info in database.items():
        print(f"{info['employee_id']:<10} | {info['name']:<22} | {info['age']:<5} | {info['department']:<20}")

    print("=" * 65)
    print(f"Total Employees: {len(database)}\n")
    return None


def update_employee(
    database: Dict[str, Dict[str, Any]],
    employee_id: str,
    name: Optional[str] = None,
    age: Optional[int] = None,
    department: Optional[str] = None
) -> bool:
    """
    [UPDATE OPERATION]
    Modifies details of an existing employee in the dictionary database.

    Args:
        database: The master dictionary holding all employee records.
        employee_id: The ID of the employee to update.
        name: New name (if updating, else None).
        age: New age (if updating, else None).
        department: New department (if updating, else None).

    Returns:
        bool: True if updated successfully, False otherwise.
    """
    # Verify employee existence
    if employee_id not in database:
        print(f"❌ [UPDATE ERROR]: Employee ID '{employee_id}' does not exist.")
        return False

    emp = database[employee_id]
    updates_made = []

    # Update Name
    if name is not None and name.strip():
        old_name = emp["name"]
        emp["name"] = name.strip()
        updates_made.append(f"Name: '{old_name}' -> '{emp['name']}'")

    # Update Age
    if age is not None:
        if isinstance(age, int) and age > 0:
            old_age = emp["age"]
            emp["age"] = age
            updates_made.append(f"Age: {old_age} -> {emp['age']}")
        else:
            print(f"⚠️ [UPDATE WARNING]: Invalid age '{age}'. Age update skipped.")

    # Update Department
    if department is not None and department.strip():
        old_dept = emp["department"]
        emp["department"] = department.strip()
        updates_made.append(f"Department: '{old_dept}' -> '{emp['department']}'")

    if updates_made:
        print(f"✅ [UPDATE SUCCESS]: Updated Employee {employee_id}: {', '.join(updates_made)}")
        return True
    else:
        print(f"ℹ️ [UPDATE NOTICE]: No changes requested for Employee {employee_id}.")
        return False


def delete_employee(
    database: Dict[str, Dict[str, Any]],
    employee_id: str
) -> Optional[Dict[str, Any]]:
    """
    [DELETE OPERATION]
    Removes an employee record from the dictionary database.

    Args:
        database: The master dictionary holding all employee records.
        employee_id: The ID of the employee to remove.

    Returns:
        Optional[Dict[str, Any]]: The deleted employee data if removed, or None.
    """
    # Check if employee exists before attempting deletion
    if employee_id in database:
        # Use .pop() to remove key and retrieve the removed object
        deleted_emp = database.pop(employee_id)
        print(f"🗑️ [DELETE SUCCESS]: Removed Employee '{deleted_emp['name']}' (ID: {employee_id}) from database.")
        return deleted_emp
    else:
        print(f"❌ [DELETE ERROR]: Cannot delete. Employee ID '{employee_id}' not found.")
        return None


# =====================================================================
# EXAMPLE USE CASES & DEMONSTRATION SUITE
# =====================================================================

def run_crud_demonstration() -> None:
    """
    Demonstrates each CRUD operation in sequence with edge cases and formatting.
    """
    print("\n" + "#" * 65)
    print("   STARTING EMPLOYEE DICTIONARY CRUD OPERATIONS DEMONSTRATION")
    print("#" * 65)

    # Initialize empty dictionary database
    employees_db: Dict[str, Dict[str, Any]] = {}

    # -------------------------------------------------------------
    # 1. CREATE OPERATIONS (Adding Employees)
    # -------------------------------------------------------------
    print("\n--- STEP 1: CREATE OPERATIONS ---")
    create_employee(employees_db, "EMP101", "Alice Johnson", 29, "Software Engineering")
    create_employee(employees_db, "EMP102", "Bob Smith", 34, "Data Science")
    create_employee(employees_db, "EMP103", "Catherine Miller", 27, "Product Design")
    create_employee(employees_db, "EMP104", "David Clark", 41, "Cloud Infrastructure")

    # Edge Case: Attempting to insert duplicate employee ID
    print("\n[Testing Edge Case: Duplicate ID]")
    create_employee(employees_db, "EMP101", "Alice Duplicate", 30, "Security")

    # -------------------------------------------------------------
    # 2. READ OPERATIONS (Retrieving Employees)
    # -------------------------------------------------------------
    print("\n--- STEP 2: READ OPERATIONS ---")
    
    # Read All Employees
    print("[Displaying All Employees]")
    read_employee(employees_db)

    # Read Specific Employee by ID
    print("[Reading Specific Employee: EMP102]")
    read_employee(employees_db, "EMP102")

    # Edge Case: Looking up non-existent employee ID
    print("\n[Testing Edge Case: Non-existent Employee Query]")
    read_employee(employees_db, "EMP999")

    # -------------------------------------------------------------
    # 3. UPDATE OPERATIONS (Modifying Details)
    # -------------------------------------------------------------
    print("\n--- STEP 3: UPDATE OPERATIONS ---")

    # Updating Department and Age (e.g., Promotion & Birthday)
    print("[Updating Alice's Department and Age]")
    update_employee(employees_db, "EMP101", age=30, department="Principal Architecture")

    # Updating Name (e.g., correction)
    print("\n[Updating Catherine's Full Name]")
    update_employee(employees_db, "EMP103", name="Catherine Miller-Davis")

    # Edge Case: Updating a non-existent employee ID
    print("\n[Testing Edge Case: Updating Non-existent Employee]")
    update_employee(employees_db, "EMP999", department="Executive")

    # Display records to confirm updates
    print("\n[State of Database After Updates]")
    read_employee(employees_db)

    # -------------------------------------------------------------
    # 4. DELETE OPERATIONS (Removing Employees)
    # -------------------------------------------------------------
    print("--- STEP 4: DELETE OPERATIONS ---")

    # Deleting an existing employee
    print("[Deleting Bob Smith (EMP102)]")
    delete_employee(employees_db, "EMP102")

    # Edge Case: Attempting to delete an already deleted employee ID
    print("\n[Testing Edge Case: Deleting Non-existent Employee]")
    delete_employee(employees_db, "EMP102")

    # -------------------------------------------------------------
    # 5. FINAL READ (Post-Delete Verification)
    # -------------------------------------------------------------
    print("\n--- STEP 5: FINAL VERIFICATION ---")
    print("[Displaying Database Contents After All CRUD Operations]")
    read_employee(employees_db)

    print("#" * 65)
    print("          CRUD DEMONSTRATION COMPLETED SUCCESSFULLY")
    print("#" * 65 + "\n")


# =====================================================================
# OPTIONAL INTERACTIVE CLI MENU
# =====================================================================

def interactive_cli():
    """Interactive command-line interface for manual CRUD testing."""
    db: Dict[str, Dict[str, Any]] = {}
    
    # Preload sample data
    create_employee(db, "EMP101", "Sudheer Gadde", 24, "Full Stack Engineering")
    create_employee(db, "EMP102", "Priya Sharma", 28, "AI & Data Science")

    while True:
        print("\n" + "=" * 45)
        print("   EMPLOYEE MANAGEMENT SYSTEM - CRUD MENU")
        print("=" * 45)
        print("1. Create Employee (Add)")
        print("2. Read All Employees")
        print("3. Read Employee by ID")
        print("4. Update Employee Details")
        print("5. Delete Employee")
        print("6. Run Automated Test Demonstration")
        print("7. Exit")
        print("=" * 45)

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            emp_id = input("Enter Employee ID (e.g., EMP105): ").strip()
            name = input("Enter Employee Name: ").strip()
            try:
                age = int(input("Enter Employee Age: ").strip())
            except ValueError:
                print("❌ Invalid age. Must be an integer.")
                continue
            dept = input("Enter Department: ").strip()
            create_employee(db, emp_id, name, age, dept)

        elif choice == "2":
            read_employee(db)

        elif choice == "3":
            emp_id = input("Enter Employee ID to search: ").strip()
            read_employee(db, emp_id)

        elif choice == "4":
            emp_id = input("Enter Employee ID to update: ").strip()
            if emp_id not in db:
                print(f"❌ Employee ID '{emp_id}' not found.")
                continue
            name = input("Enter New Name (leave blank to skip): ").strip()
            age_str = input("Enter New Age (leave blank to skip): ").strip()
            dept = input("Enter New Department (leave blank to skip): ").strip()

            age_val = int(age_str) if age_str.isdigit() else None
            name_val = name if name else None
            dept_val = dept if dept else None

            update_employee(db, emp_id, name=name_val, age=age_val, department=dept_val)

        elif choice == "5":
            emp_id = input("Enter Employee ID to delete: ").strip()
            delete_employee(db, emp_id)

        elif choice == "6":
            run_crud_demonstration()

        elif choice == "7":
            print("👋 Exiting Employee Management System. Goodbye!")
            break

        else:
            print("❌ Invalid option. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    # By default, run the comprehensive automated demonstration
    run_crud_demonstration()
