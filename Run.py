import string
import time
import module_share
import socket

from Read import getUser, getMessage, pingPong
from Socket import botSocket
from Users import Users, UserPoints

# listening functions should return true if they are to break the loop
listeningFunctions = [] # this reacts to incoming lines
backgroundFunctions = [] # this just does stuff on timers

# init users
Users.customInit()

botObject = botSocket()
module_share.botObject = botObject

listeningFunctions.append(pingPong) # prevent timeouts
listeningFunctions.append(Users.UserListener) # listen for user based updates

backgroundFunctions.append(UserPoints.presencePoints) # this adds points for people in the chat
backgroundFunctions.append(Users.saveUserFile) # this adds points for people in the chat

# request permissions
botObject.requestPermissions()

s = botObject.getSocket() # for the input stream
readbuffer = ""
startTime = time.time()
theString = ""
while True:

	for f in backgroundFunctions:
		f()
			
	s.setblocking(0)
	s.settimeout(0.33)
	try:
		print("recv", end="")
		readbuffer = readbuffer + s.recv(1024).decode("utf-8")			
	except socket.timeout:
		print(".")

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

	

# example of rubmybum message:
#  @badges=broadcaster/1;color=;display-name=RubMyBum;emotes=;id=b281e6b1-902f-47ba-8cf4-809e9e045b2f;mod=0;room-id=142411464;sent-ts=1503340083874;subscriber=0;tmi-sent-ts=1503340085138;turbo=0;user-id=142411464;user-type= :rubmybum!rubmybum@rubmybum.tmi.twitch.tv PRIVMSG #rubmybum :fun gavin test
# user id is : user-id=142411464
# room id is : room-id=142411464