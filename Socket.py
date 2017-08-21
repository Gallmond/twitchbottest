import socket
from Settings import HOST, PORT, PASS, IDENT, CHANNEL
from Users import Users
# from Helpers import throttler

class botSocket():

	activeSocket = "hiya"

	def __init__(self):
		print("botSocket init start")
		self.activeSocket = socket.socket()
		self.activeSocket.connect((HOST, PORT))
		print("< PASS " + PASS)
		self.activeSocket.send(("PASS " + PASS + "\r\n").encode(encoding='utf-8'))
		print("< NICK " + IDENT)
		self.activeSocket.send(("NICK " + IDENT + "\r\n").encode(encoding='utf-8'))
		print("< JOIN #" + CHANNEL)
		self.activeSocket.send(("JOIN #" + CHANNEL + "\r\n").encode(encoding='utf-8'))

		# while connection
		readbuffer = ""
		Loading = True
		print("listening for connection")
		while Loading:
			readbuffer = readbuffer + self.activeSocket.recv(1024).decode("utf-8")
			temp = readbuffer.split("\r\n")
			readbuffer = temp.pop()
			
			for line in temp:
				print("> "+str(line))

				# build init userlist
				if(line.split(":")[1].split(" ")[1] == "353"):
					Users.buildUserList(line)
				# build init userlist end


				if("End of /NAMES list" in line):
					Loading = False;
					print("< PRIVMSG #" + CHANNEL + " : Bot joined chat")
					
		# while connecting end
		print("connected")

		print("botSocket init end")
		self.activeSocket.send(("PRIVMSG #" + CHANNEL + " : Bot joined chat\r\n").encode(encoding='utf-8'))

	def getSocket(self):
		return self.activeSocket

	def requestPermissions(self):
		permissions = ["commands","membership","tags"]
		for p in permissions:
			self.send(("CAP REQ :twitch.tv/"+p))
		return True

	def sendMessage(self, _msg): # send message to channel
		messageTemp = "PRIVMSG #" + CHANNEL + " :" + _msg
		self.send(messageTemp)
		return True

	def sendWhisper(self, _msg, _username): # send whisper
		messageTemp = "PRIVMSG #" + CHANNEL + " :/w "+_username+" "+_msg
		self.send(messageTemp)
		print("Whispered: " + messageTemp)


		return True

	def send(self, _msg): # print then send directly to socket
		print("< "+str(_msg))

		# add trailing return line if missing
		if(_msg.find("\r\n")!=len(_msg)-len("\r\n")):
			_msg+="\r\n"

		self.activeSocket.send((_msg+"\r\n").encode(encoding='utf-8'))
		return True
