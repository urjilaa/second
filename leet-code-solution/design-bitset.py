class Bitset:

    def __init__(self, size: int):
        self.bits = ["0"] * size
        self.flipper = ["1"] * size
        self.bitsDict = {0:size, 1:0}
        self.flipperDict = {0:0, 1:size}

    def fix(self, idx: int) -> None:#
        if self.bits[idx] != "1":
            self.bits[idx] = "1"
            self.flipper[idx] = "0"
            self.bitsDict[0] -= 1
            self.bitsDict[1] += 1
            self.flipperDict[0] += 1
            self.flipperDict[1] -= 1

    def unfix(self, idx: int) -> None:
        if self.bits[idx] != "0":
            self.bits[idx] = "0"
            self.flipper[idx] = "1"
            self.bitsDict[0] += 1
            self.bitsDict[1] -= 1
            self.flipperDict[0] -= 1
            self.flipperDict[1] += 1

    def flip(self) -> None:
        self.bits, self.flipper = self.flipper, self.bits
        self.bitsDict,self.flipperDict = self.flipperDict, self.bitsDict
         
    def all(self) -> bool:
        return self.bitsDict[0] == 0

    def one(self) -> bool:
        return self.bitsDict[1] > 0

    def count(self) -> int:
        return self.bitsDict[1]
        
    def toString(self) -> str:
        return ''.join(self.bits)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()