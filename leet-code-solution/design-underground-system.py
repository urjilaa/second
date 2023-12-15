class UndergroundSystem:

    def __init__(self):
        self.checkin_map = {} #id --> (start, time)
        self.total_map = {} #start, endstation ---> (time_total, count)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin_map[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, time = self.checkin_map[id]
        route = start, stationName
        if route not in self.total_map:
            self.total_map[route] = [0, 0]
        self.total_map[route][0] += t -time
        self.total_map[route][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.total_map[(startStation, endStation)]
        return total / count

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)