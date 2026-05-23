## 🛠️ Problem 07: The Configuration Profile Merging Engine
**Level:** Medium-Hard

**Scenario:** When running automated test suites across different environments (like Local, Staging, and Production), configuration parameters often change.

Your testing framework reads a base setup configuration dictionary, but then it pulls a separate list of system environment updates. Your job is to build a configuration merger that combines these two data structures. However, different development teams configured the updates differently: some are key-value dictionaries, and some are tuples of key-value pairs!

### 📋 System Requirements
Write an environment merger function that takes base_config and applies the runtime_overrides stream to generate a single, final execution configuration map.

### Your Strict Constraints:
1. **Handling Mixed Structures:** Your engine must dynamically determine the data type of each override item inside the loop:

- If the item is a **dictionary**, extract its "key" and "value".

- If the item is a **tuple**, unpack it directly into key, value.

2. **The Security Whitelist Guardrail:** The testing infrastructure only supports specific system keys. You must create a strict whitelist set:
```python
whitelist = {"browser", "headless", "timeout_seconds", "retry_attempts", "reporter", "network_emulation", "experimental_mode"}
```

If an override contains a key that is **not** inside this whitelist (like "unknown_flag"), your code must skip it entirely and must not let it pollute the final configuration map.

3. **Data Type Preservation:** Ensure that values retain their native types (booleans stay booleans, integers stay integers, strings stay strings).

### 🎯 Expected Target Output Layout
Your final returned dictionary should modify the base setup while safely appending the approved new environmental flags:
```python
{
    "browser": "Chrome",
    "headless": True,               # Overwritten from Dict
    "timeout_seconds": 45,          # Overwritten from Tuple
    "retry_attempts": 5,            # Overwritten from Dict
    "reporter": "HTML",             # Retained from Base
    "network_emulation": "4G_Throttled", # New setting added from Tuple
    "experimental_mode": True       # New setting added from Tuple
}
```