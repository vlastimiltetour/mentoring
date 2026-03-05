from dataclasses import dataclass
from datetime import datetime, timedelta, time
from typing import Optional, TYPE_CHECKING
from app.models.person import Person
from app.models.interviewer import Interviewer
from app.models.candidate import Candidate
from app.models.timeslot import TimeSlot
from app.models.workhours import WorkHours
from app.models.interview import Interview
from app.dao.person_dao import PersonDao
from app.dao.interview_dao import InterviewDao
from app.dao.timeslot_dao import TimeSlotDao

class Availability:
    def __init__(self, now: None | datetime, calendar_period: datetime, workhours: WorkHours):
        # get slots from a calendar
        self.workhours = workhours
        
        if now is None: # Checking Identity	"is" -> Memory address	Checking against None, True, or False.
            self.now = datetime.now()
        else:
            self.now = now

        self.truncate_to_whole_hours()
        self.calendar_period = calendar_period

        # get holidays TODO

    def truncate_to_whole_hours(self):
        self.now = self.now.replace(minute=0, second=0, microsecond=0)
        return self.now

    def is_within_workhours(self, slot):
        if slot.weekday() not in self.workhours.workdays:
            return False 
        
        if slot.time() < self.workhours.start:
            return False 
        
        if slot.time() > self.workhours.end:
            return False 
        
        return True

    def get_unavailable_slots(self, person: "Candidate | Interviewer"):
        slots_db = TimeSlotDao()
        retrieved_slots = slots_db.get_blocked_slots_by_person(person.id)

        return retrieved_slots

    def get_slots_per_person(self, person: "Candidate | Interviewer", slot_duration: int, timeframe: datetime):
        available_slots = []
        blocked_slots = self.get_unavailable_slots(person)
        duration = timedelta(minutes=slot_duration)
        start_time = self.now
    
        # for slot in timeframe
        # start time = now
        while start_time < timeframe:
            # iterate and check    
            # if slot in calendar
            if start_time > self.calendar_period:
                
                start_time += duration 
                continue #continue to check other conditions
            # if slot in workhours
            if not self.is_within_workhours(start_time):
                
                start_time += duration 
                continue #continue to check other conditions
            # if slot not blocked
            for slot in blocked_slots: #TODO need to conver this into a time
                
                if slot.start <= start_time and start_time < slot.end:
                    
                    start_time += duration
                    break # break as I won't check any other condition   # <--- "found a problem! Skip the 'else' and don't add this time."
            
            # append 
            else:
                # <--- "checked everything and found NO problems."
                available_slots.append(start_time)
                start_time += duration 

        return available_slots

    
