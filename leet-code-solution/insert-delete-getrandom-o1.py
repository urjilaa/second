class RandomizedSet:

    def __init__(self):
        self.data_map = {} 
        self.data = [] 

    def insert(self, val: int) -> bool:
        if val in self.data_map:
            return False
       
        self.data_map[val] = len(self.data)
        self.data.append(val)
        
        return True

    def remove(self, val: int) -> bool:
        if not val in self.data_map:
            return False

        last_elem = self.data[-1]
        idx_remove = self.data_map[val]

        self.data_map[last_elem] = idx_remove
        self.data[idx_remove] = last_elem

        self.data[-1] = val
        self.data.pop()
        self.data_map.pop(val)
        return True

    def getRandom(self) -> int:        
        return random.choice(self.data)