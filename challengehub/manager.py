from __future__ import annotations
from datetime import date
from pathlib import Path
from uuid import uuid4
from .models import Challenge, Enrollment, ActivityRecord
from . import storage

class ChallengeManager:
    """Coordinates the current ChallengeHub application behavior."""
    def __init__(self, data_dir="data"):
        self.data_dir=Path(data_dir)
        self.participants=storage.load_participants(self.data_dir/"participants.json")
        self.challenges=storage.load_challenges(self.data_dir/"challenges.json")
        self.enrollments=storage.load_enrollments(self.data_dir/"enrollments.json")
        self.activities=storage.load_activities(self.data_dir/"activities.csv")

    def _participant(self, participant_id):
        return next((x for x in self.participants if x.participant_id==participant_id), None)

    def _challenge(self, challenge_id):
        return next((x for x in self.challenges if x.challenge_id==challenge_id), None)

    def create_challenge(self, name, category, activity_type, goal_unit, goal_target, start_date, end_date):
        # Creates a challenge and persists the updated challenge data.
        if not name.strip(): raise ValueError("Challenge name is required")
        if goal_target <= 0: raise ValueError("Goal must be positive")
        if start_date > end_date: raise ValueError("Start date cannot be after end date")
        challenge=Challenge(f"C{len(self.challenges)+1:03d}", name.strip(), category.strip(), activity_type.strip(), goal_unit.strip(), float(goal_target), start_date, end_date)
        self.challenges.append(challenge)
        storage.save_json(self.data_dir/"challenges.json", self.challenges)
        return challenge

    def join_challenge(self, participant_id, challenge_id, joined_on=None):
        if self._participant(participant_id) is None: raise ValueError("Unknown participant")
        challenge=self._challenge(challenge_id)
        if challenge is None: raise ValueError("Unknown challenge")
        joined_on=joined_on or date.today()
        if joined_on > challenge.end_date: raise ValueError("Challenge has already ended")
        if any(x.participant_id==participant_id and x.challenge_id==challenge_id for x in self.enrollments):
            raise ValueError("Participant already joined")
        enrollment=Enrollment(participant_id, challenge_id, joined_on)
        self.enrollments.append(enrollment)
        storage.save_json(self.data_dir/"enrollments.json", self.enrollments)
        return enrollment

    def record_activity(self, participant_id, challenge_id, activity_type, amount, activity_date, note=""):
        # Validate the activity request before saving it.
        if self._participant(participant_id) is None: raise ValueError("Unknown participant")
        challenge=self._challenge(challenge_id)
        if challenge is None: raise ValueError("Unknown challenge")
        if not any(x.participant_id==participant_id and x.challenge_id==challenge_id for x in self.enrollments):
            raise ValueError("Participant is not enrolled")
        if amount <= 0: raise ValueError("Amount must be positive")
        if challenge.activity_type.lower() != activity_type.lower(): raise ValueError("Activity type does not match challenge")
        if activity_date < challenge.start_date or activity_date > challenge.end_date: raise ValueError("Activity date is outside the challenge period")
        record=ActivityRecord(f"AR-{uuid4().hex[:8].upper()}", participant_id, challenge_id, activity_type, float(amount), activity_date, note.strip())
        self.activities.append(record)
        storage.save_activities(self.data_dir/"activities.csv", self.activities)
        print(f"Activity recorded for {participant_id}: {record.amount:g} {challenge.goal_unit}")
        return record

    def progress(self, participant_id, challenge_id):
        challenge=self._challenge(challenge_id)
        if challenge is None: raise ValueError("Unknown challenge")
        rows=[x for x in self.activities if x.participant_id==participant_id and x.challenge_id==challenge_id]
        # Select the current progress calculation based on the activity type.
        if challenge.activity_type.lower() in ("session", "check-in"):
            total=float(len(rows))
        else:
            total=round(sum(x.amount for x in rows),2)
        percentage=round(min(total/challenge.goal_target*100,100.0),1) if challenge.goal_target else 0.0
        return {"participant_id":participant_id,"challenge_id":challenge_id,"total":total,"goal_target":challenge.goal_target,"goal_unit":challenge.goal_unit,"percentage":percentage,"status":"Completed" if total>=challenge.goal_target else "In progress"}

    def review_summary(self):
        # Pilot rule: unusually large amounts or empty notes are surfaced for human review.
        rows=[]
        for record in self.activities:
            flags=[]
            if record.amount > 50: flags.append("large amount")
            if not record.note.strip(): flags.append("missing note")
            if flags:
                rows.append({"record_id":record.record_id,"participant_id":record.participant_id,"challenge_id":record.challenge_id,"flags":flags})
        return rows
