from course import Course
from student import Student
from admin import Admin


# -------------------------------------------------------------------
# Author: Connor Micham
# Date: May 3, 2021
#
# This program simulates a class registration system.
# The user can log in as a student or an administrator;
# Students can add, drop and view courses;
# Administrators can view course rosters and change max class sizes.
# -------------------------------------------------------------------


def main():

    course_list = []
    student_list = []
    admin_list = []

    init_lists(course_list, student_list, admin_list)

    session_type = None
    while session_type != 0:

        session_type = int(input("Enter 1 if you are a student, 2 if you are an administrator, 0 to quit: "))

        if session_type == 1:
            student_session(course_list, student_list)

        if session_type == 2:
            admin_session(course_list, admin_list)


def init_lists(c_list, s_list, a_list):

    course1 = Course("CSC227", 2)
    course1.add_student("1003")
    course1.add_student("1004")
    c_list.append(course1)
    course2 = Course("CTI115", 2)
    course2.add_student("1001")
    c_list.append(course2)
    course3 = Course("DBA130", 1)
    course3.add_student("1002")
    c_list.append(course3)

    student1 = Student("1001", "111")
    s_list.append(student1)
    student2 = Student("1002", "222")
    s_list.append(student2)
    student3 = Student("1003", "333")
    s_list.append(student3)
    student4 = Student("1004", "444")
    s_list.append(student4)

    admin1 = Admin("8001", "888")
    a_list.append(admin1)
    admin2 = Admin("9001", "999")
    a_list.append(admin2)


def login(u_list):

    id = str(input("Enter ID: "))
    pin = str(input("Enter PIN: "))

    for person in u_list:
        if person.get_id() == id and person.get_pin() == pin:
            print("ID and PIN verified")
            print()
            return u_list.index(person)
    else:
        print("ID or PIN incorrect")
        print()
        return -1


def student_session(c_list, s_list):

    index = login(s_list) 
    if index >= 0:

        student = s_list[index] 

        task = None
        while task != 0:

            task = int(input("Enter 1 to add course, 2 to drop course, 3 to see courses you have registered, 0 to exit: "))

            if task == 1:
                student.add_course(c_list)

            if task == 2:
                student.drop_course(c_list)

            if task == 3:
                student.list_courses(c_list)

        else:
            print("Student session ended.")
            print()


def admin_session(c_list, a_list):

    index = login(a_list)
    if index >= 0:

        admin = a_list[index]

        task = None
        while task != 0:

            task = int(input("Enter 1 to show class roster, 2 to change max class size, 0 to exit: "))

            if task == 1:
                admin.show_roster(c_list)

            if task == 2:
                admin.change_max_size(c_list)

        else:
            print("Administrator session ended.")
            print()


main()
