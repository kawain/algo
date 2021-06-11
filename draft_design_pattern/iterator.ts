class RadioStation {
  constructor(private frequency: number) {}
  getFrequency(): number {
    return this.frequency;
  }
}

class StationList {
  private pointer = 0;
  public stations: RadioStation[] = [];
  addStation(station: RadioStation): void {
    this.stations.push(station);
  }
  removeStation(toRemove: RadioStation): void {
    const tmp = this.stations.filter((v) =>
      v.getFrequency() !== toRemove.getFrequency()
    );
    this.stations = tmp;
    this.pointer = 0;
  }
  next(): { done: boolean; value: RadioStation | null } {
    if (this.pointer < this.stations.length) {
      return {
        done: false,
        value: this.stations[this.pointer++],
      };
    } else {
      return {
        done: true,
        value: null,
      };
    }
  }
}

const stationList = new StationList();
stationList.addStation(new RadioStation(89));
stationList.addStation(new RadioStation(101));
stationList.addStation(new RadioStation(102));
stationList.addStation(new RadioStation(103.2));
stationList.addStation(new RadioStation(3.14));

let result = stationList.next();
while (!result.done) {
  if (result.value) {
    console.log(result.value.getFrequency());
  }
  result = stationList.next();
}

console.log("removeStation(RadioStation(89)");
console.log("removeStation(RadioStation(102)");
console.log("removeStation(RadioStation(103.2)");
stationList.removeStation(new RadioStation(89));
stationList.removeStation(new RadioStation(102));
stationList.removeStation(new RadioStation(103.2));

result = stationList.next();
while (!result.done) {
  if (result.value) {
    console.log(result.value.getFrequency());
  }
  result = stationList.next();
}
