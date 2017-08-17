import string
import time
import module_share

from Read import getUser, getMessage, pingPong
from Socket import botSocket, openSocket, sendMessage, requestTwitchPermissions
from Users import Users, UserPoints

# listening functions should return true if they are to break the loop
listeningFunctions = [] # this reacts to incoming lines
backgroundFunctions = [] # this just does stuff on timers

botObject = botSocket()
module_share.botObject = botObject



listeningFunctions.append(pingPong) # prevent timeouts
listeningFunctions.append(Users.UserListener) # listen for user based updates

backgroundFunctions.append(UserPoints.presencePoints) # this adds points for people in the chat

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

	for f in backgroundFunctions:
		if f():
			break