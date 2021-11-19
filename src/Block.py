import time
from src.StringUtil import StringUtil

class Block:

    def __init__(self, data, previousHash):
        self.data = data
        self.previousHash = previousHash
        self.timeStamp = int(time.time())
        self.nonce = 0
        self.hash = self.calculateHash()

    def calculateHash(self):

        return StringUtil.applySha256(
            str(self.previousHash).encode() +
            str(self.timeStamp).encode() + str(self.nonce).encode() + self.data
        )

    def mineBlock(self):

        while self.hash[0] != "a" or self.nonce < 98765:
            self.nonce += 1
            self.hash = self.calculateHash()

        print("Block Mined!!! : " + self.hash + "\n")

    def getData(self) -> str:
        return self.data
