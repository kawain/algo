type
  RadioStation = ref object
    frequency: float

  StationList = ref object
    stations: seq[RadioStation]


proc getFrequency(self: RadioStation): float =
  self.frequency


proc addStation(self: StationList, station: RadioStation) =
  self.stations.add(station)

proc removeStation(self: StationList, toRemove: RadioStation) =
  self.stations.delete(self.stations.find(toRemove))

iterator iter(self: StationList): RadioStation =
  for v in self.stations:
    yield v


proc main() =
  let r1 = RadioStation(frequency: 1440.89)
  let r2 = RadioStation(frequency: 1030.2)
  let r3 = RadioStation(frequency: 3000.14)

  var stationList = StationList()
  stationList.addStation(r1)
  stationList.addStation(r2)
  stationList.addStation(r3)

  for v in stationList.iter():
    echo v.getFrequency()

  echo "----"

  stationList.removeStation(r2)

  for v in stationList.iter():
    echo v.getFrequency()


main()
