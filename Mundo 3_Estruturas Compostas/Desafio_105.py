student_grade = {}
def grade(*grades):
    '''
    -> Def grade receive grades typed.
    * Parameter TOTAL = Show the amount of numbers, like TOTAL .
    * grades = Receive N numbers.
    * Student_grade = Return grades in dictionary form.
    '''
    student_grade["TOTAL"] = len(grades)
    student_grade["HIGHEST GRADE"] = max(grades)
    student_grade["LOWEST GRADE"] = min(grades)
    average = sum(grades) / len(grades)
    student_grade["GRADE AVERAGE"] = average
    if average < 7:
        student_grade["SITUATION"] = "BAD"
    elif average >= 7 and average < 8:
        student_grade["SITUATION"] = "REASONABLE"
    else:
        student_grade["SITUATION"] = "EXCELLENT!"


grade(7, 10,6.5,7.5)
print(student_grade)
