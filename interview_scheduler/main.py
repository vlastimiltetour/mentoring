from typing import List, Optional  # Importujeme potřebné typy
from dataclasses import dataclass
from datetime import datetime, timedelta, time
from app.services.availability import Availability
from app.models.person import Candidate, Interviewer, Person
from app.models.timeslot import TimeSlot, WorkHours
from app.services.scheduler import InterviewScheduler
from app.dao.dao import PersonDao, InterviewDao, TimeSlotDao

def main() -> None:
    #inits 
    person_db = PersonDao()
    slots_db = TimeSlotDao()

    #calendar & availability    
    eu_workhours = WorkHours(id=1,start=time(9,00), end=time(17,00), workdays={0,1,2,3,4})
    test_annual_availability = Availability(calendar_period=datetime(2027,1,1,9,00), workhours=eu_workhours)


    #initiate an interviewer 
    vlastimil_interviewer = Interviewer(1, "Vlastimil Tetour")
    person_db.save(vlastimil_interviewer)
    vlastimil_unavailable_slots = slots_db.save(id=1, start=datetime(2026,2,13,11,00), end=datetime(2026, 2, 13, 15,00), owner_id=1, owner_type="Interviewer",status="unavailable")

    is_available_1 = test_annual_availability.is_available(vlastimil_interviewer,slot=datetime(2026,2,15,15,00),slot_duration=60)
    is_available_2 = test_annual_availability.is_available(vlastimil_interviewer,slot=datetime(2026,2,15,14,00),slot_duration=60)
    print("is_available", is_available_1,is_available_2)


if __name__ == "__main__":
    main()
    