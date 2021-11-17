class CreditCard:

    def getCardholderName(self) -> str:
        return self.cardholderName

    def setCardholderName(self, _CarN) -> None:
        self.cardholderName = _CarN

    def getDate(self) -> str:
        return self.date

    def setDate(self, date) -> None:
        self.date = date

    def getTransactionType(self) -> str:
        return self.__transactionType

    def setTransactionType(self, trasType) -> None:
        self.__transactionType = trasType

    def getBusinessName(self) -> str:
        return self.businessName

    def setBusinessName(self, bName) -> None:
        self.businessName = bName

    def getStatus(self) -> str:
        return self.status

    def setStatus(self, status) -> None:
        self.status = status
