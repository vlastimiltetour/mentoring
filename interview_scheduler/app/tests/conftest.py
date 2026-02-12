import pytest
from datetime import time, datetime
from app.models.timeslot import WorkHours
from app.models.person import Interviewer

def sample_workhours():
    '''
    Docstring for sample_workhours
    '''
    return WorkHours(id=1, start=time(9,00), end=time(17,00), workdays={0,1,2,3,4})

def sample_interviewer():
    return Interviewer(id=1, name="Jaroslav Testik")

def sample_person_dao():
    pass 