class OrderedStream:

    def __init__(self, n: int):
        self.order = {}
        self.location = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.order[idKey] = value
        ans = []

        while self.location in self.order:
            ans.append(self.order[self.location])
            self.location += 1
        return ans

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)