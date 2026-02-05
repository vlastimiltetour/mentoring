from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Optional, TYPE_CHECKING
from person import Interviewer, Candidate

@dataclass
class TimeSlot:
    id: int
    start: datetime
    end: datetime
    owner_id: int
    owner_type: str
    status: str




class Availability:
    def __init__(self, all_slots: list[TimeSlot]):
        self.all_slots = all_slots
        
    def get_slots_per_person(self, person: "Candidate | Interviewer", slot_duration: int):
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

