from datetime import date

class Member:
    def __init__(self, name, id_number, registration_date, membership_type):
        self.name = name
        self.id_number = id_number
        self.registration_date = registration_date
        self.membership_type = membership_type
        self.classes = []
    def __str__(self):
        return (f"Member: {self.name}, ID Number: {self.id_number}, Membership Type: {self.membership_type}, Classes: {', '.join(self.classes) if self.classes else 'None'}")