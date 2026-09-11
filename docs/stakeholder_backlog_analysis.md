# Stakeholder and Backlog Analysis

**1. Analysis of Core Stakeholders**

   1.    Organizer  \- The organizer creates and manages challenges. They set the active type, goal target, and date range for each challenge.

   

* Needs \- They need accurate progress data to track participant performance. So, they can see when a challenge is completed.   
* Problems \- Wrong or incomplete data makes progress reports unreliable.  
* Success – Challenges are easy to create. Progress data is trustworthy.  
    
  2.  Participant – The Participant joins challenges and records their activities.


*  Needs – They need an easy way to log activities and see their progress update right away. They also need clear feedback when something is wrong so they can fix it.   
* Problems – Unclear error messages make it hard to figure out what went wrong. No immediate confirmation makes them unsure if their activity was saved.   
* Success – Activities are easy to record. Progress is visible. Feedback is helpful too.


  3.  Administrator – The administrator oversees the system and handles exceptions. 


* Needs – They need to review flagged records like large amounts or missing notes. They also need to make sure the system runs smoothly.  
* Problems – Without automated flags or summaries, its hard to spot problematic records.  
* Success – Flagged records are easy to find and review. The system stays reliable.

**2. Domain Vocabulary**

| Term | Definition|
| :---- | :---- |
| Participant | A user who joins challenges and records activities. |
| Challenge | A goal based activity with a specific type, target and date range. |
| Enrollment | This is the relationship between a participant and a challenge when they join. |
| ActivityRecord | A recorded activity submitted by a participant for a challenge. |
| Activity Type | The type of activity allowed for a challenge. |
| Goal Target | The goal target is an amount a participant must reach to complete a challenge. |
| Goal Unit | The goal unit is a unit of measurement for the challenge goal. |
| Progress | It is the current status of a participants completion towards a challenge goal. |
| Validation | It is the process of checking if activity data meets all rules and requirements. |
| Flagged Record | It is a record that triggers a review ruling. |
| Review Summary | It is a report of flagged records for the administrator to review. |

**3. Functional Backlog**

| Requirement ID| Requirement| Stakeholder |
| :---- | :---- | :---- |
| FB-01| Organizers shall be able to create and manage challenges with specific activity types, goal targets, goal units, and date ranges. | Organizer |
| FB-02 | Participants shall be able to enroll in active challenges and log activity records for enrolled challenges. | Participant |
| FB-03 | The system shall validate enrollment and input parameters before storing any activity record. | Participant / System|
| FB-04 | The system shall reject invalid activity submissions (e.g, negative amounts or dates outside the challenge window) with an exception, leaving stored records and calculated progress strictly unchanged. | All Stakeholders |
| FB-05 | The system shall support both amount-based (cumulative total) and count-based (session frequency) progress calculation models. | Administrator |
| FB-06 | The system shall calculate dynamic progress summaries and allow Administrators to review flagged records. | Administrator |
| FB-07 | The system shall persistently store all participants, challenges, enrollments, and activity records. | All Stakeholders|

**4. Non-Functional Backlog**

| Requirement ID | Quality Attribute | Requirement Statement | Target |
| :--- | :--- | :--- | :--- |
| NFB-01 | Performance & Responsiveness| The system shall process and confirm valid activity submissions within 2 seconds during interactive CLI execution| Low-latency user feedback. |
| NFB-02 | Usability & Error Feedback| The system shall display clear, actionable validation error messages upon receiving invalid input (e.g, negative amounts, invalid dates, unlinked IDs)| Avoid cryptic stack traces; guide user correction. |
| NFB-03 | Dependability & Data Integrity | The system shall persistently preserve all accepted participants, challenges, enrollments, and activity records without data loss across application restarts | Relational database durability (SQLite persistence). |
| NFB-04 | Maintainability & Low Coupling| The system should adopt a layered architectural pattern (decoupling CLI / UI, Core Domain Logic, and Storage Persistence) to support future rule modifications without cascading code changes. | Separation of concerns; extensible design patterns. |
| NFB-05 | Automated Verifiability | The system should be fully verifiable using automated `pytest` test suites covering normal happy-paths, boundary values, and state-preserving exception cases | High test coverage; automated regression suite. |

**5. Client Needs & Feature Prioritization**

**Must Have (Core System Scope)**
* Record activities successfully: Enrolled participants can log activities with amounts, dates and notes
* Validate participant enrollment: System checks active enrollment before accepting activity records
* Track participant progress accurately: Calculate dynamic progress metrics toward challenge goal target
* Create and manage challenges: Organizers can set up challenge dates, categories, units, and targets
* Store activity records reliably: Persistent data storage across application restarts
* Review flagged records: Administrators can audit anomalous or incomplete activity records 

 **Should Have (Enhancements & Future Growth)**
* Activity history tracking: Detailed chronological view of a participant's past submissions 
* Challenge summary reports: High-level aggregated statistics for organizers and administrators
* Completion notifications: Automated alerts when a participant reaches 100% of their goal
* Exportable reports: Structured export capabilities (e.g, CSV / JSON summaries)
* Audit logs for administrators: Detailed system audit trails for administrative review
* Enhanced reporting and analytics: Visual progress charts and participation trends


