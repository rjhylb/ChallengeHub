from datetime import date
from .manager import ChallengeManager

def main():
    app=ChallengeManager("data")
    print("ChallengeHub")
    print("Participants:", len(app.participants), "Challenges:", len(app.challenges), "Activities:", len(app.activities))
    print("P001 / C001 progress:", app.progress("P001","C001"))
    print("Admin review:", app.review_summary())

if __name__ == "__main__": main()
