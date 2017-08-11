import string
import time
from Read import getUser, getMessage, pingPong
from Socket import botSocket, openSocket, sendMessage, requestTwitchPermissions
from Initialize import joinRoom

# listening functions should return true if they are to break 
# the loop (this will skip following functions)
listeningFunctions = [] 

# prevent timeouts
listeningFunctions.append(pingPong)

activeBotSocket = botSocket()
print(activeBotSocket)

s = activeBotSocket.activeSocket
# joinRoom(s)
readbuffer = ""

startTime = time.time();

while True:
	readbuffer = readbuffer + s.recv(1024).decode("utf-8")
	temp = readbuffer.split("\n")
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
			s.sendMessage("No, you suck!")
			break