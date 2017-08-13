# =============================== user class
# - array of users
# - info like: username, id, inroom, lastmessage, opstatus, currencyamt
import uuid
import time

from Settings import USER_STARTING_POINTS, CHANNEL

class Users(): # ALWAYS CALL STATICALLY 

	userList = []

	def buildUserList(_msg): # from the initial join NAMES list
		# split names in this message
		ma = _msg.split(":")
		nl = ma[2].split(" ")
		# force broadcaster name into list
		nl.append(CHANNEL)
		for username in nl:
			_username = username.replace("\r\n","")
			# does this user already exist? if so mark as inchannel
			thisUserObject = Users.getUserByUsername(_username)
			if(thisUserObject):
				thisUserObject.inChannel = True
			else:
				Users.newUser(_username)
		print("Users.userList length ["+str(len(Users.userList))+"]")



	def UserListener(_msg):

		# discard if privmsg or whisper
		# whisper format:
		# > @badges=;color=;display-name=RubMyBum;emotes=;message-id=4;thread-id=142411464_166478382;turbo=0;user-id=142411464;user-type= :rubmybum!rubmybum@rubmybum.tmi.twitch.tv WHISPER gavin_test_bot :this is a whisper
		# message format:
		# > @badges=broadcaster/1;color=;display-name=RubMyBum;emotes=;id=0f049fc9-05df-4d09-b570-c32f9b4447aa;mod=0;room-id=142411464;sent-ts=1502633648703;subscriber=0;tmi-sent-ts=1502633650176;turbo=0;user-id=142411464;user-type= :rubmybum!rubmybum@rubmybum.tmi.twitch.tv PRIVMSG #rubmybum :This is a normal incoming message
		front = _msg.split(":")[0]
		middle = _msg.split(":")[1]
		if(len(_msg.split(":"))>2): # does it even have a last part?
			last = _msg.split(":")[2]

		if(middle.split(" ")[1] == "WHISPER"): # this is a whisper
			return False
		elif(middle.split(" ")[1] == "PRIVMSG"): # this is a normal message
			return False


		# check for userlist building
		if(middle.split(" ")[1] == "353"):
			buildUserList(_msg)
			return False


		# example ronni joins the channel:
		# > :ronni!ronni@ronni.tmi.twitch.tv JOIN #dallas
		if(_msg.find("JOIN #"+CHANNEL+"\r\n")==len(_msg)-len("JOIN #"+CHANNEL+"\r\n")): # check if msg ends "JOIN #channelname"
			# get username
			newUserName = _msg.split("!")[0][1:].replace("\r\n", "")
			return Users.newUser(newUserName)
		#elif():

		# example with tags of ronni joining channel:
		# > @color=#0D4200;display-name=ronni;emote-sets=0,33,50,237,793,2126,3517,4578,5569,9400,10337,12239;mod=1;subscriber=1;turbo=1;user-type=staff :tmi.twitch.tv USERSTATE #dallas
		
		# mode change
		# > :jtv MODE #rubmybum +o rubmybum
		if(middle.find("jtv MODE #"+CHANNEL)==0):
			thisUser = middle.split(" ")[len(middle.split(" "))-1]
			mode = middle.split(" ")[len(middle.split(" "))-2] # should be '-o' or '+o'

			thisUserObject = Users.getUserByUsername(thisUser)
			thisUserObject.opstatus = mode
			return thisUserObject.opstatus

		# user left
		# > :ronni!ronni@ronni.tmi.twitch.tv PART #dallas
		if(middle.split(" ")[1] == "PART"):
			thisUser = middle.split("!")[0].split(":")[1] 
			thisUserObject = Users.getUserByUsername(thisUser)
			thisUserObject.inChannel = False
			return thisUserObject

		return False

	def newUser(_username):
		now = time.time()
		newID = uuid.uuid4().hex
		thisUser = User(_username, now)
		Users.userList.append([newID, thisUser])
		print("new user created ["+thisUser.username+"]")
		return newID

	def getUserByUsername(_username):
		for i in Users.userList:
			print(i)
			if i[1].username.lower() == _username.lower():
				return i[1]
		return False

	def getUserById(_id):
		for i in Users.userList:
			if i[0] == _id:
				return i[1]
		return False


class User():

	def __init__(self, username, timeJoined):
		self.username = username
		self.timeJoined = timeJoined
		self.points = USER_STARTING_POINTS
		self.messages = [] # [[timestamp, "messagetext"],[timestamp, "messagetext"], ...]
		self.afk = False
		self.opstatus = "unknown"
		self.inChannel = True

