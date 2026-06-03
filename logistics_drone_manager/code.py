class LogisticsDrone:

    ALLOWED_STATUS = {"IDLE", "LOADED", "IN_FLIGHT"}
    
    def __init__(self, drone_id, max_weight_capacity):
        self.drone_id = drone_id
        self.max_weight_capacity = max_weight_capacity
        self.battery_level = 100.0
        self.current_payload_weight = 0.0
        self.status = "IDLE"

    def load_payload(self, weight):
        if self.status != "IDLE":
            print(f"Error: Drone {self.drone_id} is not ready for loading!")

        else:
            if weight > self.max_weight_capacity:
                print("Error: Payload exceeds maximum weight capacity!")

            else:
                self.status = "LOADED"
                self.current_payload_weight = weight

    def execute_flight(self, distance_km):
        required_power = (distance_km * 1.5) + (self.current_payload_weight * 0.5)

        if self.status != "LOADED":
            print("Error: Drone must be loaded before flight execution!")

        else:
            if required_power > self.battery_level:
                print("Aborting Flight: Insufficient battery power required!")

            else:
                self.status = "IN_FLIGHT"
                self.battery_level -= required_power

    def complete_delivery(self):
        if self.status != "IN_FLIGHT":
            print("Error: No active delivery in progress!")

        else:
            self.current_payload_weight = 0.0
            self.status = "IDLE"
            print(f"Delivery completed. Drone {self.drone_id} is now IDLE.")

        return round(self.battery_level, 1)


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