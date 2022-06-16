

#class Bank():
# def 1
# def 2

class Bank():
	abc = 1
	def __init__(self):
		self.abc = 10
		print(self.abc)
		
	def SavingAccount(self,uid):
		if uid == 100:
			return 59999
		else:
			return 00000
	
	def IsAccountHasLoan(self,uid):
		if uid == 100 :
			return True
		else:
			return False
		

a = Bank()
print(a.SavingAccount(100))

class Car():
	def __init__(self):
		print("Init")
	
	@classmethod
	def colour(cls):
		return "red"
	
	@classmethod
	def seats(cls):
		return 4
	
	@staticmethod
	def carname():
		return "RR"
	

c = Car()
print(c.colour())
print(Car.carname())


def checknumber(func):
	def inner1(*args):
		if type(args[0]).__name__ == "int" and type(args[1]).__name__ == "int":
			retvalue = func(*args)
			retvalue += 30
			return retvalue
		else:
			return 'error'
	return inner1




@checknumber
def addnumber(num1 , num2):
	return num1 + num2

print(addnumber(10,20))
	

