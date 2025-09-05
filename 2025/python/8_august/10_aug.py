class ones_threes_nines():
    def __init__(self):
        self.ones = 0
        self.threes = 0
        self.nines = 0

    def get_counts(self, target):
        self.target = target
        while(self.target > 0):
            if(self.target >= 9):
                self.nines += 1
                self.target -= 9
            elif(self.target >= 3):
                self.threes += 1
                self.target -= 3
            elif(self.target >= 1):
                self.ones += 1
                self.target -= 1
        return f"nines:{self.nines}, threes:{self.threes}, ones:{self.ones}"

# OnesThreesNines = ones_threes_nines()
# print(OnesThreesNines.get_counts(10))
# print(OnesThreesNines.get_counts(15))
# print(OnesThreesNines.get_counts(22))

class Employee():

    @classmethod
    def from_string(cls, name_string):
        firstname, lastname, salary = name_string.split("-")
        emp = cls()
        emp.firstname = firstname
        emp.lastname = lastname
        emp.salary = int(salary)
        return emp

    

# emp1 = Employee.from_string("John-Smith-55000")
# print(emp1.firstname)
# print(emp1.lastname)
# print(emp1.salary)