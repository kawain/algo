// わかり易い例 https://9cubed.info/article/composite
export {};

interface Employee {
  addEmployee(obj: Employee): void;
  work(): void;
}

class Director implements Employee {
  employeeList: Employee[] = [];
  addEmployee(obj: Employee): void {
    this.employeeList.push(obj);
  }
  work(): void {
    console.log("部長　働きます");
    for (const v of this.employeeList) {
      v.work();
    }
  }
}

class Manager implements Employee {
  employeeList: Employee[] = [];
  addEmployee(obj: Employee): void {
    this.employeeList.push(obj);
  }
  work(): void {
    console.log("課長　働きます");
    for (const v of this.employeeList) {
      v.work();
    }
  }
}

class LowlyEmployee implements Employee {
  addEmployee(_obj: Employee): void {
  }
  work(): void {
    console.log("働きます");
  }
}

function main(): void {
  const obj1: Employee = new LowlyEmployee();
  const obj2: Employee = new LowlyEmployee();
  const obj3: Employee = new LowlyEmployee();

  const ka: Employee = new Manager();
  ka.addEmployee(obj1);
  ka.addEmployee(obj2);
  ka.addEmployee(obj3);

  const bu: Employee = new Director();
  bu.addEmployee(ka);

  // 社長の指示
  bu.work();
}

main();
