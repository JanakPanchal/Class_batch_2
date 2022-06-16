# def funname():


def FullName(Fname,Lname=" "):
	return "{} {}".format(Fname,Lname)

print(FullName("Janak"))

def FiveTable(a):
	for i in range(1,11):
		print("{}  *  {} = {}".format(a , i , a * i))

def MissingPra(*argv):
	temp = []
	for a in argv:
		temp.append(a)
	return temp


print(MissingPra("Janak",'Roy',"Raj"))
print(MissingPra("Janak"))
print(MissingPra("Opa","Gim","Shree","Mohan"))
print(MissingPra())


#x = lambda arg : expresions
x = lambda a : a * a * a
print(x(3))

a = lambda b : FiveTable(b)

print(a(10))