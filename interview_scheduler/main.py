from typing import List, Optional  # Importujeme potřebné typy
from dataclasses import dataclass
from datetime import datetime, timedelta, time
from app.services.availability import Availability, TimeSlot, WorkHours
from app.models.person import Candidate, Interviewer
from interview_scheduler.app.services.scheduler import InterviewScheduler
from interview_scheduler.app.dao.dao import PersonDao, InterviewDao, TimeSlotDao

def main() -> None:
    #inits 
    person_db = PersonDao()
        
    eu_workhours = WorkHours(id=1,start=time(9,00), end=time(17,00), workdays={1,2,3,4,5})
    test_availability = Availability(calendar_period=datetime(2027,1,1,9,00), workhours=eu_workhours)

    vlastimil_interviewer = Interviewer(1, "Vlastimil Tetour")
    person_db.save(vlastimil_interviewer)

    is_available = test_availability.is_available(vlastimil_interviewer,slot=datetime(2026,2,13,15,00),slot_duration=60)
    print("is_available", is_available)


if __name__ == "__main__":
    main()
    