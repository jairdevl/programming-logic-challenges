import datetime

class Member:
    def __init__(self, name, id_number, registration_date, membership_type):
        self.name = name
        self.id_number = id_number
        self.registration_date = registration_date
        self.membership_type = membership_type
        self.enrolled_classes = []

    def add_class(self, class_instance):
        if len(self.enrolled_classes) < 3:
            self.enrolled_classes.append(class_instance)
            return True
        else:
            return False

    def __str__(self):
        return f"{self.name} (ID: {self.id_number}, Membership: {self.membership_type})"


class Class:
    def __init__(self, name, schedule):
        self.name = name
        self.schedule = schedule
        self.attendees = []

    def add_attendee(self, member):
        self.attendees.append(member)

    def __str__(self):
        return f"Class: {self.name} at {self.schedule}"


class Gym:
    def __init__(self):
        self.members = {}
        self.classes = []
        self.revenue = 0

    def register_member(self, name, id_number, registration_date, membership_type):
        if id_number in self.members:
            print("Error: The ID number is already registered.")
            return False
        if not self.validate_date(registration_date):
            print("Error: The registration date is not valid.")
            return False

        new_member = Member(name, id_number, registration_date, membership_type)
        self.members[id_number] = new_member
        self.revenue += self.get_membership_price(membership_type)
        print(f"Member registered: {new_member}")
        return True

    def schedule_class(self, name, schedule):
        new_class = Class(name, schedule)
        self.classes.append(new_class)
        print(f"Class scheduled: {new_class}")

    def enroll_in_class(self, id_number, class_name):
        member = self.members.get(id_number)
        class_instance = next((c for c in self.classes if c.name == class_name), None)

        if member and class_instance:
            if member.add_class(class_instance):
                class_instance.add_attendee(member)
                print(f"{member.name} has enrolled in the class {class_instance.name}.")
            else:
                print("Error: Cannot enroll in more than 3 classes.")
        else:
            print("Error: Member or class not found.")

    def list_members(self):
        print("Active members:")
        for member in self.members.values():
            print(member)

    def list_classes(self):
        print("Scheduled classes:")
        for class_instance in self.classes:
            print(class_instance)

    def generate_report(self):
        total_members = len(self.members)
        total_attendees = sum(len(class_instance.attendees) for class_instance in self.classes)
        print(f"Monthly Report:\nTotal new members: {total_members}\nTotal class attendance: {total_attendees}\nTotal revenue: ${self.revenue}")

    def validate_date(self, date):
        try:
            datetime.datetime.strptime(date, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def get_membership_price(self, membership_type):
        prices = {
            "monthly": 30,
            "quarterly": 80,
            "annual": 300
        }
        return prices.get(membership_type, 0)

# Example usage
gym = Gym()
gym.register_member("John Doe", "12345", "2025-05-01", "monthly")
gym.register_member("Anna Smith", "12346", "2025-05-02", "quarterly")
gym.schedule_class("Yoga", "10:00 AM")
gym.schedule_class("Pilates", "11:00 AM")
gym.enroll_in_class("12345", "Yoga")
gym.enroll_in_class("12345", "Pilates")
gym.enroll_in_class("12346", "Yoga")
gym.list_members()
gym.list_classes()
gym.generate_report()