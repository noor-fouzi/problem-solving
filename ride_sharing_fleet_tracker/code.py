class Vehicle:

    def __init__(self, vehicle_id, current_location):
        self.vehicle_id = vehicle_id
        self.current_location = current_location
        self.is_available = True


class Dispatcher:

    def __init__(self, region_name):
        self.region_name = region_name
        self.monitored_vehicles = []

    def register_vehicle(self, vehicle):
        if vehicle not in self.monitored_vehicles:
            self.monitored_vehicles.append(vehicle)
            print(f"Vehicle {vehicle.vehicle_id} is registered successfully.")
        
        else:
            print(f"Vehicle {vehicle.vehicle_id} is already registered.")

    def match_ride(self, pickup_city, destination_city):

        for vehicle in self.monitored_vehicles:
            if vehicle.is_available and vehicle.current_location == pickup_city:
                print(f"Vehicle {vehicle.vehicle_id} is ready to go to {destination_city}!")
                vehicle.is_available = False
                vehicle.current_location = destination_city
                return
            
            else:
                print("There are no available vehicles.")
                return
            

if __name__ == "__main__":
    vehicle_01 = Vehicle("V-01", "Al-Mukalla")
    vehicle_02 = Vehicle("V-02", "Fowa")
    vehicle_03 = Vehicle("V-03", "Al-Mukalla")

    dispatcher = Dispatcher("Al-Mukalla City")
    
    vehicle_01.is_available = False

    dispatcher.register_vehicle(vehicle_01)
    dispatcher.register_vehicle(vehicle_02)
    dispatcher.register_vehicle(vehicle_03)

    dispatcher.match_ride("Asshafii", "Al-Mukalla")
    dispatcher.match_ride("Al-Mukalla", "Addiss")