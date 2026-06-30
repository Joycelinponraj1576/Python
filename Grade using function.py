def compute_grade(score):
    if score >= 90:
        return 'A Grade'
    elif score >= 80:
        return 'B Grade'
    elif score >= 70:
        return 'C Grade'
    elif score >= 60:
        return 'D Grade'
    else:
        return 'Fail'
    
print("Enter the score (0-100): ")
score = float(input())  
grade = compute_grade(score)
print("Grade:", grade)
