class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        capacity_count=capacity
        steps = 0
        
        for index, val in enumerate(plants):
            if val <= capacity:
                steps += 1
                capacity -= val
                print()
                
            else:
                steps += index*2 +1
                capacity = capacity_count - val

        return steps