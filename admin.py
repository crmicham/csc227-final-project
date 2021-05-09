from user import User


class Admin(User):

    def __init__(self, id, pin):
        
        super().__init__(id, pin)

    def show_roster(self, c_list):

        r_course = (str(input("Enter course: "))).upper()

        for course in c_list:

            if course.get_course_code() == r_course:
                course.display_roster()
                print()
                return

        else:
            print("Course not found.")
            print()

    def change_max_size(self, c_list):

        m_course = (str(input("Enter course: "))).upper()

        for course in c_list:

            if course.get_course_code() == m_course:
                course.change_max_size()
                print()
                return

        else:
            print("Course not found.")
            print()
