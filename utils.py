def mean(scores):
    if not scores:
        return 0.0
    return sum(scores) / len(scores)

def letter_grade(scores):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "c"
    elif score >= 60:
        return "D"
    else:
        return "F"
        
    