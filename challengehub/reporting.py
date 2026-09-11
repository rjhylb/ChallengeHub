def summarize_by_challenge(records):
    summary={}
    for r in records:
        row=summary.setdefault(r.challenge_id, {"challenge_id":r.challenge_id,"activity_count":0,"total_amount":0.0})
        row["activity_count"] += 1
        row["total_amount"] = round(row["total_amount"] + r.amount, 2)
    return list(summary.values())
