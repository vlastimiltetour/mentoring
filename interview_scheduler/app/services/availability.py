from dataclasses import dataclass
from datetime import datetime, timedelta, time
from typing import Optional, TYPE_CHECKING
from app.models.person import Interviewer, Candidate
from app.models.timeslot import WorkHours

class Availability:
    def __init__(self, calendar_period: datetime, workhours: WorkHours):
        # get slots from a calendar
        self.workhours = workhours
        self.now = datetime.now()
        self.calendar_period = calendar_period

        # get holidays

    def is_within_workhours(self, slot):
        print(slot.time(), self.workhours.start)
        if slot.weekday() not in self.workhours.workdays:
            print()
            return False 
        
        if slot.time() < self.workhours.start:
            return False 
        
        if slot.time() > self.workhours.end:
            return False 
        
        return True

    def is_available(self, person: "Candidate | Interviewer", slot: datetime, slot_duration: int):
        

        #is slot within workours?
        print(self.is_within_workhours(slot))
        #is slot not blocked?

        
        
        
        #return True or False 
        pass 

    def get_all_available_slots(self):
        pass 

    def get_slots_per_person(self, person: "Candidate | Interviewer", slot_duration: int, timespan: datetime):

        available_slots = []
        duration = timedelta(minutes=slot_duration)
        start_time = None

        raw_availability = self.all_slots
        
        for slot in raw_availability:
           if slot.owner_id == person.id and slot.status == "available":
                start_time = slot.start 
                while (start_time + duration) <= slot.end:
                    available_slots.append(start_time)          
                    start_time += duration

        return available_slots

    def get_all_available_slots(self):
        return self.all_slots 


@dataclass
class Interview:
    id: int
    candidate: Candidate
    interviewer: Interviewer
    scheduled_slot: TimeSlot

    def __str__(self):
        return f"The interview betweeen {self.candidate} and interviewer {self.interviewer} will take place on {self.scheduled_slot}."

