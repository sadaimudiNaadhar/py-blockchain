import time
from src.StringUtil import StringUtil

class Block:

    def __init__(self, data, previousHash):
        self.data = data
        self.previousHash = previousHash
        self.timeStamp = int(time.time())
        self.nounce = 0
        self.hash = self.calculateHash()

    def calculateHash(self):

        return StringUtil.applySha256(
            str(self.previousHash).encode() +
            bytes(self.timeStamp) + bytes(self.nounce) + self.data
        )

    def mineBlock(self):

        while self.hash[0] > "8":
            self.nounce += 1
            self.hash = self.calculateHash()

        print("Block Mined!!! : " + self.hash + "\n")

    def getData(self) -> str:
        return self.data
