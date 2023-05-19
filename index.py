# An array to hold the courses
courses_db = []

# An array to hold the marks
marks_db = []

# An array to hold the credit hours
credit_hours_db = []

# An array to hold the Grade point of every mark
grade_p = []

total = []

def course():
    print("Enter Courses")
    courses = True
    while courses == True:
        enter= input(": ")
        courses = False if not enter else True
        if courses:
            courses_db.append(enter)
            


def mark():
    print("")
    print("Enter Marks")
    marks = True
    while marks == True:
        enter = input(": ")
        marks = False if not enter else True
        if marks:
            marks_db.append(int(enter))


def credit_hrs():
    print("")
    print("Enter Corresponding credit_hous")
    credit_hours = True
    while credit_hours == True:
        enter = input(": ")
        credit_hours = False if not enter else True
        if credit_hours:
            # if enter < 2 or enter > 3:
            #     print("Invalid value")
            # else:
            credit_hours_db.append(int(enter))


def output():
    for marks in marks_db:
        if marks >= 80:
            print(f"{marks}   A   4.00")
            grade_p.append(4.00)
        elif marks >=75:
            print(f"{marks}   B+   3.50")
            grade_p.append(3.50)
        elif marks >=70:
            print(f"{marks}   B   3.00")
            grade_p.append(3.00)
        elif marks >=65:
            print(f"{marks}   C+   2.50")
            grade_p.append(2.50)
        elif marks >=60:
            print(f"{marks}   C   2.00")
            grade_p.append(2.00)
        elif marks >=55:
            print(f"{marks}   D+   1.50")
            grade_p.append(1.50)
        elif marks >=50:
            print(f"{marks}   D   1.00")
            grade_p.append(1.00)
        elif marks >=45:
            print(f"{marks}   E   0.50")
            grade_p.append(0.50)
        else:
            print(f"{marks}   F   0")
            grade_p.append(0)


def calculation():
    # Multiplies the appended values in grade_p and credit_hours_db array
    for n in range(0, len(grade_p)):
        total.append(grade_p[n] * credit_hours_db[n])

    # Sums up all the values in total array
    total_1 = 0
    for x in total:
        total_1 += x


    # Sums up all the values in credit_hours_db array
    total_2 = 0
    for y in credit_hours_db:
        total_2 += y    

    #Divides the sum of total  by the sum of credit_hours_db and print out the final GPA
    Total_GPA = total_1/total_2
    GPa = Total_GPA.__round__(2)
    print("")
    print(F"GPA: {GPa}")     



def app():
    course()
    mark()
    credit_hrs()
    output()
    calculation()


app()