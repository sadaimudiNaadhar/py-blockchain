
import hashlib
import json

from AESCipher import AESCipher
from BankingRecord import BankingRecord


class StringUtil:

    @staticmethod
    def applySha256(input: str):
        return hashlib.sha256(input).hexdigest()

    @staticmethod
    def getJson(input: str) -> str:
        return json.dumps(input.__dict__)

    @staticmethod
    def getDificultyString(input: int) -> str:
        return hashlib.sha256(input).hexdigest()
