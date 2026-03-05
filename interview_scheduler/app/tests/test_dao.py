import pytest 
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

from app.tests.conftest import test_data_dir, interviewer_johnny, sample_johnny_blocked_slots


def test_save_and_get_person(interviewer_johnny):
    person_db = PersonDao()
    person_db.save(interviewer_johnny)

    assert interviewer_johnny == person_db.get_object_by_id(interviewer_johnny.id)
    assert interviewer_johnny.name == "Johny Everpure"
    assert interviewer_johnny.id == 1
    assert interviewer_johnny.email == "johny@everpure.com"

def test_save_and_get_slot(sample_johnny_blocked_slots, interviewer_johnny, sample_alan_blocked_slots, candidate_alan):
    slot_db = TimeSlotDao()
    slot_db.save(sample_johnny_blocked_slots)
    slot_db.save(sample_alan_blocked_slots)

    assert sample_johnny_blocked_slots.id == 1
    assert sample_johnny_blocked_slots.owner_type == "Interviewer"
    assert len(slot_db.get_blocked_slots_by_person(interviewer_johnny.id)) == 1

    assert sample_alan_blocked_slots.id == 2
    assert sample_alan_blocked_slots.owner_type == "Candidate"
    assert len(slot_db.get_blocked_slots_by_person(candidate_alan.id)) == 1

def test_save_and_get_interview():
    pass 


def test_blocked_slot():
    pass 

def test_save_and_get_interview():
    pass 

def test_alan_blocker_slots(sample_alan_blocked_slots, candidate_alan):
    pass
