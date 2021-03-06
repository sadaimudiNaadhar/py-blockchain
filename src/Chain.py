from src.AESCipher import AESCipher
from src.Block import Block
from src import Config
from src.StringUtil import StringUtil

class Chain:

    def __init__(self) -> None:
        self.__blocks: Block = []

    def addBlock(self, obj: object):

        __length = len(self.__blocks)

        if __length > 0:
            __hash = self.__blocks[__length - 1].hash
        else:
            __hash = 0  # first block

        block: Block = Block(Chain.getEncryptedData(obj), __hash)
        block.mineBlock()

        return self.__blocks.append(block)

    @staticmethod
    def getEncryptedData(obj: object):
        return AESCipher(Config.getSecret()).encrypt(StringUtil.getJson(obj))

    def isValid(self) -> bool:

        length = len(self.__blocks)

        if length < 2:
            return False

        currentBlock: Block
        
        for currentBlock in self.__blocks[length - 1:1:-1]:

            prevObject = self.__blocks[self.__blocks.index(currentBlock) - 1]

            if currentBlock.hash != currentBlock.calculateHash():
                return False

            if currentBlock.previousHash != prevObject.calculateHash():
                return False
            
            if currentBlock.hash[0] != Config.getDifficultyString():
                return False

        return True

    def showBlockChainData(self):
        print("\nThe block chain: ")

        for currentBlock in self.__blocks:
            print(currentBlock.__dict__)

    def showDecryptedBlockData(self):

        currentBlock: Block
        
        for  currentBlock in self.__blocks:

            print("\nDecrypted block data for block #: "
                  + str(self.__blocks.index(currentBlock) + 1)
                  + " " + AESCipher(Config.getSecret()).decrypt(currentBlock.getData()))
