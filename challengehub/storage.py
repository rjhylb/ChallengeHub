from __future__ import annotations
from dataclasses import asdict
from datetime import date
from pathlib import Path
import csv, json
from .models import Participant, Challenge, Enrollment, ActivityRecord

def _date(value):
    return value if isinstance(value, date) else date.fromisoformat(value)

def load_participants(path):
    return [Participant(**x) for x in json.loads(Path(path).read_text(encoding="utf-8"))]

def load_challenges(path):
    rows=json.loads(Path(path).read_text(encoding="utf-8"))
    for x in rows:
        x["start_date"]=_date(x["start_date"]); x["end_date"]=_date(x["end_date"])
    return [Challenge(**x) for x in rows]

def load_enrollments(path):
    rows=json.loads(Path(path).read_text(encoding="utf-8"))
    for x in rows: x["joined_on"]=_date(x["joined_on"])
    return [Enrollment(**x) for x in rows]

def load_activities(path):
    result=[]
    with Path(path).open(newline="", encoding="utf-8") as f:
        for x in csv.DictReader(f):
            x["amount"]=float(x["amount"]); x["activity_date"]=_date(x["activity_date"])
            result.append(ActivityRecord(**x))
    return result

def save_json(path, rows):
    def default(v):
        if isinstance(v, date): return v.isoformat()
        raise TypeError(type(v).__name__)
    Path(path).write_text(json.dumps([asdict(x) for x in rows], indent=2, default=default), encoding="utf-8")

def save_activities(path, rows):
    fields=["record_id","participant_id","challenge_id","activity_type","amount","activity_date","note"]
    with Path(path).open("w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=fields); w.writeheader()
        for item in rows:
            row=asdict(item); row["activity_date"]=item.activity_date.isoformat(); w.writerow(row)
