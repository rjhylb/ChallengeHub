1. Analysis of Core Stakeholders

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


  


  


  

2. Domain Vocabulary 

| TERM | DEFINITION |
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

3. Functional Backlog

| FB-01 | Participants can record activities for enrolled challenges. | Participant |
| :---- | :---- | :---- |
| FB-02 | Participants can view their challenge progress. | Participant |
| FB-03 | Organizers can create and manage challenges. | Organizer |
| FB-04 | The system validates participant enrollment before recording activities. | Participant / Organizer |
| FB-05 | Administrators can review flagged activity records. | Administrator |
| FB-06 | The system stores valid activity records. | All Stakeholders |

Non Functional Backlog

| NFB-01 | The system shall complete valid activity recording within 2 seconds. |
| :---- | :---- |
| NFB-02 | The system shall display clear validation messages for invalid input. |
| NFB-03 | The system shall preserve all accepted activity records without data loss. |

Must Have for Clients needs  
\- Record activities successfully.  
Validate participant enrollment.  
Track participant progress accurately.  
Create and manage challenges.  
Store activity records reliably.  
Review flagged records.

Should Have for Clients needs  
\- Activity history tracking.  
Challenge summary reports.  
Completion notifications.  
Exportable reports.  
Audit logs for administrators.  
Enhanced reporting and analytics.

