class campus:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def get_info(self):
        return f"campus: {self.name}, Location: {self.location}"

class Department(campus):
    def __init__(self, name, location, department_name):
        super().__init__(name, location)
        self.department_name = department_name
    def get_info(self):
        return f"Department: {self.department_name}, Campus: {self.name}, Location: {self.location}"

class Faculty(Department):
    def __init__(self, name, location, department_name, faculty_name):
        super().__init__(name, location, department_name)
        self.faculty_name = faculty_name

    def get_info(self):
        return f"Faculty: {self.faculty_name}, Depaertment: {self.department_name}, Campus: {self.name}, Location: {self.location}"

campus = campus("Baghdad Ul Jadeed", "Bahawalpur")
department = Department("Baghdad Ul Jadeed", "Bahawalpur", "Software Engineering")
faculty = Faculty("Baghdad Ul Jadeed", "Bahawalpur", "Software Engineering", "Computing")

print(campus.get_info())

print(faculty.get_info())

print(department.get_info())


