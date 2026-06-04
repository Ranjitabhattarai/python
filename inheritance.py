# Parent Class
class Parent:
    def __init__(self, father_name, mother_name):
        self.father_name = father_name
        self.mother_name = mother_name

    def display_parent_details(self):
        print("Father Name:", self.father_name)
        print("Mother Name:", self.mother_name)


# Child Class (inherits Parent)
class Student(Parent):
    def __init__(self, student_name, father_name, mother_name):
        super().__init__(father_name, mother_name)  # Initialize Parent class
        self.student_name = student_name

    def display_student_details(self):
        print("Student Name:", self.student_name)
        self.display_parent_details()


# Creating Object
s1 = Student("Ranjita", "indra bhattarai", "bishnu battarai")

# Display Details
s1.display_student_details()