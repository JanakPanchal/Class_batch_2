import os
import time
# r , w , a , x
class FileOpr():
	@classmethod
	def readfile(cls,filename):
		with open(filename, 'r') as f:
			listoflines = f.readlines()
			f.close()
		return listoflines
#write
	@classmethod
	def writetext(cls,filename,data):
		try:
			with open(filename, "w") as f:
				f.writelines(data)
				f.close()
		except RuntimeError as error:
			return  error
#append
	@classmethod
	def appendData(cls,filename,data):
		try:
			with open(filename,"a") as f :
				f.write(data)
				f.close()
				
			return True
		except  RuntimeError as error:
			return error
#delete
	@classmethod
	def deleteTextfile(cls,filename):
		time.sleep(10)
		os.remove(filename)
		return "file is removed"
#create
	@classmethod
	def createfile(cls,filename):
		with open(filename , "x") as f :
			f.close()
		return "file is created"

fileop = FileOpr()
print(fileop.createfile("./name.txt"))
fileop.writetext("name.txt", "Welcome to ")
fileop.appendData("name.txt","India")
print(fileop.readfile("name.txt"))
print(fileop.deleteTextfile("name.txt"))