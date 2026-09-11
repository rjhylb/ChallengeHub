from dataclasses import dataclass
from datetime import date

@dataclass
class Participant:
    participant_id: str
    name: str
    email: str

@dataclass
class Challenge:
    challenge_id: str
    name: str
    category: str
    activity_type: str
    goal_unit: str
    goal_target: float
    start_date: date
    end_date: date

@dataclass
class Enrollment:
    participant_id: str
    challenge_id: str
    joined_on: date

@dataclass
class ActivityRecord:
    record_id: str
    participant_id: str
    challenge_id: str
    activity_type: str
    amount: float
    activity_date: date
    note: str = ""
