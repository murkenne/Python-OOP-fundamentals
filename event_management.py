'''Task 2: Event Management System Enhancement

- Problem Statement: Extend an existing Event class by adding a feature to keep
track of the number of participants. 
Implement a method add_participant that increases the 
count and a method get_participant_count to retrieve the current count.
'''

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0
        
    def add_participant(self):
        self.participant_count += 1
        print(f"Participant added. Total participants: {self.participant_count}")
    
    def get_participant_count(self):
        return self.participant_count


event_1 = Event("Tech Conference", "2024-10-01")

event_1.add_participant()  # Adds a participant
event_1.add_participant()  # Adds another participant

# Print the current participant count
print(f"Current participant count: {event_1.get_participant_count()}")
