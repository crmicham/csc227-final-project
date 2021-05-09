from user import User


class Student(User):

    def __init__(self, id, pin):

        super().__init__(id, pin)

    def add_course(self, c_list):

        a_course = (str(input("Enter course you want to add: "))).upper()  

        for course in c_list:

            if course.get_course_code() == a_course: 
                course.add_student(self.get_id())
                print()
                return

        else:
            print("Course not found.")
            print()

    def drop_course(self, c_list):

        print("*Simulating user input*")
        print("Enter course you want to drop: CTI115")
        d_course = "CTI115"

        for course in c_list:  

            if course.get_course_code() == d_course:
                course.drop_student(self.get_id())
                print()
                return

        else:
            print("Course not found.")
            print()

    def list_courses(self, c_list):

        print("Courses registered:")

        counter = 0
        for course in c_list:

            if course.student_in_course(self.get_id()) is True:  
                print(course.get_course_code())  
                counter += 1

        else:
            print(f"Number of courses registered: {counter}")
            print()







