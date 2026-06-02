### 🚀 Problem 12: The Smart Hotel Room Booking Manager
**Level:** Medium-Hard (Week 3 Logic Gating + OOP State Tracking)

**Scenario:** A luxury resort wants to automate its room booking engine. Instead of managing room numbers and availability statuses via messy matrices, they want a dedicated object model for each room that can self-evaluate booking availability, enforce safety capacities, and cleanly compute checkout bills.

### 📋 System Requirements
Write a Python class named `HotelRoom`.

### Your Structural Constraints:
1. **The Constructor** (`__init__`): The constructor must accept three parameters when initialized:
    - `room_number` (int)
    - `room_type` (string - e.g., `"Suite"`, `"Standard"`)
    - `max_capacity` (int - maximum number of guests allowed)
2. **Default Object States:** The constructor must automatically initialize two fixed state variables without taking them as parameters:
    - `self.is_occupied = False` (Boolean tracking if someone is currently checked in)
    - `self.current_guests = 0` (Integer tracking the exact guest count)
3. **Method 1:** `check_in(self, guest_count)`
    - **Guardrail A (Double-Booking Check):** If the room is *already occupied* (`self.is_occupied` is `True`), print: `"Error: Room [room_number] is already occupied!"` and refuse the check-in.
    - **Guardrail B (Capacity Check):** If the room is empty, but the incoming `guest_count` strictly exceeds the room's `max_capacity`, print: `"Error: Exceeds room capacity!"` and refuse the check-in.
    - **Success Path:** If both gates pass, set `self.is_occupied` to `True`, set `self.current_guests` to the incoming `guest_count`, and print: `"Successfully checked into Room [room_number]!"`
4. **Method 2:** `check_out(self, nights_stayed, price_per_night)`
    - **Guardrail:** If the room is already vacant when checkout is attempted, print: `"Error: Room is already vacant!"` and return `0.0`.
    - **Success Path:** Calculate the total stay cost ($nights \times price$). Reset the room's tracking states entirely (`is_occupied` back to `False`, `current_guests` back to `0`). Return the total financial cost as a **pure float rounded to 2 decimal places**.
    
### 🎯 Expected Execution Layout
Test your logic gating inside your `if __name__ == "__main__":` block with this scenario:


```Python
if __name__ == "__main__":
    # 1. Create a luxury honeymoon suite for up to 2 guests
    room_302 = HotelRoom(room_number=302, room_type="Suite", max_capacity=2)

    # 2. Try to sneak 4 people into the suite (Should trigger capacity guardrail)
    room_302.check_in(4)

    # 3. Check in a valid couple
    room_302.check_in(2)

    # 4. Try to double-book another guest while they are there (Should trigger occupancy guardrail)
    room_302.check_in(1)

    # 5. Check out after a 3-night stay at $150.50 per night
    bill = room_302.check_out(nights_stayed=3, price_per_night=150.50)
    print(f"Checkout Total: ${bill}")
```


### Expected Console Output:
```Plaintext
Error: Exceeds room capacity!
Successfully checked into Room 302!
Error: Room 302 is already occupied!
Checkout Total: $451.5
```