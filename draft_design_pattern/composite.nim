type
  Employee = ref object of RootObj
    name: string
    salary: float
    roles: seq[Employee]

  Developer = ref object of Employee
  Designer = ref object of Employee

  Organization = ref object
    employees: seq[Employee]


method getName(self: Employee): string {.base, locks: "unknown".} =
  discard

method setSalary(self: Employee, salary: float) {.base, locks: "unknown".} =
  discard

method getSalary(self: Employee): float {.base, locks: "unknown".} =
  discard

method getRoles(self: Employee): seq[Employee] {.base, locks: "unknown".} =
  discard


method getName(self: Developer): string {.locks: "unknown".} =
  self.name

method setSalary(self: Developer, salary: float) {.locks: "unknown".} =
  self.salary = salary

method getSalary(self: Developer): float {.locks: "unknown".} =
  self.salary

method getRoles(self: Developer): seq[Employee] {.locks: "unknown".} =
  self.roles


method getName(self: Designer): string {.locks: "unknown".} =
  self.name

method setSalary(self: Designer, salary: float) {.locks: "unknown".} =
  self.salary = salary

method getSalary(self: Designer): float {.locks: "unknown".} =
  self.salary

method getRoles(self: Designer): seq[Employee] {.locks: "unknown".} =
  self.roles


proc addEmployee(self: Organization, employee: Employee) =
  self.employees.add(employee)

proc getNetSalaries(self: Organization): float =
  result = 0
  for v in self.employees:
    result += v.getSalary()


proc main() =
  let john = Developer(name: "John Doe", salary: 12000)
  let jane = Designer(name: "Jane Doe", salary: 15000)

  let organization = Organization()
  organization.addEmployee(john)
  organization.addEmployee(jane)

  echo "正味の給与: " & $organization.getNetSalaries()


main()
