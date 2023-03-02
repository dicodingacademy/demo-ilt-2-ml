def exam_grade(score):
    if score > 95:
        grade = "Top Score"
    elif score < 30:
        grade = "Fail"
    else:
        grade = "Pass"
    return grade


print(exam_grade(55))  # Should be Fail
print(exam_grade(60))  # Should be Pass
