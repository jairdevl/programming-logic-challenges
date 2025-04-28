from datetime import datetime, timedelta

class Member:
    def __init__(self, name, age, preferred_sport, start_date):
        self.name = name
        self.age = age
        self.preferred_sport = preferred_sport
        self.start_date = start_date
        self.activities = []

    def add_activities(self, activity):
        if len(self.activities) < 3:
            self.activities.append(activity)
            print(f"Activity added: {activity} successfully.")
        else:
            print("Error: Member can only have 3 activities.")

class Activity:
    def __init__(self, name, date, max_asistances):
        self.name = name
        self.date = date
        self.max_asistances = max_asistances
        self.asistances = []

    def register(self, member):
        if len(self.asistances) < self.max_asistances:
            self.asistances.append(member)
            print(f"Member {member.name} registered for {self.name} successfully.")
        else:
            print("Error: Maximum number of asistances reached.")

class SportsClub:
    def __init__(self):
        self.members = []
        self.activities = []

    def register_member(self, name, age, preferred_sport):
        if age <= 0:
            print("The age number must be positive.")
            return
        if any(m.name == name and m.preferred_sport == preferred_sport for m in self.members):
            print("Error: Member already exists.")
            return
        start_date = datetime.now()
        new_member = Member(name, age, preferred_sport, start_date)
        self.members.append(new_member)
        print(f"Member {name} added successfully.")
    
    def program_activity(self, name, date, max_asistances):
        new_activity = Activity(name, date, max_asistances)
        self.activities.append(new_activity)
        print(f"Activity {name} programmed a {date} successfully.")
    
    def list_members(self):
        print("Active members:")
        for member in self.members:
            print(f"{member.name} - {member.age} years - {member.preferred_sport}")
        
    def list_activities(self):
        print("Activities:")
        for activity in self.activities:
            print(f"{activity.name} - {activity.date} - {activity.max_asistances} asistances")
    
    def generate_report(self):
        total_members = len(self.members)
        total_activities = len(self.activities)
        total_asistances = sum(len(activity.asistances) for activity in self.activities)
        average_attendece = total_asistances / total_activities if total_activities > 0 else 0
        
        print("\nReport monthly:")
        print(f"Total new members: {total_members}")
        print(f"Amount activities: {total_activities}")
        print(f"Average attendance: {average_attendece:.2f}")

    def sed_reminder(self):
        date_now = datetime.now()
        for member in self.members:
            if member.start_date + timedelta(days=365) - date_now < timedelta(days=30):
                print(f"Reminder: {member.name} will be a year old soon.")

# Example usage:
club = SportsClub()
club.register_member("John Doe", 30, "Football")
club.register_member("Jane Smith", 25, "Basketball")
club.register_member("John Doe", 30, "Football")
club.program_activity("Football", datetime(2025, 5, 10), 10)
club.program_activity("Basketball", datetime(2025, 5, 15), 8)
club.list_members()
club.list_activities()
club.generate_report()
club.sed_reminder()