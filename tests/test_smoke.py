from datetime import date
from pathlib import Path
import shutil
from challengehub import ChallengeManager

def copy_data(tmp_path):
    source=Path(__file__).parents[1]/"data"
    target=tmp_path/"data"; shutil.copytree(source,target); return target

def test_existing_progress_behavior(tmp_path):
    app=ChallengeManager(copy_data(tmp_path))
    result=app.progress("P001","C001")
    assert result["total"] == 7.5
    assert result["status"] == "In progress"

def test_existing_record_activity_happy_path(tmp_path):
    app=ChallengeManager(copy_data(tmp_path))
    before=len(app.activities)
    app.record_activity("P001","C001","walk",2.0,date(2026,8,10),"Evening walk")
    assert len(app.activities)==before+1
    assert app.progress("P001","C001")["total"] == 9.5

def test_existing_count_progress_behavior(tmp_path):
    app=ChallengeManager(copy_data(tmp_path))
    assert app.progress("P003","C002")["total"] == 1.0
