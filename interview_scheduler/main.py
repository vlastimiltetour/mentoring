from typing import List, Optional  # Importujeme potřebné typy
from dataclasses import dataclass
from datetime import datetime, timedelta, time
from app.services.availability import Availability
from app.models.person import Candidate, Interviewer, Person
from app.models.timeslot import TimeSlot, WorkHours
from app.services.scheduler import InterviewScheduler
from app.dao.person_dao import PersonDao, InterviewDao, TimeSlotDao

def main() -> None:
    print("Hello world")
    
if __name__ == "__main__":
    main()
    