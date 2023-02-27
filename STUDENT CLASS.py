class Student:
    no_of_leaves = 4

    def __init__(self, name, section, department, faculty, campus):
        self.name = name
        self.section = section
        self.department = department
        self.faculty = faculty
        self.campus = campus

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves


waseem = Student("WASEEM", "E2", "Software Engineering", "Computing", "BJC")
hassan = Student("HASSAN", "M1", "Computer Science", "Computing", "BJC")
abdullah = Student("ABDULLAH", "M2", "Data Science", "Computing", "BJC")

waseem.change_leaves(8)
print(waseem.no_of_leaves)
hassan.change_leaves(10)
print(waseem.name, hassan.department, hassan.no_of_leaves)
print(abdullah.faculty, abdullah.campus)
