## Problem 13: Decentralized Ride-Sharing Fleet Tracker

### What is a Ride-Sharing Fleet Tracker?
Think of a ride-sharing fleet tracker as the central control room for companies like Uber or Lyft.

Instead of managing everything through a giant spreadsheet, the tracker uses software to coordinate two main components:

1. **The Vehicles (The Units)**: Individual cars scattered across different cities. Each car continuously reports its ID, where it is right now, and whether it is empty or currently carrying a passenger.

2. **The Dispatcher (The Brain)**: A central scheduling engine that monitors all vehicles in a specific region. When a customer requests a ride, the dispatcher instantly scans its live asset list, finds an empty car in that customer's city, and changes that car's status from "available" to "busy" while routing it to the new destination.

### The Problem to Solve
You need to build a simplified version of this backend dispatch engine using two interacting objects: a `Vehicle` blueprint and a `FleetDispatcher` blueprint.

### 1. The Vehicle Component
Create a class that models an individual car. It needs to store:

- A unique identifier (e.g., `"V-101"`).

- Its current city location.

- Its availability status (whether it can accept a passenger or not).

### 2. The Dispatcher Component
Create a class that models the central management engine for a region. It needs to handle two operations:

- **Registration**: A way to add new vehicle objects to its monitored tracking list.

- **Ride Matching**: A method that takes a customer's `pickup_city` and `destination_city`, searches its tracked list for a car that is both physically located in that city and free to take a ride, and updates that specific car's internal data to reflect its new destination and busy status.

If no car meets the requirements, it must reject the request. If a car is found, it must return that specific updated vehicle object.

### Requirements
1. `Vehicle` **Class**

    - Constructor accepts: `vehicle_id` (string), `initial_base_city` (string).

    - Internal attributes to track: vehicle ID, current city, and availability status (defaults to `True`).

2. `FleetDispatcher` **Class**

    - Constructor accepts: `region_name` (string).

    - Internal attributes to track: region name, and a list containing registered vehicles (starts empty).

    - `register_vehicle(self, vehicle_object)`: Adds a Vehicle instance to the active fleet list.

    - `request_ride(self, pickup_city, destination_city)`: Sweeps the registered fleet to find the first available vehicle currently in the `pickup_city`.

        - If no valid match is found, print a denial message and return `None`.

        - If a match is found, mutate that specific vehicle's internal availability status to `False`, update its location to the `destination_city`, print a dispatch message containing the vehicle ID and destination, and return the mutated vehicle object.