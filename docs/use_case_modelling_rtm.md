**Use-Case Modeling**

UC \- 01: Create Challenge

UC \- 02: Manage Challenge

UC \- 03: Join Challenge

UC \- 04: View Challenge Progress

UC \- 05: Record Activity

UC \- 06: Review Summary

**Textual specifications** 

| ID / name | UC \- 01: Create Challenge |
| :---- | :---- |
| **Primary actor** | Organizer |
| **Stakeholders** | Organizer – easy challenge setup Participant \- need clear goal targets and acceptable date ranges |
| **Trigger** | Organizer chooses to create a new challenge. |
| **Preconditions** | Organizer should be authorized and authenticated in the system. |
| **Main success scenario** | Organizer selects the option to create a new challenge Organizer inputs challenge details (name, category, activity type, goal unit’s, target, dates) System validates the details (name, category, activity type, goal unit’s, target, dates)  System saves the new Challenge System confirms the added challenge. |
| **Alternative/exception flows** | 3A \- Invalid inputs \- System flags invalid fields |
| **Postconditions** | A new Challenge record exists in the storage open for enrollemnt. No entry is saved on failure |
| **Related requirements** | FB-03, NFB-02, NFB-03 |

| ID / name | UC \- 02: Manage Challenge |
| :---- | :---- |
| **Primary actor** | Organizer |
| **Stakeholders** | Organizer – needs to change some challenges Participant – needs a consistent and fair rules. |
| **Trigger** | Organizer selects an existing challenge to manage |
| **Preconditions** | Organizer should be authorized and authenticated in the system. The Challenge should already exist. |
| **Main success scenario** | Organizer selects the challenge they want to change. Organizers edits parameters (name, category, activity type, goal unit’s, target, dates) System verifies changes do not conflicts with existing records System confirms the changes  |
| **Alternative/exception flows** | 3A – Conflicting update submitted (e.g. new end dates will end the challenge for some participant) \- Reject Submission and displays the reason for the rejection. |
| **Postconditions** | Challenge updates are saved No entry is saved on failure |
| **Related requirements** | FB-03, NFB-02, NFB-03 |

| ID / name | UC \- 03 Join Challenge |
| :---- | :---- |
| **Primary actor** | Participant |
| **Stakeholders** | Participant – wants to enroll to a specific challenge Organizer – Tracks challenges and enrollment. |
| **Trigger** | Participant selects an active challenge and chooses to enroll |
| **Preconditions** | Participant and the target challenge already exists.  |
| **Main success scenario** | Participants select an active challenge Participants choose to enroll. System checks if the challenge is still active. System checks if the user is already enrolled. System creates a new enrollment record. System confirms the enrollment |
| **Alternative/exception flows** | 3A – Challenge is already inactive \- Reject Submission and displays when the challenge ended 4A – Participant is already enrolled – Reject submission, and display enrollment date. |
| **Postconditions** | An Enrollment record is created No enrollment is saved on failure |
| **Related requirements** | FB-04, NFB-02 |

| ID / name | UC \- 04 View Challenge Progress |
| :---- | :---- |
| **Primary actor** | Participant |
| **Stakeholders** | Participant – needs a real-time progress report Organizer – needs reliable progress data |
| **Trigger** | Participant selects the enrolled challenge to check progress |
| **Preconditions** | Participant and the target challenge already exist, and the participant is enrolled in the challenge |
| **Main success scenario** | Participants selects the challenge to view progress  System retrieves the accepted ActivityRecords associated with the enrollment System calculates the progress  System displays the progress metrics and the completion percentage |
| **Alternative/exception flows** | 2A – No activity recorded yet \- System displays 0% completion and shows an option to record the first progress.  |
| **Postconditions** | Current progress is displayed |
| **Related requirements** | FB-02, NFB-01 |

| ID / name | UC \- 05 Record Activity |
| :---- | :---- |
| **Primary actor** | Participant |
| **Stakeholders** | Participant – needs a reliable, fast way to log progress/activity. Administrator – needs a way to review or flag anomalies in the record Organizer – needs reliable and valid data |
| **Trigger** | Participant chooses to log an activity for a challenge. |
| **Preconditions** | Participant and the target challenge already exist, the participant is enrolled in the challenge, and the activity date is within the challenge period. |
| **Main success scenario** | Participant enters activity details (date, activity type, amount, optional notes) and submits. System validates active enrollment System checks that the activity type matches the challenge System validates that the submitted amount is not negative System stores the valid ActivityRecord. System updates participant's progress toward the Target |
| **Alternative/exception flows** | 2A – No valid enrollment found – Reject submission, advise the participant to enroll first. 4A – Negative amount – Reject submission and identify the valid range  |
| **Postconditions** | One ActivityRecord is stored No record is stored when failure |
| **Related requirements** | FB-01, FB-04, FB-06, NFB-01, NFB-02, NFB-03 |

| ID / name | UC-06 Review Summary |
| :---- | :---- |
| **Primary actor** | Administrator |
| **Stakeholders** | Administrator – needs a way to review or flag anomalies in the record Organizer – needs reliable and valid data |
| **Trigger** | Administrator accesses the records |
| **Preconditions** | Administrator is authenticated and authorized |
| **Main success scenario** | Administrator requests the Review Summary list. System compiles and displays all activity records |
| **Alternative/exception flows** | 1A – No records – Reject request, report that no record is saved |
| **Postconditions** | System compiles and displays all records No record will show on failure |
| **Related requirements** | FB-05, NFB-02, NFB-03 |

**Requirements Traceability**

| Requirement ID | Statement | Type | Use Case and Reference |
| :---- | :---- | :---- | :---- |
| FB-01 | Participants can record activities for enrolled challenges. | Functional | UC-05 Record Activity: Main Success Scenario (Steps 1–6) |
| FB-02 | Participants can view their challenge progress. | Functional | UC-04 View Challenge Progress: Steps 2–4 UC-05 Record Activity: Step 5 |
| FB-03 | Organizers can create and manage challenges. | Functional | UC-01 Create Challenge: All steps UC-02 Manage Challenge: All steps |
| FB-04 | The system validates participant enrollment before recording activities.  | Functional | UC-03 Join Challenge: Step 4 UC-05 Record Activity: Step 2 and Alternative Flow 2A |
| FB-05 | Administrators can review flagged activity records. | Functional | UC-06 Review Summary: All steps  |
| FB-06 | System stores valid activity records reliably. | Functional | UC-05 Record Activity: Main Success Scenario: Step 4 |
| NFB-01 | System shall complete valid activity recording within 2 seconds. | Non-Functional | UC-04 View Challenge Progress: Step 4 UC-05 Record Activity: Step 6 |
| NFB-02 | Display clear validation messages for invalid input. | Non-Functional | UC-01 Create Challenge: Alternative Flow 3A UC-02 Manage Challenge: Alternative Flow 3A UC-03 Join Challenge: Alternative Flows 3A, 4A UC-05 Record Activity: Alternative Flow 2A, 4A UC-06 Review Summary: Alternative Flow 1A |
| NFB-03 | Preserve all accepted activity records without data loss. | Non-Functional | UC-01 Create Challenge: Postconditions UC-02 Manage Challenge: Postconditions UC-05 Record Activity: Postconditions UC-06 Review Summary: Postconditions |

