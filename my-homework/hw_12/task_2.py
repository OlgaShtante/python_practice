from typing import List

class Employee:
    def __init__(self, name: str, position: str, salary: float):
        self.name = name
        self.position = position
        self.salary = salary

    def get_info(self) -> str:
        return f"Employee info: {self.name}, {self.position}, {self.salary}"

class Manager(Employee):
    def __init__(self, name: str, position: str, salary: float):
        super().__init__(name, position, salary)
        self.subordinates: List[Employee] = []

    def get_info(self) -> str:
        info = super().get_info()
        return f"{info}, Subordinates: {len(self.subordinates)}"

    def add_subordinate(self, employee: Employee) -> None:
        self.subordinates.append(employee)

    def remove_subordinate(self, employee: Employee) -> None:
        if employee in self.subordinates:
            self.subordinates.remove(employee)


if __name__ == "__main__":
    print(f"*** EMPLOYEE INFO ***")
    employee1 = Employee("Test 1", "Developer", 60000)
    print(employee1.get_info())
    employee2 = Employee("Test 2", "Tester", 50000)
    print(employee2.get_info())

    manager = Manager("Test 3", "Manager", 80000)
    print(f"*** MANAGER INFO ***")
    print(manager.get_info())
    manager.add_subordinate(employee1)
    manager.add_subordinate(employee2)
    print(f"*** ADD SUBORDINATES ***")
    print(manager.get_info())

    manager.remove_subordinate(employee2)
    print(f"*** REMOVE SUBORDINATES ***")
    print(manager.get_info())