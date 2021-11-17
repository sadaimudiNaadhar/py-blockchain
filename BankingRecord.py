class BankingRecord:

    def getAccountNumber(self) -> str:

        return self.__accountNumber

    def setAccountNumber(self, accountNumber) -> None:
        self.__accountNumber = accountNumber

    def getAccountType(self) -> str:

        return self.__accountType

    def setAccountType(self, accountType) -> None:
        self.__accountType = accountType

    def getTransactionType(self) -> str:

        return self.__transactionType

    def setTransactionType(self, transactionType) -> None:
        self.__transactionType = transactionType

    def getTransactionAmount(self) -> str:

        return self.__transactionAmount

    def setTransactionAmount(self, transactionAmount) -> None:
        self.__transactionAmount = transactionAmount

    def getBalance(self) -> str:

        return self.__balance

    def setBalance(self, balance) -> None:
        self.__balance = balance
