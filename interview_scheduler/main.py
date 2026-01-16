from typing import List, Optional  # Importujeme potřebné typy
from dataclasses import dataclass
from datetime import datetime, timedelta
from availability import Availability, TimeSlot
from person import Candidate, Interviewer
from scheduler import InterviewScheduler

def main() -> None:

    karel_availability = Availability([
        TimeSlot(
            datetime(2026, 9, 1, 11, 00),
            datetime(2026, 9, 1, 12, 00),
        ),
        TimeSlot(
            datetime(2026, 6, 1, 10, 30),
            datetime(2026, 6, 1, 12, 30),),
        TimeSlot(
            datetime(2026, 1, 1, 10, 30),
            datetime(2026, 1, 1, 12, 30),),
        
    ])

    vlastimil_availability = Availability([ # vlastimil
        TimeSlot(
            datetime(2026, 6, 1, 9, 00),
            datetime(2026, 6, 1, 17, 00),),
            TimeSlot(
            datetime(2026, 6, 2, 9, 00),
            datetime(2026, 6, 2, 17, 00),),
            TimeSlot(
            datetime(2026, 6, 3, 9, 00),
            datetime(2026, 6, 3, 17, 00),),
            TimeSlot(
            datetime(2026, 6, 4, 9, 00),
            datetime(2026, 6, 4, 17, 00),),
            TimeSlot(
            datetime(2026, 6, 5, 9, 00),
            datetime(2026, 6, 5, 17, 00),)
        
    ])

    interviewer2_availability = Availability([ #jaroslav
        TimeSlot(
            datetime(2026, 1, 23, 9, 30),
            datetime(2026, 1, 23, 11, 30),),
        TimeSlot(
            datetime(2026, 9, 1, 11, 00),
            datetime(2026, 9, 1, 12, 00),
        ),
        TimeSlot(
            datetime(2026, 1, 1, 11, 00),
            datetime(2026, 1, 1, 18, 00),
        )
    ])

    karel_candidate = Candidate(1,"Karel Novak", karel_availability)
    interviewer1 = Interviewer(11,"Vlastimil Tetour", vlastimil_availability)
    interviewer2 = Interviewer(12,"Jaroslav Kamen", interviewer2_availability)
    scheduler = InterviewScheduler(duration=60)
    interview_scheduled = scheduler.schedule(karel_candidate, [interviewer1,interviewer2]) # karel vlastimil: 10.30,  11.00 ; karel jaroslav 11.00
    #print(interview_scheduled)

    print(interviewer1.check_availability())

if __name__ == "__main__":
    main()