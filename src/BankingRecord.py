class BankingRecord:

    def getAccountNumber(self) -> int:

        return self.__accountNumber
    
    def setAccountNumber(self, accountNumber: int) -> None:
        
        self.__accountNumber = accountNumber

    def getAccountType(self) -> str:

        return self.__accountType

    def setAccountType(self, accountType: str) -> None:
        self.__accountType = accountType

    def getTransactionType(self) -> str:

        return self.__transactionType

    def setTransactionType(self, transactionType: str) -> None:
        self.__transactionType = transactionType

    def getTransactionAmount(self) -> float:

        return self.__transactionAmount

    def setTransactionAmount(self, transactionAmount: float) -> None:
        self.__transactionAmount = transactionAmount

    def getBalance(self) -> float:

        return self.__balance

    def setBalance(self, balance: float) -> None:
        self.__balance = balance
