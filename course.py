
class Course:

    def __init__(self, c_code, m_size):

        self.__course_code = c_code
        self.__max_size = m_size
        self.__roster = []

    def add_student(self, id):

        if len(self.__roster) == self.__max_size:
            print("Course is already full.")

        elif id in self.__roster:
            print("You are already enrolled in this course.")

        else:
            self.__roster.append(id)
            print(f"Student {id} added to {self.__course_code}")

    def drop_student(self, id):

        if id not in self.__roster:
            print("You are not enrolled in this course.")

        else:
            self.__roster.remove(id)
            print(f"Student {id} removed from {self.__course_code}")

    def display_roster(self):

        for students in sorted(self.__roster): 
            print(students)

        print(f"Number of students: {len(self.__roster)}")

    def change_max_size(self):

        print(f"Current enrollment: {len(self.__roster)}")
        print(f"Current max size: {self.__max_size}")

        new_size = int(input("Enter new size: "))

        while new_size < len(self.__roster): 
            print("New max size cannot be smaller than current enrollment.")
            new_size = int(input("Enter new size: "))

        self.__max_size = new_size 

    def get_course_code(self):

        return self.__course_code

    def student_in_course(self, id):

        if id in self.__roster:
            return True

        else:
            return False

