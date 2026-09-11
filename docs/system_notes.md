## 1. System Overview & Context
ChallengeHub is an existing Python prototype used to manage virtual wellness and productivity challenges.

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


