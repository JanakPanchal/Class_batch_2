#if
#if else
# if elif else
#switch statemement

numberList = [ 10 , 20 ,30 ,50 ,20 ,40 ,60 ,35]
i = 35
if i in numberList:
	for a in range(1 , 11):
		print("{} * {} = {}".format(i , a , i * a))
else:
	print("condition is false")
	
name = "Panchal"

if name == "Janak":
	print("Name is {}".format(name))
elif name == "Panchal":
	print("Last Name is {}".format(name))
elif name == "Roy":
	print("Name is {}".format(name))
else:
	print("Name is not valid")
	
	
def a(b):
	return {
		"a" : "1",
		"b" : "2",
		"c" : "3"
	}.get(b , "def")

print(a("v"))