from typing import List, Optional  # Importujeme potřebné typy
from availability import Availability

class Person:
    def __init__(self, person_id: int, name: str, availability: Availability):
        self.id = person_id
        self.name = name
        self.availability = availability


class Candidate(Person):
    def __repr__(self):
        return f"Candidate {self.name} has applied to the process, with this availability: {self.availability}"
    

class Interviewer(Person):
    def check_availability(self):
        return f"Interviewer {self.name} is available: {self.availability}" 
        
        
    


