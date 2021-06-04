# どんな組織も従業員（employee）で構成されているものです。
# 各従業員は同じ機能（給与や責務など）を共有しており、
# 従業員によっては報告の義務があったりなかったり、部下がいたりいなかったりします。
# compositeパターンは、クライアントが個別のオブジェクトを統一的な方法で扱えるようにするためのものです。
from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary

    @abstractmethod
    def getName(self) -> str:
        pass

    @abstractmethod
    def setSalary(self, salary: float) -> None:
        pass

    @abstractmethod
    def getSalary(self) -> float:
        pass

    @abstractmethod
    def getRoles(self) -> list["Employee"]:
        pass


class Developer(Employee):
    def __init__(self, name: str, salary: float) -> None:
        super().__init__(name, salary)
        self.roles: list["Employee"] = []

    def getName(self) -> str:
        return self.name

    def setSalary(self, salary: float) -> None:
        self.salary = salary

    def getSalary(self) -> float:
        return self.salary

    def getRoles(self) -> list["Employee"]:
        return self.roles


class Designer(Employee):
    def __init__(self, name: str, salary: float) -> None:
        super().__init__(name, salary)
        self.roles: list["Employee"] = []

    def getName(self) -> str:
        return self.name

    def setSalary(self, salary: float) -> None:
        self.salary = salary

    def getSalary(self) -> float:
        return self.salary

    def getRoles(self) -> list["Employee"]:
        return self.roles


# 次に、さまざまな種別の従業員で構成された組織Organizationを記述します


class Organization:
    def __init__(self) -> None:
        self.employees: list[Employee] = []

    def addEmployee(self, employee: Employee):
        self.employees.append(employee)

    def getNetSalaries(self) -> float:
        netSalary: float = 0
        for v in self.employees:
            netSalary += v.getSalary()
        return netSalary


# 従業員を準備
john = Developer('John Doe', 12000)
jane = Designer('Jane Doe', 15000)

# 組織に追加
organization = Organization()
organization.addEmployee(john)
organization.addEmployee(jane)

print(f"正味の給与: {organization.getNetSalaries()}")
