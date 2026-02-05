from typing import List, Optional  # Importujeme potřebné typy
from dataclasses import dataclass
from datetime import datetime, timedelta
from person import Candidate, Interviewer
from availability import Interview, Availability

class InterviewScheduler:

    def __init__(self, availability: Availability):
        self.availability = availability
    
    def schedule(self, candidate: Candidate, interviewers: list[Interviewer], intervew_duration: int):
        #take candidate and schedule with interviewers 
        #iterate over interviewers
        self.intervew_duration = intervew_duration
        all_matching_slots = []
    
        for interviewer in interviewers:  
            interviewer_slots = self.availability.get_slots_per_person(person=interviewer, slot_duration=intervew_duration)
            candidate_slots = self.availability.get_slots_per_person(person=candidate, slot_duration=intervew_duration)
            
            matching_slots = [i for i in interviewer_slots if i in candidate_slots]
            
            for slot in matching_slots:
                all_matching_slots.append((slot, interviewer.name))
        
        if all_matching_slots:
            earliest_slot = self._find_earliest_slot(all_matching_slots)
            
            interviewer_scheduled = Interview(
                id=1,
                candidate=candidate, 
                interviewer=earliest_slot[1],
                scheduled_slot=earliest_slot[0]
            )
            return interviewer_scheduled
        
       
        return None
    
    def _find_earliest_slot(self, slot_list): 
        earliest_slot = sorted(slot_list, key=lambda x: x[0])
        
        if earliest_slot:
            return earliest_slot[0]

        return None

