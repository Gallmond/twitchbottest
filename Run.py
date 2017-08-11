import string
import time
from Read import getUser, getMessage, pingPong
from Socket import botSocket, openSocket, sendMessage, requestTwitchPermissions
from Initialize import joinRoom

# listening functions should return true if they are to break 
# the loop (this will skip following functions)
listeningFunctions = [] 



botObject = botSocket()

s = botObject.getSocket()
# joinRoom(s)


# prevent timeouts
listeningFunctions.append(pingPong)

# request permissions
botObject.requestPermissions()

readbuffer = ""
startTime = time.time();
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
		print ()
		if "You Suck" in message:
			botObject.sendMessage("No, you suck!")
			break