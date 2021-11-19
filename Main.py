from src.BankingRecord import BankingRecord
from src.Chain import Chain
from src.MedicalRecord import MedicalRecord
from src.CreditCard import CreditCard
from src.StudentRecord import StudentRecord

chain = Chain()

print("Trying to Mine block 1...")

bankRecord: BankingRecord = BankingRecord()

bankRecord.setAccountNumber(7009)
bankRecord.setAccountType("Savings")
bankRecord.setTransactionType("Deposit")
bankRecord.setTransactionAmount(200.0)
bankRecord.setBalance(200.0)

chain.addBlock(bankRecord)

print("Trying to Mine block 2... ")

medicalRecord: MedicalRecord = MedicalRecord()
medicalRecord.setDoctorName("Dr. Vaisakh")
medicalRecord.setPatientID("12345")
medicalRecord.setPatientName("Krishna")
medicalRecord.setProcedureCode("582")
medicalRecord.setVisitDate("2/21/2021")

chain.addBlock(medicalRecord)

print("Trying to Mine block 3... ")

creditCardTransaction: CreditCard = CreditCard()
creditCardTransaction.setBusinessName("Business XXX")
creditCardTransaction.setCardholderName("Sadaimudinaadhar")
creditCardTransaction.setDate("2/21/2021")
creditCardTransaction.setStatus("Pending")
creditCardTransaction.setTransactionType("PURCHASE")

chain.addBlock(creditCardTransaction)

print("Trying to Mine block 4... ")

studentRecord: StudentRecord = StudentRecord()
studentRecord.setStudentID(12123123)
studentRecord.setStudentName("Vaisakh V N")
studentRecord.setStudentMajor("Advanced Programming")
chain.addBlock(studentRecord)

print("Blockchain Validity: " + str(chain.isValid()))

chain.showBlockChainData()
chain.showDecryptedBlockData()
