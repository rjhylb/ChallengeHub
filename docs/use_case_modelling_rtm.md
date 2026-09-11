**1. Use-Case Modeling**

UC \- 01: Create Challenge

UC \- 02: Manage Challenge

UC \- 03: Join Challenge

UC \- 04: View Challenge Progress

UC \- 05: Record Activity

UC \- 06: Review Summary

**2. Textual Specifications** 

**UC-01: Create Challenge**

| ID / name | UC \- 01: Create Challenge |
| :---- | :---- |
| **Primary actor** | Organizer |
| **Stakeholders** | Organizer – Needs intuitive challenge setup Participant \- Needs clear goal targets, units, and dates |
| **Trigger** | Organizer chooses to create a new challenge. |
| **Preconditions** | Organizer should be authorized and authenticated in the system. |
| **Main success flow** | Organizer selects the option to create a new challenge Organizer inputs challenge details (name, category, activity_type, goal_unit, goal_target, start_date, end_date) System validates that dates and numeric targets are positive and logical System saves the new Challenge entity System confirms the added challenge. |
| **Alternative flows** | 3A \- Invalid inputs \- System flags invalid fields, displays error messages, and cancels saving |
| **Postconditions** | A new Challenge record exists in the storage open for enrollemnt. No entry is saved on failure |
| **Related requirements** | FB-01, NFB-02, NFB-03 |

**UC-02: Manage Challenge**

| ID / name | UC \- 02: Manage Challenge |
| :---- | :---- |
| **Primary actor** | Organizer |
| **Stakeholders** | Organizer – needs to change some challenges Participant – needs a consistent and fair rules. |
| **Trigger** | Organizer selects an existing challenge to manage |
| **Preconditions** | Organizer should be authorized and authenticated in the system. The Challenge should already exist. |
| **Main success flow** | Organizer selects the challenge they want to change. Organizers edits parameters (name, category, activity_type, goal_unit, goal_target, start_date, end_date) System verifies changes do not conflicts with existing records System confirms the changes  |
| **Alternative flows** | 3A – Conflicting update submitted (e.g. new end dates will end the challenge for some participant) \- Reject Submission and displays the reason for the rejection. |
| **Postconditions** | Challenge updates are saved No entry is saved on failure |
| **Related requirements** | FB-01, NFB-02, NFB-03 |


**UC-03: Join Challenge**

| ID / name | UC \- 03 Join Challenge |
| :---- | :---- |
| **Primary actor** | Participant |
| **Stakeholders** | Participant – wants to enroll to a specific challenge Organizer – Tracks challenges and enrollment. |
| **Trigger** | Participant selects an active challenge and chooses to enroll |
| **Preconditions** | Participant and the target challenge already exists.  |
| **Main success flow** | Participants select an active challenge Participants choose to enroll. System checks if the challenge is still active. System checks if the user is already enrolled. System creates a new enrollment record. System confirms the enrollment |
| **Alternative flows** | 3A – Challenge is already inactive \- Reject Submission and displays when the challenge ended 4A – Participant is already enrolled – Reject submission, and display enrollment date. |
| **Postconditions** | An Enrollment record is created No enrollment is saved on failure |
| **Related requirements** | FB-02, FB-03 NFB-02 |

**UC-04: View Challenge Progress**

| ID / name | UC \- 04 View Challenge Progress |
| :---- | :---- |
| **Primary actor** | Participant |
| **Stakeholders** | Participant – needs a real-time progress report Organizer – needs reliable progress data |
| **Trigger** | Participant selects the enrolled challenge to check progress |
| **Preconditions** | Participant and the target challenge already exist, and the participant is enrolled in the challenge |
| **Main success flow** | Participants selects the challenge to view progress  System retrieves the accepted ActivityRecords associated with the enrollment System calculates the progress  System displays the progress metrics and the completion percentage |
| **Alternative flows** | 2A – No activity recorded yet \- System displays 0% completion and shows an option to record the first progress.  |
| **Postconditions** | Current progress is displayed |
| **Related requirements** | FB-05, FB-06, NFB-01 |

**UC-05: Record Activity**

| ID / name | UC \- 05 Record Activity |
| :---- | :---- |
| **Primary actor** | Participant |
| **Stakeholders** | Participant – needs a reliable, fast way to log progress/activity. Administrator – needs a way to review or flag anomalies in the record Organizer – needs reliable and valid data |
| **Trigger** | Participant chooses to log an activity for a challenge. |
| **Preconditions** | Participant and the target challenge already exist, the participant is enrolled in the challenge, and the activity date is within the challenge period. |
| **Main success flow** | Participant enters activity details (activity_date, activity_type, amount, optional note) and submits. System validates active enrollment System checks that the activity type matches the challenge System validates that the submitted amount is not negative System stores the valid ActivityRecord. System updates participant's progress toward the Target |
| **Alternative flows** | 2A – Unlinked Enrollment – Reject submission, advise the participant to enroll first. 4A – Invalid amount / Out-of-bounds date – Reject submission and identify the valid range  |
| **Postconditions** | One ActivityRecord is stored No record is stored when failure |
| **Related requirements** | FB-02, FB-03, FB-04, FB-06, NFB-01, NFB-02, NFB-03 |

**UC-06: Review Summary**

| ID / name | UC-06 Review Summary |
| :---- | :---- |
| **Primary actor** | Administrator |
| **Stakeholders** | Administrator – needs a way to review or flag anomalies in the record Organizer – needs reliable and valid data |
| **Trigger** | Administrator accesses the records |
| **Preconditions** | Administrator is authenticated and authorized |
| **Main success flow** | Administrator requests the Review Summary list. System compiles and displays all activity records |
| **Alternative flows** | 1A – No records found – Reject request, report that no record is saved |
| **Postconditions** | System compiles and displays all records No record will show on failure |
| **Related requirements** | FB-06, NFB-02, NFB-03 |


## Requirements Traceability


| Requirement ID | Statement | Type | Use Case and Reference | pytest Verification |
| :---- | :---- | :---- | :---- | :---- |
| FB-01 | Organizers shall create and manage challenges with specific dates, units, and targets | Functional | UC-01 (Steps 1–5)<br>UC-02 (Steps 1–4) | tests/test_challenges.py::test_create_challenge_success |
| FB-02 | Participants shall enroll in active challenges and record activity entries | Functional | UC-03 (Steps 1–6)<br>UC-05 (Steps 1–5)| tests/test_activities.py::test_record_activity_success |
| FB-03 | System shall validate active enrollment before storing activity entries | Functional | UC-03 (Step 4)<br>UC-05 (Step 2, Alt 2A) | tests/test_activities.py::test_unlinked_participant_rejected |
| FB-04 | Invalid submissions shall raise an exception, leaving stored state and progress strictly unchanged | Functional | UC-05 (Alt 4A, Postconditions) | tests/test_activities.py::test_invalid_amount_preserves_state |
| FB-05 | System shall support amount-based and count-based progress calculation model | Functional | UC-04 (Steps 2–4) | tests/test_progress.py::test_calculation_strategies
| FB-06 | System shall generate dynamic progress summaries and administrative review dashboards | Functional | UC-04 (Step 4)<br>UC-06 (Steps 1–2) | tests/test_cli.py::test_admin_review_summary|
| FB-07 | System shall persistently store all participants, challenges, enrollments, and activity logs | Functional | UC-01, UC-03, UC-05 (Postconditions) | tests/test_persistence.py::test_sqlite_persistence |
| NFB-01 | Valid activity submissions shall be processed within 2 seconds | Non-Functional | UC-04 (Step 4)<br>UC-05 (Step 6) | tests/test_performance.py::test_recording_latency |
| NFB-02 | System shall display clear validation messages for invalid inputs | Non-Functional |UC-01–UC-06 (Alternative Exception Flows) | tests/test_activities.py::test_error_message_clarity |
| NFB-03 | System shall preserve accepted records without data corruption across restarts | Non-Functional | UC-01, UC-02, UC-05, UC-06 (Postconditions) | tests/test_persistence.py::test_data_integrity_across_restarts |
| NFB-04 | System should adopt a layered architecture (CLI, Business Logic, Persistence) | Non-Functional | Architectural Constraint | Inspection of challengehub/ package separation |
| NFB-05 | System should be verifiable using automated pytest test suites) | Non-Functional | All Use Cases | Full suite execution (python -m pytest -q) |

