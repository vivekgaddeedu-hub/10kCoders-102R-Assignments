# Assignment Report: Interactive Registration Form with HTML & JavaScript

- **Course / Batch:** 10kCoders - 102R
- **Assignment Title:** Creating Interactive Forms with HTML
- **Location:** [`HTML/assig2/registration_form.html`](file:///Users/sudheergadde/Desktop/10kCoders-102R-Assignments/HTML/assig2/registration_form.html)

---

## 1. Objective

The objective of this assignment is to design and build an interactive registration web form utilizing semantic HTML5 form controls, custom CSS styling, and client-side JavaScript validation.

Key learning outcomes:
1. Working with diverse input types (`text`, `email`, `password`, `number`, `checkbox`, `submit`).
2. Structuring forms with semantic `<form>`, `<label>`, `<input>`, and `<button>` elements.
3. Implementing client-side validation logic using HTML5 attributes and JavaScript event listeners.
4. Providing real-time visual feedback (success/error states) and an alert upon successful submission.

---

## 2. Form Architecture & Input Fields

The form is wrapped in a `<form>` element configured with `method="POST"` and a mock action endpoint (`action="https://httpbin.org/post"`).

| Field Label | Input Type | Element ID | Validation Rules Applied |
| :--- | :--- | :--- | :--- |
| **Full Name** | `type="text"` | `fullname` | Required, non-empty, minimum 2 characters |
| **Email Address** | `type="email"` | `email` | Required, standard RFC 5322 email pattern check |
| **Password** | `type="password"` | `password` | Required, minimum 6 characters |
| **Confirm Password** | `type="password"` | `confirm_password` | Required, must match `password` exactly |
| **Age** | `type="number"` | `age` | Required, integer constraint: `18 <= age <= 100` |
| **Newsletter** | `type="checkbox"` | `newsletter` | Optional toggle, defaults to checked |
| **Submit Button** | `<button type="submit">` | `submit-btn` | Triggers JavaScript validation & submission |

---

## 3. Validation Logic & Specifications

### 3.1 Validation Rules:
1. **Full Name Validation:**
   - Checked using `.trim() !== ""` to prevent submissions with only spaces.
   - Minimum length check of 2 characters.
2. **Email Format Validation:**
   - Validated against regular expression: `/^[^\s@]+@[^\s@]+\.[^\s@]+$/`.
3. **Password Confirmation:**
   - Compares the raw value of `password.value === confirm_password.value`.
   - Re-evaluates in real-time as the user types in either field.
4. **Age Boundary Check:**
   - Numerical verification: `18 <= Number(age) <= 100`.
   - Prevents negative, decimal, or out-of-range values.

### 3.2 Dynamic Visual Feedback:
- When a field fails validation, its container receives the `.has-error` CSS class, highlighting the border in crimson red and revealing an explanatory error message below the input.
- When valid, the container receives the `.has-success` CSS class, showing an emerald green border.

---

## 4. JavaScript Integration

The script attaches to the `DOMContentLoaded` event and intercepts the `submit` event:

```javascript
form.addEventListener("submit", function (event) {
  event.preventDefault(); // Intercept submission

  const isNameValid = validateFullName();
  const isEmailValid = validateEmail();
  const isPasswordValid = validatePassword();
  const isConfirmPasswordValid = validateConfirmPassword();
  const isAgeValid = validateAge();

  if (isNameValid && isEmailValid && isPasswordValid && isConfirmPasswordValid && isAgeValid) {
    alert(
      "🎉 Registration Successful!\n\n" +
      "Welcome aboard, " + fullNameInput.value.trim() + "!"
    );
    form.reset();
  }
});
```

---

## 5. Visual Styling & User Experience (UX)

- **Palette & Typography:** Modern dark-mode palette using radial gradients, slate backgrounds, and Google Fonts (`Outfit` for headings, `Inter` for interface elements).
- **Glassmorphic Card:** Floating card with `backdrop-filter: blur(16px)` and elevation drop shadows.
- **Responsiveness:** Fluid grid columns that transition from 2-column password row to single-column stacking on mobile screens (`< 540px`).
