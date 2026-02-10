from dataclasses import dataclass
from datetime import datetime, timedelta, time
from typing import Optional, TYPE_CHECKING
from app.models.person import Interviewer, Candidate, Person

@dataclass
class TimeSlot:
    id: int
    start: datetime
    end: datetime
    owner_id: int
    owner_type: str
    status: str


@dataclass
class WorkHours:
    id: int
    start: time
    end: time
    workdays: set[int]


@dataclass
class Interview:
    id: int
    candidate: Candidate
    interviewer: Interviewer
    scheduled_slot: TimeSlot

    def __str__(self):
        return f"The interview betweeen {self.candidate} and interviewer {self.interviewer} will take place on {self.scheduled_slot}."

