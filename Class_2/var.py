#str , int , float , list , tuple, set , dict


name = "Janak"
print(type(name).__name__)

number = 10
percentag = 78.5
print(type(number))
print(type(percentag))


name_list = ["Janak","Roy","Fib","Sagar","Shree",20,30.10]
print(name_list)
print(type(name_list))
print(name_list[0])
print(name_list[0:3])
print(name_list[::-1])

person_data = dict(
	name = "Janak",
	age = 20,
	location = "Mumbai"
)
print(person_data)
print(type(person_data))
print(person_data["name"])

data = (
      ["Janak","Roy","Fib","Sagar","Shree",20,30.10],
	   dict(
			name = "Janak",
			age = 20,
			location = "Mumbai"
		),
	   ["Janak", "Roy", "Fib", "Sagar", "Shree", 20, 30.10],
	   10101010110,
	    "Mumbai")
print(data)
print(type(data))
print(data[2][1])
print(data[1]["name"])
print(data[4])


name_list = {"Janak","Roy","Fib","Sagar","Shree","Janak"}
print(list(set(name_list)))







