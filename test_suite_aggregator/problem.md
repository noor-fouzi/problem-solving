### 🛠️ Problem 03: The System Log Sanitizer
**Level:** Medium-Easy

**Scenario:** Our authentication service dumps a messy system log of login attempts. Some lines are corrupted, some are successful logins, and others are failed hacks. We need to clean this data and filter out security threats before sending it to a database.

**The Input Data:**

Your function will receive a list of raw strings representing logs. Each string follows this exact structural pattern:
`"TIMESTAMP | USERNAME | STATUS_CODE"`

Here is an example payload your system must process:

```Python
raw_logs = [
    "2026-05-17 05:00:12 | noorfouzi | 200",
    "2026-05-17 05:01:45 | admin | 403",
    "MALFORMED_LINE_ERR_909",
    "2026-05-17 05:03:22 | hacker_joe | 403",
    "2026-05-17 05:04:11 | validUser123 | 200"
]
```

**The Requirements:**

Write a new function (name it according to clean-code standards) that parses this list and returns a dictionary containing two keys:

1. `"secure_events"`: A list of user strings that successfully logged in (Status `200`).

2. `"flagged_attempts"`: A list of user strings that were rejected (Status `403`).

### 🔍 Architectural Hints & Guardrails
- **String Manipulation Hint**: Look into Python's `.split()` method. It allows you to chop up a single string into a list of pieces based on a specific delimiter (like a comma, or a vertical pipe `|`).

- **The Data Cleaning Trap (Crucial):** Notice how the logs contain spaces around the vertical pipes (`" | "`). If you split raw strings, your extracted usernames might end up with hidden trailing or leading spaces (e.g., `" noorfouzi "` instead of `"noorfouzi"`). Look up a string method that "shaves" off whitespace from the ends of a string.

- **Edge Case Protection:** Your code *will* hit malformed lines (like `"MALFORMED_LINE_ERR_909"`). If you try to split a line that doesn't have two `|` characters, your index mapping might look for a status code that isn't there and crash the program. You need a structural check to verify a line has the correct amount of data pieces before processing it. If it's malformed, skip it!