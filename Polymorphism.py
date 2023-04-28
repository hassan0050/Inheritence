class Faculty:
    def __init__(self, name, departments):
        self.name = name
        self.departments = departments

class Departmen:
    def __init__(self, name, campus):
        self.name = name
        self.campus = campus

class campus:
    def __init__(self, name, location):
        self.name = name
        self.location = location

#Example usage
campus1 = campus("Baghdad UL Jadeed", "Bahawalpur",)
campus2 = campus("Khwaja Fareed", "Bahawalpur")

department1 = Departmen("Software Engineering", campus1)
department2 = Departmen("Mathematics", campus1)
department3 = Departmen("MBBS", campus2)

faculty1 = Faculty("Computing", [department1])
faculty2 = Faculty("Management Science", [department2])
faculty3 = Faculty("Medical and Health", [department3])


print(faculty1.departments[0].name)
print(faculty1.name)
print(campus1.name)
print(department1.campus.location)

