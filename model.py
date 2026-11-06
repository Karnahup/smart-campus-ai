def predict_failure(attendance, marks):

    if attendance < 60 or marks < 40:
        return "High Risk"

    elif marks < 60:
        return "Moderate Risk"

    else:
        return "Low Risk"


def placement_score(marks, attendance):

    score = (marks + attendance) / 2

    if score > 80:
        return "High Placement Chance"

    elif score > 60:
        return "Medium Placement Chance"

    else:
        return "Low Placement Chance"
    
def study_suggestion(marks, attendance):

    if marks < 50 and attendance < 70:
        return "Increase study hours and attend more classes."

    elif marks < 50:
        return "Focus more on studying and revise difficult topics."

    elif attendance < 70:
        return "Improve attendance to understand subjects better."

    else:
        return "Great performance! Keep it up."
