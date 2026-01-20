from typing import List, Optional  # Importujeme potřebné typy
from dataclasses import dataclass

@dataclass
class Person:
   id: int
   name: str = None
   email: str = None

@dataclass
class Candidate(Person):

    def __repr__(self):
        return f"candidate {self.name}"

class Interviewer(Person):
    
    def __repr__(self):
        return f"interviewer {self.name}"

        
        
    


