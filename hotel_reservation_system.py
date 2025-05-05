from datetime import datetime, timedelta

class Room:
    def __init__(self, number, room_type, price):
        self.number = number
        self.room_type = room_type
        self.price = price
        self.status = True
        self.reservation = None

class reservation:
    def __init__(self, room, start_date, end_date):
        self.room = room
        self.start_date = start_date
        self.end_date = end_date
        self.total_cost = self.calculate_cost()

    def calculate_cost(self):
        nights = (self.end_date - self.start_date).days
        return nights * self.room.price

class Hotel:
    def __init__(self):
        self.rooms = []
        self.reservations = []

    def add_room(self, room):
        self.rooms.append(room)
    
    def search_available_rooms(self, start_date, end_date):
        available_rooms = []
        for room in self.rooms:
            if room.status == True:
                available_rooms.append(room)
        return available_rooms
    
    def make_reservation(self, room_number, start_date, end_date):
        if start_date < datetime.now().date():
            print("Error: Start date must be in the future.")
            return
        
        for room in self.rooms:
            if room.number == room_number and room.status == True:
                print("The room is already reserved.")
                return
            else:
                reservation = reservation(room, start_date, end_date)
                room.status = False
                room.reservation = reservation
                self.reservations.append(reservation)
                print(f"Reservation for room {room_number} from {start_date} to {end_date} created successfully.")
                return
        print("Error: Room not found.")

    def cancel_reservation(self, room_number):
        for reservation in self.reservations:
            if reservation.room.number == room_number:
                reservation.room.status = True
                self.reservations.remove(reservation)
                print(f"Reservation {room_number} cancelled successfully.")
                return
        print("Error: Reservation not found.")
    
    def generate_daily_report(self):
        total_reservation = len(self.reservations)
        total_earnings = sum(reservation.total_cost for reservation in self.reservations)
        total_income = sum(reservation.total_cost for reservation in self.reservations)
        print(f"Total reservations: {total_reservation}")
        print(f"Total earnings: {total_earnings}")
        print(f"Total income: {total_income}")
    
    def send_reminder(self, room_number):
        for room in self.rooms:
            if room.number == room_number and room.status == True:
                print(f"Reminder: Room {room_number} is available.")
                return
            else:
                print(f"No active reservation found for room {room_number}.")
                return

# Example usage:
hotel = Hotel()
hotel.add_room(Room(101, "Single", 100))
hotel.add_room(Room(102, "Double", 150))
hotel.add_room(Room(103, "Suite", 200))

# Search for available rooms
start_date = datetime.now().date() + timedelta(days=1)
end_date = datetime.now().date() + timedelta(days=2)
available_rooms = hotel.search_available_rooms(start_date, end_date)
print(f"Available rooms: {[r.number for r in available_rooms]}")

# Make a reservation
hotel.make_reservation(101, start_date, end_date)

# Cancel a reservation
hotel.cancel_reservation(101)

# Generate daily report
hotel.generate_daily_report()

# Send reminder
hotel.send_reminder(101)