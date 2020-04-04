'''
https://leetcode.com/contest/weekly-contest-182/problems/design-underground-system/
'''
class UndergroundSystem:

    def __init__(self):
        self.st = defaultdict(int)
        self.j = defaultdict(int)
        self.u = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.u[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        assert id in self.u and self.u[id] is not None
        self.st[(self.u[id][0], stationName)] += t - self.u[id][1]
        self.j[(self.u[id][0], stationName)] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        assert (startStation, endStation) in self.st
        return self.st[(startStation, endStation)] / self.j[(startStation, endStation)]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
