class Employee:
    def __init__(self, name: str, type: str, base_salary: float):
        self.name = name
        self.type = type
        self.base_salary = base_salary

    def calculate_salary(self) -> float:
        print(f'Base salary of {self.type} {self.name}: {self.base_salary}$')

class Manager(Employee):
    def calculate_salary(self) -> float:
        bonus = self.base_salary * 0.2
        return self.base_salary + bonus

class Developer(Employee):
    def calculate_salary(self) -> float:
        bonus = self.base_salary * 0.1
        return self.base_salary + bonus

class Tester(Employee):
    def calculate_salary(self) -> float:
        bonus = self.base_salary * 0.3
        return self.base_salary + bonus

if __name__ == "__main__":
    employee = Employee('John', 'intern', 0)
    employee.calculate_salary()

    manager = Manager('Dick', 'PM', 6000)
    manager_salary = manager.calculate_salary()
    print(manager_salary)

    dev = Developer('Nick', 'SD', 5000)
    dev_salary = dev.calculate_salary()
    print(dev_salary)

    qa = Tester('Mike', 'QA', 4000)
    qa_salary = qa.calculate_salary()
    print(qa_salary)