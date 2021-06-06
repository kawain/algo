# iterator パターンは、背後にある表現を隠したまま、
# あるオブジェクトの1つ以上の要素にアクセスする手段を提供します
from collections.abc import Iterator

# あるオブジェクト


class RadioStation:
    def __init__(self, frequency: float) -> None:
        self.frequency = frequency

    def getFrequency(self) -> float:
        return self.frequency


# 続いてiteratorを記述します

class StationList:
    def __init__(self) -> None:
        self.stations: list[RadioStation] = []

    def addStation(self, station: RadioStation) -> None:
        self.stations.append(station)

    def removeStation(self, toRemove: RadioStation) -> None:
        toRemoveFrequency = toRemove.getFrequency()
        self.stations = [
            v for v in self.stations if v.frequency != toRemoveFrequency
        ]

    def __iter__(self) -> Iterator[RadioStation]:
        return iter(self.stations)


stationList = StationList()
stationList.addStation(RadioStation(89))
stationList.addStation(RadioStation(101))
stationList.addStation(RadioStation(102))
stationList.addStation(RadioStation(103.2))
stationList.addStation(RadioStation(3.14))

for v in stationList:
    print(v.getFrequency())

print("removeStation(RadioStation(89)")
print("removeStation(RadioStation(102)")
print("removeStation(RadioStation(103.2)")
stationList.removeStation(RadioStation(89))
stationList.removeStation(RadioStation(102))
stationList.removeStation(RadioStation(103.2))

for v in stationList:
    print(v.getFrequency())
