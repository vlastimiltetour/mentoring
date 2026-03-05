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


def test_get_slots_per_person_1_week(sample_availability_service, interviewer_johnny):
    
    retrieved_slots = sample_availability_service.get_slots_per_person(
        interviewer_johnny,slot_duration=60, timeframe=datetime(2026, 3, 8, 11, 00))
    
    assert len(retrieved_slots) == 36

def test_get_slots_per_person_2_weeks(sample_availability_service, interviewer_johnny):
    
    retrived_slots = sample_availability_service.get_slots_per_person(
        interviewer_johnny,slot_duration=60, timeframe=datetime(2026, 3, 15, 11, 00))
    
    assert len(retrived_slots) == 76

def test_get_slots_alan(sample_availability_service, candidate_alan):
    retrived_slots = sample_availability_service.get_slots_per_person(
        candidate_alan,slot_duration=60, timeframe=datetime(2026, 3, 15, 11, 00))
    
    assert len(retrived_slots) == 77

def test_interview_scheduling_service(sample_availability_service,candidate_alan, interviewer_johnny, sample_interview):
    scheduler = InterviewScheduler()
    result = scheduler.schedule(sample_availability_service, candidate=candidate_alan, interviewers=[interviewer_johnny], interview_duration=60, timeframe=datetime(2026, 3, 15, 11, 00))

    assert result.id == sample_interview.id
    assert result.scheduled_slot == sample_interview.scheduled_slot