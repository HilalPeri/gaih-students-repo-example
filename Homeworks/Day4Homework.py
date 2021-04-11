def calculate(midterm, project, final):
    return midterm*(0.3)+project*(0.3)+final*(0.4)


def getStudent(times):
    students = []
    for i in range(0, times):
        name = input("Name and Surname:")
        midterm = int(input("Midterm Grade: "))
        project = int(input("Project Grade: "))
        final = int(input("Final Grade: "))
        obj = {'name': name, 'Midterm Grade': midterm,
               'Project Grade': project, 'Final Grade': final, 'Passing Grade': calculate(midterm, project, final)}
        students.append(obj)
    return students


def sortArray(array, sortKey):
    return sorted(
        array, key=lambda array: array[sortKey], reverse=True)


def writeStudents(students):
    for student in students:
        print(" \n ")
        print("Ad Soyad:" + student['name'])
        print("Midterm Grade:" + str(student['Midterm Grade']))
        print("Project Grade:" + str(student['Project Grade']))
        print("Final Grade:" + str(student['Final Grade']))
        print("Passing Grade:" + str(student['Passing Grade']))


if __name__ == "__main__":
    students = getStudent(5)
    students = sortArray(students, 'Passing Grade')
    writeStudents(students)