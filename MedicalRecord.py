class MedicalRecord:

    def getPatientName(self) -> str:

        return self.__patientName

    def setPatientName(self, patientName) -> None:
        self.__patientName = patientName

    def getPatientID(self) -> str:

        return self.patientID

    def setPatientID(self, patId) -> None:
        self.patientID = patId

    def getVisitDate(self) -> str:

        return self.visitDate

    def setVisitDate(self, _VisD) -> None:
        self.visitDate = _VisD

    def getDoctorName(self) -> str:

        return self.doctorName

    def setDoctorName(self, docName) -> None:
        self.doctorName = docName

    def getProcedureCode(self) -> str:

        return self.procedureCode

    def setProcedureCode(self, code) -> None:
        self.procedureCode = code
