from dataclasses import dataclass
from datetime import datetime, timedelta, time
from typing import Optional, TYPE_CHECKING
from app.models.person import Interviewer, Candidate, Person

@dataclass
class WorkHours:
    id: int
    start: time
    end: time
    workdays: set[int]