# Team Collaboration Agreement & Working Charter
## Course: CPE106L-4 Software Design Laboratory
### Project: ChallengeHub Virtual Challenge Management System
#### Team 1
---

## 1. Core Objectives and Principles
This agreement establishes the collaborative framework, engineering standards, and communication protocols for our 4-member team. Our shared commitment is to:
1. Deliver a robust, high-quality ChallengeHub system that tells a single, consistent software-design story across requirements, UML, architecture, code, and verification.
2. Maintain a healthy, supportive, and egoless team dynamic where knowledge is shared and collective ownership is practiced.
3. Adhere to the software engineering code of ethics by upholding professional competence, consistency, and academic integrity.

---

## 2. Roles and Responsibility Allocation
With a team of four, we divide core engineering and managerial roles to ensure clear ownership while promoting collaborative cross-training:
S
### **RACHEL JOY BALDO: Project Manager & Requirements Lead**
*   **Primary Focus:** Project coordination, requirements elicitation, and stakeholder scope.
*   **Key Responsibilities:**
    *   Act as the primary facilitator for team meetings, tracking sprint goals and weekly progress.
    *   Maintain the **Product Backlog** (mapping use cases, functional "shall" rules, and non-functional "should" constraints).
    *   Lead the compilation of the **Requirements Baseline (Checkpoint 1)** deliverables.
    *   Monitor task card updates and coordinate the division of labor.

### **MARK ANGELO AYCARDO Software Architect Developer**
*   **Primary Focus:** Object-oriented modeling, architectural integrity, and database mapping.
*   **Key Responsibilities:**
    *   Lead the creation of UML Class Diagrams, CRC Card sessions, and Sequence Diagrams.
    *   Design the system's structural components (implementing Layered Architecture, Strategy Pattern for progress calculations, and Repository Pattern).
    *   Design the relational database schema in SQLite and define appropriate constraint layers.
    *   Author core domain business logic modules in Python.

### **JIAN BERNARD QUINTON: Git Integration Manager**
*   **Primary Focus:** Version control organization, repository health, and Google Colab sync.
*   **Key Responsibilities:**
    *   Establish and maintain the Git branching and pull request (PR) workflow.
    *   Coordinate merges into the protected `main` branch and resolve any merge conflicts.
    *   Develop and distribute utility scripts ( Google Drive / Colab path connection cells).
    *   Serve as the gatekeeper for the project build environment, ensuring no broken dependencies are introduced.

### **ISSA DUMLAO: QA & Validation Lead**
*   **Primary Focus:** Automated testing, validation strategies, and regression testing.
*   **Key Responsibilities:**
    *   Design the team's automated verification plan in `pytest` (targeting Core, Risk, and Problematic paths).
    *   Lead the implementation of pytest assertions, database mocks, and test fixtures.
    *   Measure and monitor test execution coverage (aiming for high-coverage test paths).
    *   Verify edge cases, boundaries, and validation rules (proving that invalid entries cleanly reject without changing stored states)

---

## 3. Git Branching & Collaboration Workflow
To prevent code conflicts and maintain a high-integrity history, we enforce a strict **Distributed Version Control (Git) workflow**:

1.  **Protected Branch (`main`):**
    *   The `main` branch holds the stable, tested and fully functional codebase. No developer is allowed to commit directly to `main`.
2.  **Feature Branching (`feature/`) & Bug Fixes (`bugfix/`):**
    *   Every feature, requirements model, or test script must be developed on a dedicated branch named semantically:
        *   Format: `feature/FR-[id]-short-description` (ex.`feature/FR-01-add-challenge`)
        *   Format: `bugfix/[issue]-description` (ex.`bugfix/connection-leak`)
3.  **Local Colab Verification:**
    *   Before opening a Pull Request (PR), the developer must execute the automated test suite in quiet mode from their Google Colab terminal:
        ```bash
        python -m pytest -q
        ```
    *   **The "Never Break the Build" Rule:** A branch cannot be merged if any pytest validation fails or leaves errors.
4.  **Pull Request (PR) & Peer Review:**
    *   Once local verification is complete, the developer pushes their branch and creates a PR into `main`.
    *   **Mandatory Approval:** At least one team member (other than the author) must review the PR, verify the test results, inspect code readability, and provide approval before merging is permitted.

---

## 4. Communication & Meeting Cadence
Clear, structured communication pathways are established to prevent information silos:

*   **Weekly Synchronous Meeting:**
    *   **When:** Once a week (aligned with lab/lecture schedules).
    *   **Purpose:** Sprint planning, review of previous milestones, and pair-modeling/debugging sessions.
*   **Daily Async Check-ins (Scrum style via Teams):**
    *   Every team member posts a brief 3-sentence update answering:
        1. *What did I complete yesterday?*
        2. *What will I work on today?*
        3. *Are there any blockers preventing progress?*
*   **Shared Workspace:**
    *   All work is saved inside our shared Google Drive directory (`/My Drive/ChallengeHub`).
    *   We maintain a shared document for drafting checkpoints before compiling final PDFs.

---

## 5. Conflict Resolution Protocol
If technical disagreements or communication issues arise:
1.  **Seek Consensus:** Discuss the trade-offs of each design or requirement option during weekly meetings, referencing evidence from the course textbook or project guide.
2.  **Evaluate Against Client Needs:** Align decisions with the client requirements (e.g., prioritize low-coupling, database persistence, and clean domain vocabulary).
3.  **Majority Vote:** If consensus cannot be reached, the Project Manager will facilitate a vote. In the event of a tie, the specific role owner (e.g., the Architect for design issues, or the QA Lead for testing protocols) has the final decision-making authority.

---

## 6. Academic Integrity and Professional Ethics
*   We will strictly follow Mapúa University's policies regarding academic integrity and professional ethics.
*   We commit to utilizing AI assistants (like Gemini Notebook) as cooperative brainstorming and modeling partners. We will not bypass learning opportunities by copy-pasting code or diagrams without understanding and verifying their logical correctness.
*   All work submitted under our names represents our collective engineering efforts.

---

## 7. Team Signatures & Commitments
By signing this contract, we commit to adhering to this Team Agreement:

*   **RACHEL JOY BALDO (Project Manager / Requirements):** ___________________________ Date: ___________
*   **MARK ANGELO AYCARDO (Software Architect / Developer):** ___________________________ Date: ___________
*   **JIAN BERNARD QUINTON (Git Master / Integration):** ___________________________ Date: ___________
*   **ISSA DUMLAO (QA Lead / Validation):** ___________________________ Date: ___________
