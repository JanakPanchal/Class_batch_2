#value
# Arithmetic operators
# Assignment operators

# return TRUE FALSE
# Comparison operators
# Logical operators
# Identity operators
# Membership operators

# Arithmetic operators
# + , - , / , % , *

print(5+2)
print(5 * 10)

for i in range(1 ,11):
	print("{}  *  {} = {}".format(5, i , 5 * i))


for i in range(1 ,11):
	print("{}  /  {} = {}".format(100, i , int(100 / i)))
	
	
# Assignment operators
# = , += , -=  , *= , /= , %= , **= , &=
name = "ABC"
a ,b = 10,20
print(name , a , b)

# conut = 10
# count = conut + 1
# print(count)
# count += 1
# print(count)
#
# conut = 10
# count = conut * 2
# print(count)
# count *= 2
# print(count)

# Comparison operators
# == , < , > , >=, <= , !=
num = 10
num2 = 20
num3 = 10
print(num == num2)
print(num < num2)
print(num > num2)
print(num != num3)
name = "Janak"
name1 = "janak"
print(name  == name1)


# Logical operators
# and , or , not

#condition1 and Condition2
# true and true
#true

#condition1 and Condition2
# true or false
#true

#condition1 and Condition2
# true not false
#true

#condition1 and Condition2
# true  not true
#false
print("------Logical operators -------")
print(num  == num3 and num2 > num and num3 != num2)
#either any of the condition is true it will return true
print(num != num3 or num2 == num3)
print(num  == num3 != num2 > num )


# Identity operators
#is , mot is
print("------Identity operators -------")
fname_1 = ["Janak", "Abhay"]
fname_2 = fname_1
print(fname_2 is fname_1)
fname_3 = fname_2
print(fname_3 is fname_1)
print(fname_3 is not fname_1)


# Membership operators
#in , not in
print("------Membership operators -------")
name1 = [ 10 , 20 ,30 , 40 , 50]
print( 100 in name1)
print(10 in name1)
print(100 not in name1)

# for a in name1:
# 	if 10 == a:
# 		print(True)
# 	else:
# 		print(False)


