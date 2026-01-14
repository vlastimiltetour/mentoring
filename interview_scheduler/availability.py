from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class TimeSlot:
    start: datetime
    end: datetime


class Availability:
    def __init__(self, slots: list[TimeSlot]):
        self.slots = slots

    def __repr__(self):
        return f"Availability: {self.slots}"


@dataclass
class Interview:
    candidate_name: str
    interviewer_name: str
    scheduled_slot: datetime

    def __str__(self):
        return f"The interview betweeen candidate {self.candidate_name} and interviewer {self.interviewer_name} will take place on {self.scheduled_slot}."

