### 🛠️ Problem 02: The Bulk Processor
**Level:** Medium-Easy

**Scenario:** Our signup page just went viral. Instead of validating one username at a time, our backend is receiving **batches** (lists) of usernames. We need to process them efficiently and provide a summary.

### The Requirements:
Write a function `process_signups(usernames_list)` that:

1. **Iterates** through a list of usernames.

2. **Reuses** your validation logic from Day 1.

3. **Categorizes** them into two lists: `valid` and `invalid`.

4. **Returns a Dictionary** that looks like this:

```Python
{
    "successful_count": 3,
    "failed_count": 2,
    "rejected_usernames": ["list", "of", "failed", "ones"]
}
```

**The Task:**
You need to handle the case where the input list might be **empty**.