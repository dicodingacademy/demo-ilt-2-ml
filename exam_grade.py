def exam_grade(score):
    if score > 95:
        grade = "A"
    elif score > 80:
        grade = "B"
    elif score > 70:
        grade = "C"
    elif score > 60:
        grade = "D"
    else:
        grade = "E"
    return grade


print(exam_grade(55))  # Should be Fail
print(exam_grade(60))  # Should be Pass
