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

    interviewer1_availability = Availability([ # vlastimil
        TimeSlot(
            datetime(2026, 6, 1, 9, 30),
            datetime(2026, 6, 1, 11, 30),),
        TimeSlot(
            datetime(2026, 9, 1, 11, 00),
            datetime(2026, 9, 1, 12, 00),
        )
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

    karel_candidate = Candidate("Karel Novak", karel_availability)
    interviewer1 = Interviewer("Vlastimil Tetour", interviewer1_availability)
    interviewer2 = Interviewer("Jaroslav Kamen", interviewer2_availability)
    scheduler = InterviewScheduler(duration=60)
    interview_scheduled = scheduler.schedule(karel_candidate, [interviewer1,interviewer2]) # karel vlastimil: 10.30,  11.00 ; karel jaroslav 11.00
    print(interview_scheduled)

if __name__ == "__main__":
    main()