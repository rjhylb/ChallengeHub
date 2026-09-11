## 1. System Overview & Context
ChallengeHub is an existing Python prototype used to manage virtual wellness and productivity challenges

## 2. Dataset & Schema Findings
Inspection of the initial sample data log (`data/activities.csv`) confirms that the transactional activity engine relies on a flat-file schema containing seven specific attributes

| Column Name | Data Type | Description & Constraints | Example Value |
| :--- | :--- | :--- | :--- |
| **`record_id`** | String | Unique string identifier for each activity submission. | `AR-0001` |
| **`participant_id`** | String | Foreign key linking the record to an enrolled `Participant`. | `P001` |
| **`challenge_id`** | String | Foreign key linking the record to a target `Challenge`. | `C001` |
| **`activity_type`** | String | Categorical string representing the logged physical or productivity task. | `walk` |
| **`amount`** | Float | Numeric magnitude logged by the participant (e.g., distance or duration). | `3.5` |
| **`activity_date`** | String (YYYY-MM-DD) | Date string indicating when the activity was performed. | `2026-02-01` |
| **`note`** | String | Optional qualitative description or context provided by the user. | `Morning walk` |

## 3. Observable Prototype Behavior (Baseline CLI Findings)
Execution of the prototype CLI module (`python -m challengehub.cli`) provided empirical proof of the core domain engine's data loading, progress calculatio and administrative filtering capabilities

1. **System Resource Counting:**
   * **Observed State:** `Participants: 3, Challenges: 2, Activities: 3` 
   * **Analysis:** The persistence layer successfully loads relational records into memory upon initialization

## 4. Established System Responsibilities
Based on observable behavior and project specifications, ChallengeHub is responsible for:
* **Organizer Management:** Facilitating the creation and maintenance of challenge windows, targets, units and categories
* **Participant Logging & Tracking:** Validating active enrollments, processing activity records, and dynamically computing progress percentages
* **Administrator Oversight:** Monitoring system health and compiling review summaries for flagged or anomalous submissions
* **Data Integrity & State Preservation:** Persisting records across sessions while guaranteeing that rejected/invalid activity submissions leave stored data strictly unchanged

