class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        start2=min(start,destination)
        destination2=max(start,destination)
        tot=sum(distance)
        print(tot)
        road1=sum(distance[start2:destination2])
      
        print(road1)
        road2=tot-road1
        return min(road1, road2)

      

