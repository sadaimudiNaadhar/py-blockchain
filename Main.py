from src.BankingRecord import BankingRecord
from src.Chain import Chain
from src.MedicalRecord import MedicalRecord
from src.CreditCard import CreditCard

chain = Chain()

print("Trying to Mine block 1...")

bankRecord: BankingRecord = BankingRecord()

bankRecord.setAccountNumber("1234")
bankRecord.setAccountType("Savings")
bankRecord.setTransactionType("Deposit")
bankRecord.setTransactionAmount("100")
bankRecord.setBalance("200")

chain.addBlock(bankRecord)

print("Trying to Mine block 2... ")

medicalRecord: MedicalRecord = MedicalRecord()
medicalRecord.setDoctorName("Dr. Joseph Oakes")
medicalRecord.setPatientID("54469")
medicalRecord.setPatientName("Joseph Sliwka")
medicalRecord.setProcedureCode("582")
medicalRecord.setVisitDate("2/21/2019")

chain.addBlock(medicalRecord)

print("Trying to Mine block 3... ")

creditCardTransaction: CreditCard = CreditCard()
creditCardTransaction.setBusinessName("Penn State University - Abington")
creditCardTransaction.setCardholderName("Joseph Sliwka")
creditCardTransaction.setDate("2/21/2019")
creditCardTransaction.setStatus("Pending")
creditCardTransaction.setTransactionType("PURCHASE")

chain.addBlock(creditCardTransaction)

print("Blockchain Validity: " + str(chain.isValid()))

chain.showBlockChainData()
chain.showDecryptedBlockData()
