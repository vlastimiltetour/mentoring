from typing import List, Optional  # Importujeme potřebné typy
from dataclasses import dataclass
from datetime import datetime, timedelta
from person import Candidate, Interviewer
from availability import Interview, Availability

class InterviewScheduler:
    def __init__(self, duration: int):
        self.duration = duration
    
    def schedule(self, candidate: Candidate, interviewers: list[Interviewer]):
        #take candidate and schedule with interviewers 
        #iterate over interviewers

        all_matching_slots = []
    
        for interviewer in interviewers:  
            interviewer_slots = self._get_timeslots(availability=interviewer.availability)
            candidate_slots = self._get_timeslots(availability=candidate.availability)
            matching_slots = [i for i in interviewer_slots if i in candidate_slots]
            
            for slot in matching_slots:
                all_matching_slots.append((slot, interviewer.name))
        
        
        
        if all_matching_slots:
            earliest_slot = self._find_earliest_slot(all_matching_slots)
            
            interviewer_scheduled = Interview(
                candidate_name=candidate.name, 
                interviewer_name=earliest_slot[1],
                scheduled_slot=earliest_slot[0]
            )
            return interviewer_scheduled
        
       
        return None
    
    def _get_timeslots(self, availability: Availability):
        available_slots = []
        duration = timedelta(minutes=self.duration)
        start_time = None

        for slot in availability.slots:
           start_time = slot.start 
           
           while (start_time + duration) <= slot.end:
            available_slots.append(start_time)          
            start_time += duration

        return available_slots
    
    def _find_earliest_slot(self, slot_list): 
        earliest_slot = sorted(slot_list, key=lambda x: x[0])
        
        if earliest_slot:
            return earliest_slot[0]

        return None

