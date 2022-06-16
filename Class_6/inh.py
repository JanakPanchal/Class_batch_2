# A
#
# B(a)
#
# C (b)

# class BaseClass():
# 	#body of class
#
# class DerivedClass(BaseClass):
# 	#body of DerivedClass

# class BaseClass():
# 	#body of class
# class DerivedClass(BaseClass):
# 	#body of DerivedClass
# class SubDerivedClass(DerivedClass):
#   #body of SubDerivedClass

class Customer():
	CID = [100,101,102,103]
	LOANID = [100,101]
	abc = 1
	def __init__(self,cid):
		self.CID = cid
		
	@classmethod
	def SavingAccount(cls,cid):
		if cid in cls.CID:
			return 20000
		else:
			return None
		
	@classmethod
	def IsLoanPresent(cls,cid):
		return True if cid in cls.LOANID else False
	
	@classmethod
	def InterstValue(cls,AccountType,cid):
		if AccountType == "Saving":
			return 4.10
		else:
			return None
	
	
class LoanDept(Customer):
	def __init__(self):
		Customer.__init__(self,101)
	
	def LoanMothlyIntAmount(self,cid, amount):
		if Customer.IsLoanPresent(cid) == True:
			return 10000 * 100 / 720
		else:
			return amount * 100 / 720

# l = LoanDept()
# print(l.LoanMothlyIntAmount(103,20000))

class CreditScore(LoanDept):
	def IsCustomerEq(self,cid,amount):
		if LoanDept.IsLoanPresent(cid) != True:
			if LoanDept.SavingAccount(cid) > 5000:
				return dict(
					IsEligible = True,
					IntAmount = LoanDept.LoanMothlyIntAmount(self,cid,amount)
				)
			else:
				return dict(
					value = None
				)
			
c = CreditScore()
print(c.IsCustomerEq(101,10000))
			
		
	
	
	