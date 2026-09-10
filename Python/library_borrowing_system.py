"""
University Library Book Borrowing System
Topic: Conditional Statements Practice in Python
Course / Track: 10kCoders - 102R
Author: Sudheer Gadde

Tasks / Requirements:
1. Accept book availability, membership status (active/inactive), and number of books currently borrowed.
2. Implement conditional logic:
   - Condition A: The book must be available.
   - Condition B: The borrower must have an active membership status.
   - Condition C: The borrower must not have borrowed more than 3 books (limit <= 3).
3. Output whether borrowing is approved or denied, providing specific reasons upon denial.
4. Comprehensive test suite demonstrating all logical permutations and edge cases.
"""

from typing import Tuple, List

# Maximum allowed borrowed books before borrowing another book
MAX_ALLOWED_BORROWED_BOOKS = 3


def check_borrowing_eligibility(
    is_available: bool,
    membership_status: str,
    books_borrowed: int
) -> Tuple[bool, List[str]]:
    """
    Evaluates borrowing eligibility based on library business rules.

    Args:
        is_available: True if the requested book is in stock, False otherwise.
        membership_status: 'active' or 'inactive' (case-insensitive).
        books_borrowed: Integer count of books the borrower currently possesses.

    Returns:
        Tuple[bool, List[str]]:
            - bool: True if all borrowing conditions are met, False otherwise.
            - List[str]: List of failure reasons if denied, or success message if approved.
    """
    reasons_for_denial: List[str] = []

    # Rule 1: Book Availability Check
    if not is_available:
        reasons_for_denial.append("The requested book is currently unavailable (already checked out).")

    # Rule 2: Membership Status Check (Active / Inactive)
    cleaned_status = membership_status.strip().lower()
    if cleaned_status != "active":
        reasons_for_denial.append(
            f"Borrower's membership status is '{membership_status}'. Active membership is required."
        )

    # Rule 3: Borrowing Quota Check (Must not have borrowed more than 3 books)
    if books_borrowed > MAX_ALLOWED_BORROWED_BOOKS:
        reasons_for_denial.append(
            f"Borrowing limit exceeded: Member has already borrowed {books_borrowed} books "
            f"(Maximum allowed is {MAX_ALLOWED_BORROWED_BOOKS})."
        )
    elif books_borrowed < 0:
        reasons_for_denial.append("Invalid input: Number of borrowed books cannot be negative.")

    # Final Decision using Conditional Logic
    if len(reasons_for_denial) == 0:
        return True, ["All eligibility criteria met. Book borrowing approved!"]
    else:
        return False, reasons_for_denial


def process_borrowing_request(
    book_title: str,
    is_available: bool,
    membership_status: str,
    books_borrowed: int
) -> None:
    """
    Processes a borrowing request and displays a detailed decision summary.
    """
    print("-" * 65)
    print(f"📖 Processing Request for: '{book_title}'")
    print(f"   • Book Available       : {'Yes' if is_available else 'No'}")
    print(f"   • Membership Status    : {membership_status.title()}")
    print(f"   • Current Books Held   : {books_borrowed}")
    print("   -------------------------------------------------------------")

    approved, messages = check_borrowing_eligibility(
        is_available, membership_status, books_borrowed
    )

    if approved:
        print("   STATUS: ✅ APPROVED")
        print(f"   MESSAGE: {messages[0]}")
    else:
        print("   STATUS: ❌ DENIED")
        print("   REASON(S) FOR DENIAL:")
        for idx, reason in enumerate(messages, start=1):
            print(f"     {idx}. {reason}")
    print("-" * 65)


def run_all_test_scenarios() -> None:
    """
    Executes a structured test matrix covering all conditional branches.
    """
    print("\n" + "=" * 65)
    print("   UNIVERSITY LIBRARY BORROWING SYSTEM - TEST SCENARIOS")
    print("=" * 65 + "\n")

    test_cases = [
        {
            "scenario": "Scenario 1: Ideal Case (All conditions valid)",
            "title": "Introduction to Python Programming",
            "available": True,
            "status": "active",
            "borrowed": 1
        },
        {
            "scenario": "Scenario 2: Book is Unavailable",
            "title": "Clean Code Architecture",
            "available": False,
            "status": "active",
            "borrowed": 2
        },
        {
            "scenario": "Scenario 3: Inactive Membership Status",
            "title": "Data Structures & Algorithms in Python",
            "available": True,
            "status": "inactive",
            "borrowed": 1
        },
        {
            "scenario": "Scenario 4: Boundary Limit (Exactly 3 books held)",
            "title": "Artificial Intelligence: A Modern Approach",
            "available": True,
            "status": "active",
            "borrowed": 3  # Not more than 3 -> Allowed
        },
        {
            "scenario": "Scenario 5: Exceeded Limit (4 books held)",
            "title": "Deep Learning with PyTorch",
            "available": True,
            "status": "active",
            "borrowed": 4  # More than 3 -> Denied
        },
        {
            "scenario": "Scenario 6: Multiple Violations (Inactive + Limit Exceeded + Unavailable)",
            "title": "Design Patterns Explained",
            "available": False,
            "status": "inactive",
            "borrowed": 5
        },
        {
            "scenario": "Scenario 7: Edge Case (Negative borrowed count)",
            "title": "Operating System Concepts",
            "available": True,
            "status": "active",
            "borrowed": -1
        }
    ]

    for tc in test_cases:
        print(f"▶ [{tc['scenario']}]")
        process_borrowing_request(
            book_title=tc["title"],
            is_available=tc["available"],
            membership_status=tc["status"],
            books_borrowed=tc["borrowed"]
        )
        print()


def interactive_library_prompt() -> None:
    """
    Prompts the user interactively in the terminal to evaluate a custom request.
    """
    print("\n" + "=" * 65)
    print("         INTERACTIVE LIBRARY BORROWING EVALUATOR")
    print("=" * 65)

    title = input("Enter book title: ").strip() or "General Library Book"

    avail_input = input("Is the book available? (yes/no): ").strip().lower()
    is_available = avail_input in ["yes", "y", "true", "1"]

    membership_status = input("Enter borrower membership status (active/inactive): ").strip()

    while True:
        borrowed_input = input("Enter number of books currently borrowed: ").strip()
        try:
            books_borrowed = int(borrowed_input)
            break
        except ValueError:
            print("❌ Invalid number. Please enter an integer.")

    print("\n[Evaluating Custom Request...]")
    process_borrowing_request(title, is_available, membership_status, books_borrowed)


if __name__ == "__main__":
    # Execute full automated test suite demonstrating all conditional paths
    run_all_test_scenarios()
