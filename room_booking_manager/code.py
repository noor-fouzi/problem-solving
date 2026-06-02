class HotelRoom:
    
    def __init__(self, room_number, room_type, max_capacity):
        self.room_number = room_number
        self.room_type = room_type
        self.max_capacity = max_capacity
        self.is_occupied = False
        self.current_guests = 0
    
    def check_in(self, guest_count):

        if self.is_occupied:
            print(f"Error: Room {self.room_number} is already occupied!")

        else:
            if guest_count > self.max_capacity:
                print("Error: Exceeds room capacity!")

            else:
                self.is_occupied = True
                self.current_guests = guest_count
                print(f"Successfully checked into Room {self.room_number}!")

    def check_out(self, nights_stayed, price_per_night):

        cost = 0.0

        if self.is_occupied:
            self.is_occupied = False
            self.current_guests = 0
            cost = round(nights_stayed * price_per_night, 2)

        else:
            print("Error: Room is already vacant!")

        return cost


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