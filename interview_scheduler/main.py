from typing import List, Optional  # Importujeme potřebné typy
from dataclasses import dataclass
from datetime import datetime, timedelta
from availability import Availability, TimeSlot
from person import Candidate, Interviewer
from scheduler import InterviewScheduler
from dao import PersonDao, InterviewDao, TimeSlotDao

def main() -> None:

    #inits 
    person_db = PersonDao()
    interview_db = InterviewDao()
    timeslot_db = TimeSlotDao()


    v1 = TimeSlot(1, datetime(2026, 6, 1, 9, 00),
            datetime(2026, 6, 1, 17, 00),1, "Interviewer", "available")
    timeslot_db.save(v1)
    
    v2 = TimeSlot(datetime(2026, 6, 2, 9, 00),
            datetime(2026, 6, 2, 17, 00),1, "Interviewer", "available")
    v3 = TimeSlot(datetime(2026, 6, 3, 9, 00),
            datetime(2026, 6, 3, 17, 00),1, "Interviewer", "available")
    v4 = TimeSlot(datetime(2026, 6, 4, 9, 00),
            datetime(2026, 6, 4, 17, 00),1, "Interviewer", "available")
    v5 = TimeSlot(datetime(2026, 6, 5, 9, 00),
            datetime(2026, 6, 5, 17, 00),1, "Interviewer", "available")
    
    k1 = TimeSlot(datetime(2026, 2, 1, 9, 00),
            datetime(2026, 6, 1, 17, 00),2, "Interviewer", "available")
    k2 = TimeSlot(datetime(2026, 2, 2, 9, 00),
            datetime(2026, 2, 2, 17, 00),2, "Interviewer", "available")
    k3 = TimeSlot(datetime(2026, 2, 3, 9, 00),
            datetime(2026, 2, 3, 17, 00),2, "Interviewer", "available")
    k4 = TimeSlot(datetime(2026, 2, 4, 9, 00),
            datetime(2026, 2, 4, 17, 00),2, "Interviewer", "available")
    k5 = TimeSlot(datetime(2026, 2, 5, 9, 00),
            datetime(2026, 2, 5, 17, 00),2, "Interviewer", "available")
    
    j1 = TimeSlot(datetime(2026, 6, 5, 12, 00),
            datetime(2026, 6, 5, 14, 00),11, "Candidate", "available")
   
    master_list = [v1,v2,v3,v4,v5,k1,k2,k3,k4,k5,j1]
        
    master_availalibility = Availability(master_list)

    
    candidate_jaroslav = Candidate(11, "Jaroslav Cerman")
    person_db.save(candidate_jaroslav)

    vlastimil_interviewer = Interviewer(1, "Vlastimil Tetour")
    person_db.save(vlastimil_interviewer)

    karel_interviewer = Interviewer(2, "Karel Brumbal")
    person_db.save(karel_interviewer)

    honza_interviewer = Interviewer(3, "Honza Koumal")
    person_db.save(honza_interviewer)

    print('get person by id: type', person_db.get_object_by_id(1))
    print(person_db.delete(3))
    print(person_db.delete(15))
    
    karel_interviewer = Interviewer(2, "Karel Kinsky", "kaok@mail.cz")
    person_db.save(karel_interviewer)
    

    vlastimil_availability = Availability(master_list).get_slots_per_person(vlastimil_interviewer, 60)
    print('this is vlastimil availability', vlastimil_availability)

    print(person_db.list_all())
    
    print(person_db.get_object_by_id(20))


    #code operations 
    #print(master_availalibility.get_slots_per_person(candidate_jaroslav)) #this works
    #print(master_availalibility.get_all_available_slots())
    scheduler = InterviewScheduler(master_availalibility)
    
    intervew_scheduled = scheduler.schedule(candidate_jaroslav, [vlastimil_interviewer, karel_interviewer], 60)
    #interview_db.save(intervew_scheduled)


if __name__ == "__main__":
    main()
    