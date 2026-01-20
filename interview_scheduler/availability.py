from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Optional, TYPE_CHECKING
from person import Interviewer, Candidate

@dataclass
class TimeSlot:
    start: datetime
    end: datetime
    owner_id: int
    owner_type: str
    status: str


class Availability:
    def __init__(self, all_slots: list[TimeSlot]):
        self.all_slots = all_slots

    def process_slots(self, person: "Candidate | Interviewer"):
        clean_slots = []
        
        for slot in self.all_slots:
            print('slot', slot)
         
        
    def get_slots_per_person(self, person: "Candidate | Interviewer"):
        slots_query = self.process_slots(person)


        for slot in self.all_slots:
            
            if slot.owner_id == person.id and slot.status == "available":
                slots_query.append(slot)
                
        return slots_query

    def get_all_available_slots(self):
        return self.all_slots 


@dataclass
class Interview:
    candidate: Candidate
    interviewer: Interviewer
    scheduled_slot: TimeSlot

    def __str__(self):
        return f"The interview betweeen {self.candidate} and interviewer {self.interviewer} will take place on {self.scheduled_slot}."

