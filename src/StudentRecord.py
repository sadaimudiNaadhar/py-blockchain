class StudentRecord:

    def getStudentID(self) -> int:

        return self.__studentID

    def setStudentID(self, studentID: int) -> None:
        self.__studentID = studentID

    def getStudentName(self) -> str:

        return self.__studentName

    def setStudentName(self, name) -> None:
        self.__studentName = name

    def getStudentMajor(self) -> str:

        return self.__studentMajor

    def setStudentMajor(self, studentMajor) -> None:
        self.__studentMajor = studentMajor
