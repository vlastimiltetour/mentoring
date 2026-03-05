#export PYTHONPATH=$PYTHONPATH:.
#pytest

import pytest 
import os
import shutil
from unittest.mock import MagicMock
from typing import List, Optional  # Importujeme potřebné typy
from dataclasses import dataclass
from datetime import datetime, timedelta, time
from app.services.availability import Availability
from app.models.person import Person
from app.models.interviewer import Interviewer
from app.models.candidate import Candidate
from app.models.timeslot import TimeSlot
from app.models.workhours import WorkHours
from app.models.interview import Interview
from app.services.scheduler import InterviewScheduler
from app.dao.person_dao import PersonDao
from app.dao.interview_dao import InterviewDao
from app.dao.timeslot_dao import TimeSlotDao

@pytest.fixture
def test_data_dir(tmp_path):
    d = tmp_path / "test_data"
    d.mkdir()
    return str(d)

@pytest.fixture
def sample_person_dao(test_data_dir):
    return PersonDao(storage_file=os.path.join(test_data_dir, "test_person.json")) 

@pytest.fixture
def candidate_alan():
    return Candidate(id=2,name= "Alan Harper", email="alan@harper.com")

@pytest.fixture
def interviewer_johnny():
    return Interviewer(id=1, name="Johny Everpure", email="johny@everpure.com")

@pytest.fixture
def eu_workhours(): #last working hour slot is 16,00
    return WorkHours(id=1,start=time(9,00), end=time(16,00), workdays={0,1,2,3,4})

@pytest.fixture
def sample_availability_service(eu_workhours):
    return Availability(now=datetime(2026,2,28,9,00), calendar_period=datetime(2027,1,1,9,00), workhours=eu_workhours)

@pytest.fixture
def sample_johnny_blocked_slots():
    return TimeSlot(id=1, start=datetime(2026,3,2,9,00), end=datetime(2026, 3, 2, 13,00), owner_id=1, owner_type="Interviewer",status="unavailable")

@pytest.fixture
def sample_alan_blocked_slots():
    return TimeSlot(id=2, start=datetime(2026,3,2,11,30), end=datetime(2026, 3, 2, 15,00), owner_id=2, owner_type="Candidate",status="unavailable")

@pytest.fixture
def sample_interview():
    return Interview(id=1, candidate=candidate_alan, interviewer=interviewer_johnny, scheduled_slot=datetime(2026,3,2,15,0))