#GPA Calculator for Babcock Grading system
def gpasystem():
    no_of_sub = int(input("Input the number of courses you're taking: "))
    i = 0
    summ = 0
    sum_credit = 0
    while i < no_of_sub:
        i += 1
        grade_point = int(input("Input the credit for course " + str(i) + ": "))
        grade = input("Input grade for course " + str(i) + ": ")
        if grade in ['A', 'a']:
            grade = 5
        elif grade in ['B', 'b']:
            grade = 4
        elif grade in ['C', 'c']:
            grade = 3
        elif grade in ['D', 'd']:
            grade = 2
        elif grade in ['E', 'e']:
            grade = 1
        elif grade in ['F', 'f']:
            grade = 0
        else:
            print("Input a valid grade")
            continue
        total = grade * grade_point
        summ += total
        sum_credit += grade_point
    gpa = summ / sum_credit
    return gpa
sem = int(input("Input the number of semesters you've had so far: "))
totalgpa = 0
j=1
while j<= sem:
    j+=1
    gpapersem = gpasystem()
    print (f"Your GPA for semester {j-1}: {gpapersem}")
    totalgpa += gpapersem
cgpa = totalgpa / sem
print(f"Your CGPA: {cgpa: .3f}")