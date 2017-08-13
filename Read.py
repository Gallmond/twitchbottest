import string
import module_share

def getUser(line):
	separate = line.split(":", 2)
	user = separate[1].split("!", 1)[0]
	return user
def getMessage(line):
	separate = line.split(":")
	elems = len(separate)
	message = separate[elems-1]
	return message

def pingPong(line):
	# handle ping/pong but ONLY from twitch
	if line.find("PING") == 0:
		module_share.botObject.sendMessage((line.replace("PING", "PONG"))) #pong back to twitch
		print("responded to twitch ping")
		return True
