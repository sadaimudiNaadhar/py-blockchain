
import hashlib
import json

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
