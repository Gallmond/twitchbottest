import string
import time
import module_share

from Read import getUser, getMessage, pingPong
from Socket import botSocket, openSocket, sendMessage, requestTwitchPermissions
from Users import Users

# listening functions should return true if they are to break 
# the loop (this will skip following functions)
listeningFunctions = [] 

botObject = botSocket()
module_share.botObject = botObject



listeningFunctions.append(pingPong) # prevent timeouts
listeningFunctions.append(Users.UserListener) # listen for user based updates

# request permissions
botObject.requestPermissions()

s = botObject.getSocket() # for the input stream
readbuffer = ""
startTime = time.time()
while True:
	readbuffer = readbuffer + s.recv(1024).decode("utf-8")
	temp = readbuffer.split("\r\n")
	readbuffer = temp.pop()		

	for line in temp:
		message = ""
		print("> " + str(line))

		# do listening to incoming	
		for f in listeningFunctions:			
			if f(line):			
				print("breaking loop")			
				break

		message = getMessage(line)
		if "You Suck" in message:
			botObject.sendMessage("No, you suck!")
			break