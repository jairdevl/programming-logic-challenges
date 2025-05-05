from datetime import datetime

class Event:
    def __init__(self, title, date, start_time, duration, participants):
        self.title = title
        self.date = date
        self.start_time = start_time
        self.duration = duration
        self.participants = participants
    
    def __str__(self):
        return f"Event: {self.title} - Date: {self.date} - Start Time: {self.start_time} - Duration: {self.duration} - Participants: {', '.join(self.participants)}"

class EventManagementSystem:
    def __init__(self):
        self.events = []
    
    def add_event(self, title, date, start_time, duration, participants):
        # Validations
        if duration < 0:
            print("Error: Duration must be greater than 0.")
            return
        
        start_time = datetime.strptime(f"{date} {start_time}", "%Y-%m-%d %H:%M")

        # Check if existing events at the same date and time
        for event in self.events:
            if (event.date == date and event.start_time == start_time):
                print("Error: Event already exists at the same date and time.")
                return
        new_event = Event(title, date, start_time, duration, participants)
        self.events.append(new_event)
        print(f"Event {title} added successfully.")

    def remove_event(self, title):
        for event in self.events:
            if event.title == title:
                self.events.remove(event)
                print(f"Event {title} removed successfully.")
                return
        print(f"Event {title} not found.")
    
    def view_event(self):
        if not self.events:
            print("No events found.")
            return
        for event in self.events:
            print(event)
    def search_event(self, date):
        events = [event for event in self.events if event.date == date]
        if not events:
            print("No events found for the given date.")
            return
        for event in events:
            print(event)
    def daily_events(self, date):
        events = [event for event in self.events if event.date == date]
        print(f"Report for {date}: ")
        print(f"Total events: {len(events)}")
        for event in events:
            print(f"-{event.title}: Participants: {', '.join(event.participants)}")

    def sed_notification(self,):
        for event in self.events:
            print(f"Notification sent to participants of {event.title}: ")
            print(f"Date: {event.date}, start time: {event.start_time}")

    def conclude_event(self, title):
        for event in self.events:
            if event.title == title:
                print(f"Summary of {event.title}: ")
                print(event)
                feedback = input("Enter feedback: ")
                print(f"Feedback: {feedback}")
                self.events.remove(event)
                print(f"Event {title} concluded successfully.")
                return
        print(f"Event {title} not found.")
            
def main():
    system = EventManagementSystem()
    while True:
        print("\nMenu:")
        print("1. Add event")
        print("2. Remove event")
        print("3. View events")
        print("4. Search events")
        print("5. Daily events")
        print("6. Send notification")
        print("7. Conclude event")
        print("8. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter event title: ")
            date = input("Enter event date (YYYY-MM-DD): ")
            start_time = input("Enter event start time (HH:MM): ")
            duration = int(input("Enter event duration (in hours): "))
            participants = input("Enter event participants (comma separated): ").split(",")
            system.add_event(title, date, start_time, duration, participants)
        elif choice == "2":
            title = input("Enter event title to remove: ")
            system.remove_event(title)
        elif choice == "3":
            system.view_event()
        elif choice == "4":
            date = input("Enter event date to search (YYYY-MM-DD): ")
            system.search_event(date)
        elif choice == "5":
            date = input("Enter event date to view daily events (YYYY-MM-DD): ")
            system.daily_events(date)
        elif choice == "6":
            system.sed_notification()
        elif choice == "7":
            title = input("Enter event title to conclude: ")
            system.conclude_event(title)
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()