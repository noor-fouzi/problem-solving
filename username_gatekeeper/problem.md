### 🛠️ Problem 01: The "New User" Gatekeeper
**Level:** Easy

**Scenario:** You are building the signup logic for a new social media platform. Before we save a user to our database, we need to ensure their chosen username meets our security and formatting standards.

**The Requirements:**
Write a Python function `validate_username(username)` that checks the following:

1. **Length:** The username must be between **5 and 15 characters** (inclusive).

2. **Alpha-Numeric:** It can only contain letters and numbers. No spaces or special characters (like `@`, `#`, `!`).

3. **Prohibited Word:** For branding reasons, the username cannot be the word `"admin"` (case-insensitive).

**The Task:**
The function should return `True` if the username is valid, and `False` if it fails any of the rules.