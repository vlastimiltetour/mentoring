from typing import List, Optional  # Importujeme potřebné typy
from dataclasses import dataclass
from datetime import datetime, timedelta
from availability import Availability, TimeSlot
from person import Candidate, Interviewer
from scheduler import InterviewScheduler


def main() -> None:

    #inits 
    v1 = TimeSlot(datetime(2026, 6, 1, 9, 00),
            datetime(2026, 6, 1, 17, 00),1, "Interviwer", "available")
    v2 = TimeSlot(datetime(2026, 6, 2, 9, 00),
            datetime(2026, 6, 2, 17, 00),1, "Interviwer", "available")
    v3 = TimeSlot(datetime(2026, 6, 3, 9, 00),
            datetime(2026, 6, 3, 17, 00),1, "Interviwer", "available")
    v4 = TimeSlot(datetime(2026, 6, 4, 9, 00),
            datetime(2026, 6, 4, 17, 00),1, "Interviwer", "available")
    v5 = TimeSlot(datetime(2026, 6, 5, 9, 00),
            datetime(2026, 6, 5, 17, 00),1, "Interviwer", "available")
    
    k1 = TimeSlot(datetime(2026, 2, 1, 9, 00),
            datetime(2026, 6, 1, 17, 00),2, "Interviwer", "available")
    k2 = TimeSlot(datetime(2026, 2, 2, 9, 00),
            datetime(2026, 2, 2, 17, 00),2, "Interviwer", "available")
    k3 = TimeSlot(datetime(2026, 2, 3, 9, 00),
            datetime(2026, 2, 3, 17, 00),2, "Interviwer", "available")
    k4 = TimeSlot(datetime(2026, 2, 4, 9, 00),
            datetime(2026, 2, 4, 17, 00),2, "Interviwer", "available")
    k5 = TimeSlot(datetime(2026, 2, 5, 9, 00),
            datetime(2026, 2, 5, 17, 00),2, "Interviwer", "available")
    
    j1 = TimeSlot(datetime(2026, 6, 5, 12, 00),
            datetime(2026, 6, 5, 14, 00),11, "Interviwer", "available")
   
    master_list = [v1,v2,v3,v4,v5,k1,k2,k3,k4,k5,j1]
    
    master_availalibility = Availability(master_list)
    
    candidate_jaroslav = Candidate(11, "Jaroslav Cerman")
    vlastimil_interviewer = Interviewer(1, "Vlastimil Tetour")
    karel_interviewer = Interviewer(2, "Karel Brumbal")
    
    #code operations 
    #print(master_availalibility.get_slots_per_person(candidate_jaroslav)) #this works
    #print(master_availalibility.get_all_available_slots())
    scheduler = InterviewScheduler(master_availalibility)
    
    print(scheduler.schedule(candidate_jaroslav, [vlastimil_interviewer, karel_interviewer], 60))


if __name__ == "__main__":
    main()
    