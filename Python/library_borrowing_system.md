# Assignment: Conditional Statements Practice in Python

- **Course / Batch:** 10kCoders - 102R
- **Topic:** Python Conditional Statements (`if`, `elif`, `else`) & Logical Operators
- **Application:** Automated University Library Book Borrowing System
- **Executable Script:** [`library_borrowing_system.py`](file:///Users/sudheergadde/Desktop/10kCoders-102R-Assignments/Python/library_borrowing_system.py)

---

## 1. Objective

This assignment focuses on applying Python conditional statements to implement real-world decision-making logic. By building an automated university library borrowing system, we practice:
1. Formulating compound boolean expressions using logical operators (`and`, `or`, `not`).
2. Evaluating relational comparison operators (`==`, `!=`, `<`, `>`, `<=`).
3. Providing clear, specific feedback when conditions fail instead of generic errors.
4. Structuring edge cases and test cases to guarantee 100% conditional branch coverage.

---

## 2. Business Rules & Logic Criteria

An automated library system determines whether a borrower is permitted to borrow a requested book based on three mandatory conditions:

| Rule # | Condition | Valid Criteria | Failure Reason |
| :--- | :--- | :--- | :--- |
| **Rule 1** | Book Availability | Book is in stock (`is_available == True`) | Book is currently checked out / unavailable |
| **Rule 2** | Membership Status | Borrower status is `'active'` | Member account is inactive / suspended |
| **Rule 3** | Borrowing Quota | Currently borrowed books $\le 3$ | Member has exceeded the maximum 3-book limit |

> **Decision Rule:** All three conditions must be satisfied simultaneously for borrowing to be approved. If any condition fails, the system denies borrowing and explicitly lists the reasons.

---

## 3. Implementation Logic

### Multi-Condition Evaluation Pattern
Instead of a single deeply nested `if-else` chain that halts at the first failure, this implementation checks each condition independently and collects all applicable reasons for denial:

```python
def check_borrowing_eligibility(is_available: bool, membership_status: str, books_borrowed: int):
    reasons_for_denial = []

    # Condition 1: Book Availability
    if not is_available:
        reasons_for_denial.append("The requested book is currently unavailable.")

    # Condition 2: Membership Status
    if membership_status.strip().lower() != "active":
        reasons_for_denial.append(f"Borrower's membership status is '{membership_status}'. Active membership is required.")

    # Condition 3: Borrowing Limit (must not exceed 3 books)
    if books_borrowed > 3:
        reasons_for_denial.append(f"Borrowing limit exceeded: Member has already borrowed {books_borrowed} books (Max is 3).")
    elif books_borrowed < 0:
        reasons_for_denial.append("Invalid input: Number of borrowed books cannot be negative.")

    # Final Decision
    if len(reasons_for_denial) == 0:
        return True, ["All eligibility criteria met. Book borrowing approved!"]
    else:
        return False, reasons_for_denial
```

---

## 4. Test Scenarios Matrix

The system was evaluated against 7 distinct test scenarios covering standard operations, boundary conditions, and multi-failure edge cases:

| Scenario | Book Available | Membership Status | Books Borrowed | Expected Outcome | Reason(s) |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **1. Ideal Case** | `True` | `"active"` | `1` | **✅ APPROVED** | All criteria met |
| **2. Unavailable** | `False` | `"active"` | `2` | **❌ DENIED** | Book currently unavailable |
| **3. Inactive Member**| `True` | `"inactive"` | `1` | **❌ DENIED** | Active membership required |
| **4. Boundary Limit** | `True` | `"active"` | `3` | **✅ APPROVED** | Exactly 3 books held (not > 3) |
| **5. Limit Exceeded** | `True` | `"active"` | `4` | **❌ DENIED** | Exceeded 3-book maximum |
| **6. Multi-Failure** | `False` | `"inactive"` | `5` | **❌ DENIED** | Unavailable + Inactive + Limit exceeded |
| **7. Negative Input** | `True` | `"active"` | `-1` | **❌ DENIED** | Count cannot be negative |

---

## 5. Execution Output

```text
=================================================================
   UNIVERSITY LIBRARY BORROWING SYSTEM - TEST SCENARIOS
=================================================================

▶ [Scenario 1: Ideal Case (All conditions valid)]
📖 Processing Request for: 'Introduction to Python Programming'
   STATUS: ✅ APPROVED
   MESSAGE: All eligibility criteria met. Book borrowing approved!

▶ [Scenario 2: Book is Unavailable]
📖 Processing Request for: 'Clean Code Architecture'
   STATUS: ❌ DENIED
   REASON: 1. The requested book is currently unavailable (already checked out).

▶ [Scenario 3: Inactive Membership Status]
📖 Processing Request for: 'Data Structures & Algorithms in Python'
   STATUS: ❌ DENIED
   REASON: 1. Borrower's membership status is 'inactive'. Active membership is required.

▶ [Scenario 4: Boundary Limit (Exactly 3 books held)]
📖 Processing Request for: 'Artificial Intelligence: A Modern Approach'
   STATUS: ✅ APPROVED
   MESSAGE: All eligibility criteria met. Book borrowing approved!

▶ [Scenario 5: Exceeded Limit (4 books held)]
📖 Processing Request for: 'Deep Learning with PyTorch'
   STATUS: ❌ DENIED
   REASON: 1. Borrowing limit exceeded: Member has already borrowed 4 books (Maximum allowed is 3).

▶ [Scenario 6: Multiple Violations (Inactive + Limit Exceeded + Unavailable)]
📖 Processing Request for: 'Design Patterns Explained'
   STATUS: ❌ DENIED
   REASONS:
     1. The requested book is currently unavailable (already checked out).
     2. Borrower's membership status is 'inactive'. Active membership is required.
     3. Borrowing limit exceeded: Member has already borrowed 5 books (Maximum allowed is 3).
```
