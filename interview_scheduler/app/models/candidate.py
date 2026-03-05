from typing import List, Optional  
from dataclasses import dataclass
from app.models.person import Person

@dataclass
class Candidate(Person):
    def __repr__(self):
        return f"candidate {self.name}"
