### 🚀 Problem 12: The Autonomous Logistics Warehouse Drone
**Level:** Hard (Advanced OOP State Machine + Mutually Exclusive Gating)

**Scenario:** An automated fulfillment center utilizes smart drones to transfer inventory pallets. You must build the state-tracking engine for a drone object that dynamically evaluates operational battery drainage thresholds, payload weight capacities, and multi-stage execution routing.

### 📋 System Requirements
Write a Python class named `LogisticsDrone`.

### 1. The Constructor (`__init__`)
Accepts two structural parameters upon instantiation:
- `drone_id` (string)
- `max_weight_capacity` (float - in kilograms)

Automatically initializes three default internal operational state attributes:
- `self.battery_level = 100.0` (Float representing battery percentage)
- `self.current_payload_weight = 0.0` (Float tracking loaded weight)
`self.status = "IDLE"` (String tracking current machine state. Allowed states: `"IDLE"`, `"LOADED"`, `"IN_FLIGHT"`)

### 2. Method 1: `load_payload(self, weight)`
- **Guardrail A (Status Conflict)**: If the drone status is not `"IDLE"`, print: `"Error: Drone [drone_id] is not ready for loading!"` and deny the operation.
- **Guardrail B (Capacity Breach)**: If the target `weight` strictly exceeds `max_weight_capacity`, print: `"Error: Payload exceeds maximum weight capacity!"` and deny the operation.
- **Success Path:** Update `self.current_payload_weight` to the incoming weight value, transition `self.status` to `"LOADED"`, and print: `"Payload of [weight]kg loaded successfully."`

### 3. Method 2: `execute_flight(self, distance_km)`
- **Guardrail A (Status Conflict)**: If the drone status is not `"LOADED"`, print: `"Error: Drone must be loaded before flight execution!"` and abort takeoff.
- **Guardrail B (Energy Starvation)**: Flight consumes power based on this formula:
$$\text{Power Required} = (\text{distance\_km} \times 1.5) + (\text{self.current\_payload\_weight} \times 0.5)$$
If the calculated power required strictly exceeds `self.battery_level`, print: `"Aborting Flight: Insufficient battery power required!"` and abort takeoff.
- **Success Path:** Deduct the calculated power from `self.battery_level`. Transition `self.status` to `"IN_FLIGHT"`. Print: `"Drone [drone_id] is in flight."`
### 4. Method 3: `complete_delivery(self)`
- **Guardrail**: If the drone status is not `"IN_FLIGHT"`, print: `"Error: No active delivery in progress!"`
- **Success Path:** Reset `self.current_payload_weight` to `0.0`. Transition `self.status` back to `"IDLE"`. Print: `"Delivery complete. Drone [drone_id] is now IDLE."` Return the remaining `self.battery_level` rounded to 1 decimal place.

### 🎯 Expected Execution Layout
Test the state transitions inside your `if __name__ == "__main__":` block:
```Python
if __name__ == "__main__":
    drone = LogisticsDrone(drone_id="DRN-99", max_weight_capacity=15.0)

    # 1. Attempt invalid flight before loading
    drone.execute_flight(distance_km=10)

    # 2. Attempt overload
    drone.load_payload(weight=20.0)

    # 3. Successful load
    drone.load_payload(weight=10.0)

    # 4. Attempt flight with insufficient battery drain check
    # Distance 60km * 1.5 = 90 + (10kg * 0.5) = 5. Total 95% power needed.
    drone.execute_flight(distance_km=60)

    # 5. Complete cycle
    drone.complete_delivery()
```

**Expected Console Output:**
```Plaintext
Error: Drone must be loaded before flight execution!
Error: Payload exceeds maximum weight capacity!
Payload of 10.0kg loaded successfully.
Drone DRN-99 is in flight.
Delivery complete. Drone DRN-99 is now IDLE.
```