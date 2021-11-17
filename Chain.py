from AESCipher import AESCipher
from Block import Block
from StringUtil import StringUtil
import Config


class Chain:

    def __init__(self) -> None:
        self.__blocks = []

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
        return AESCipher(Config.secret).encrypt(StringUtil.getJson(obj))

    def isValid(self) -> bool:

        length = len(self.__blocks)

        if length < 2:
            return False

        for currentBlock in self.__blocks[length - 1:1:-1]:

            prevObject = self.__blocks[self.__blocks.index(currentBlock) - 1]

            if currentBlock.hash != currentBlock.calculateHash():
                return False

            if currentBlock.previousHash != prevObject.calculateHash():
                return False

        return True

    def showBlockChainData(self):
        print("\nThe block chain: ")

        for currentBlock in self.__blocks:
            print(currentBlock.__dict__)

    def showDecryptedBlockChain(self):

        for currentBlock in self.__blocks:

            print("\nDecrypted block data for block #: "
                  + str(self.__blocks.index(currentBlock) + 1)
                  + " " + AESCipher(Config.secret).decrypt(currentBlock.getData()))
