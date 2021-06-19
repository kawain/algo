export {};

interface Door {
  getDescription(): void;
}

class WoodenDoor implements Door {
  getDescription(): void {
    console.log("私は木のドアです");
  }
}

class IronDoor implements Door {
  getDescription(): void {
    console.log("私は鉄のドアです");
  }
}

interface DoorFittingExpert {
  getDescription(): void;
}

class Welder implements DoorFittingExpert {
  getDescription(): void {
    console.log("私が取り付けられるのは鉄のドアだけです");
  }
}

class Carpenter implements DoorFittingExpert {
  getDescription(): void {
    console.log("私が取り付けられるのは木のドアだけです");
  }
}

interface DoorFactory {
  makeDoor(): Door;
  makeFittingExpert(): DoorFittingExpert;
}

class WoodenDoorFactory implements DoorFactory {
  makeDoor(): Door {
    return new WoodenDoor();
  }
  makeFittingExpert(): DoorFittingExpert {
    return new Carpenter();
  }
}

class IronDoorFactory implements DoorFactory {
  makeDoor(): Door {
    return new IronDoor();
  }
  makeFittingExpert(): DoorFittingExpert {
    return new Welder();
  }
}

const woodenFactory = new WoodenDoorFactory();
let door = woodenFactory.makeDoor();
let expert = woodenFactory.makeFittingExpert();
door.getDescription();
expert.getDescription();

const ironFactory = new IronDoorFactory();
door = ironFactory.makeDoor();
expert = ironFactory.makeFittingExpert();
door.getDescription();
expert.getDescription();
