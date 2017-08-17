import module_share
import uuid
import time

from Read import getUser
from Settings import USER_STARTING_POINTS, CHANNEL, POINTS_AK_ADD, POINTS_AK_PERIOD, POINTS_NAME_PLURAL

class UserPoints():

	lastPresenceCheck = time.time()

	def add(userObj, add):
		userObj.points+= add
		return userObj.points

	def subtract(userObj, subtract):
		userObj.points-= subtract
		return userObj.points

	def presencePoints():
		now = time.time()
		pamnt = 0;
		usernm = 0;
		if UserPoints.lastPresenceCheck < now-POINTS_AK_PERIOD:

			for li in Users.userList:
				if li[1].afk is False:
					li[1].points += POINTS_AK_ADD
					usernm+=1
					pamnt+= POINTS_AK_ADD
			UserPoints.lastPresenceCheck = now

		print("added "+str(pamnt)+" points to "+str(usernm)+" users")
		# add X points to every user present in chat


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
		for li in Users.userList:
			print(li[1].username);



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
		else:
			last = ""

		# ========= MESSAGES FROM CHAT
		if isUserMessage(_msg):

			if userMessageStarts(_msg, "!"+POINTS_NAME_PLURAL): # user typed "!points"
				thisUser = middle.split("!")[0] 
				thisUserObject = Users.getUserByUsername(thisUser)
				thisUserPoints = thisUserObject.points
				msg = thisUser+" has "+str(thisUserPoints)+" "+POINTS_NAME_PLURAL
				module_share.botObject.sendMessage(msg)
				return True

		# ========= MESSAGES FROM CHAT END

		# ========= DIRECT WHISPER
		if isWhisper(_msg):

			if userMessageStarts(_msg, "hiya"):
				module_share.botObject.sendWhisper("back at ya", getUser(_msg))
				return False


		# ========= DIRECT WHISPER END



		


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
			return True

		# user left
		# > :ronni!ronni@ronni.tmi.twitch.tv PART #dallas
		if(middle.split(" ")[1] == "PART"):
			thisUser = middle.split("!")[0] 
			thisUserObject = Users.getUserByUsername(thisUser)
			thisUserObject.inChannel = False
			return True

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
			if i[1].username.lower() == _username.lower():
				return i[1]
		return False

	def getUserById(_id):
		for i in Users.userList:
			if i[0] == _id:
				return i[1]
		return False

	def getUserPoints(_id):
		for i in Users.userList:
			if i[0] == _id:
				return i[1].points
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



# helpers for checking what kind of incoming message
def userMessageStarts(_msg, _keyword):
	ma = _msg.split(":")
	if ma[2].find(_keyword)==-1:
		return False
	else:
		if ma[2].find(_keyword)==0:
			return True
		else:
			return False

def isWhisper(_msg):
	ma = _msg.split(":")
	if ma[1].split(" ")[1]=="WHISPER":
		return True
	else:
		return False

def isUserMessage(_msg):
	# format like:
	# > @badges=broadcaster/1;color=;display-name=RubMyBum;emotes=;id=b7b8bccd-ee77-4287-8868-3cf5b64f4cf4;mod=0;room-id=142411464;sent-ts=1502990928960;subscriber=0;tmi-sent-ts=1502990929450;turbo=0;user-id=142411464;user-type= :rubmybum!rubmybum@rubmybum.tmi.twitch.tv PRIVMSG #rubmybum :11456
	ma = _msg.split(":")
	if ma[1].split(" ")[1] == "PRIVMSG":
		return True
	else:
		return False
