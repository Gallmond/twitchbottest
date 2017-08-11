import socket
from Settings import HOST, PORT, PASS, IDENT, CHANNEL
# from Helpers import throttler

def botSocket():


	def __init__(self):
		print("botSocket init start")
		self.activeSocket = socket.socket()
		self.activeSocket.connect((HOST, PORT))
		# while connection
		readbuffer = ""
		Loading = True
		while Loading:
			readbuffer = readbuffer + self.activeSocket.recv(1024).decode("utf-8")
			temp = readbuffer.split("\n")
			readbuffer = temp.pop()
			
			for line in temp:
				print("> "+str(line))
				if("End of /NAMES list" in line):
					Loading = True;
					self.send("Successfully joined chat")
		# while connecting end

		self.identifySelf()
		self.requestPermissions()
		print("botSocket init end")

	def identifySelf():
		self.send(("PASS " + PASS + "\r\n").encode(encoding='utf-8'))
		self.send(("NICK " + IDENT + "\r\n").encode(encoding='utf-8'))
		self.send(("JOIN #" + CHANNEL + "\r\n").encode(encoding='utf-8'))
		return True

	def requestPermissions():
		permissions = ["commands","membership","tags"]
		for p in permissions:
			self.send(("CAP REQ :twitch.tv/"+p+"\r\n").encode(encoding='utf-8'))
		return True

	def sendMessage(_msg): # send message to channel
		messageTemp = "PRIVMSG #" + CHANNEL + " :" + _msg
		self.send(messageTemp)
		return True

	def send(_msg): # print then send directly to socket
		print("< "+str(_msg))
		self.activeSocket.send(_msg)
		return True





def openSocket():
	s = socket.socket()
	s.connect((HOST, PORT))
	s.send(("PASS " + PASS + "\r\n").encode(encoding='utf-8'))
	s.send(("NICK " + IDENT + "\r\n").encode(encoding='utf-8'))
	s.send(("JOIN #" + CHANNEL + "\r\n").encode(encoding='utf-8'))

	# request commands (needed to whispter)
	# s.send(("CAP REQ :twitch.tv/commands\r\n").encode(encoding='utf-8'))

	# temp whisper test
	
	#s.send(("PRIVMSG #rub_my_bum :/w rubmybum tetttt\r\n").encode(encoding='utf-8'))
	return s
	
def sendMessage(s, message):
	messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
	s.send((messageTemp + "\r\n").encode(encoding='utf-8'))
	print("< " + str(messageTemp))

# 	Sending whisper format:
# 	PRIVMSG #jtv :/w otherusername HeyGuys
# 	Receiving whisper format:
#	:rubmybum!rubmybum@rubmybum.tmi.twitch.tv WHISPER gavin_test_bot :fafafafa
def sendWhisper(s, username, message):
	msg = "PRIVMSG #" + CHANNEL + " :/w "+username+" "+message
	s.send((msg + "\r\n").encode(encoding='utf-8'))
	print("Whispered: " + messageTemp)

def requestTwitchPermissions(s, permissionType):
	permissions = ["commands","membership","tags"]
	if permissionType not in permissions:
		return False
	s.send(("CAP REQ :twitch.tv/"+permissionType+"\r\n").encode(encoding='utf-8'))
