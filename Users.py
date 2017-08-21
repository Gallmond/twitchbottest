import module_share
import uuid
import time
import pickle

from Read import getUser
from Settings import USER_STARTING_POINTS, CHANNEL, POINTS_AK_ADD, POINTS_AK_PERIOD, POINTS_NAME_PLURAL, USER_AFK_TIMER, USER_MESSAGES_STORED, FILE_SAVE_PERIOD

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

			for userName in Users.userList:
				if isUserAfk(userName) is False:
					Users.userList[userName].points += POINTS_AK_ADD
					usernm+=1
					pamnt+= POINTS_AK_ADD
			UserPoints.lastPresenceCheck = now

			print("added "+str(pamnt)+" points to "+str(usernm)+" users")
			# add X points to every user present in chat


class Users(): # ALWAYS CALL STATICALLY 

	userListLoadedTime = time.time()
	userListSavedTime = time.time()
	userList = {}

	def saveUserFile():
		if Users.userListSavedTime < time.time()-FILE_SAVE_PERIOD:
			saveUserListToFile(Users.userList)
			Users.userListSavedTime = time.time()
			print("saved userlist to file")
		return True

	def customInit():
		# load userlist
		Users.userList = loadUserListFromFile()
		Users.userListLoadedTime = time.time()
		print("loaded userList "+str(len(Users.userList)))

	def buildUserList(_msg):

		# split names in this message
		ma = _msg.split(":")
		nameList = ma[2].split(" ")
		# force broadcaster name into list
		nameList.append(CHANNEL)
		for userName in nameList:
			userName = userName.replace("\r\n","")

			# does this exist?
			if userName in Users.userList:
				# just mark as present
				Users.userList[userName].inChannel = True
			else:
				# add new user
				Users.addNewUser(userName)
		print("userlist length: "+str(len(Users.userList)))

	def UserListener(_msg):

		front = _msg.split(":")[0]
		middle = _msg.split(":")[1]
		if(len(_msg.split(":"))>2): # does it even have a last part?
			last = _msg.split(":")[2]
		else:
			last = ""


		# ========= USER STATE CHANGE
		if isUserState(_msg):
			return True

		# ========= USER STATE CHANGE END



		# ========= MESSAGES FROM CHAT
		if isUserMessage(_msg):

			logMessage(_msg)

			if userMessageStarts(_msg, "!"+POINTS_NAME_PLURAL): # user typed "!points"
				thisUser = middle.split("!")[0] 
				thisUserObject = Users.userList[thisUser]
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
			thisUserObject = Users.userList[thisUser]
			thisUserObject.opstatus = mode
			return True

		# user left
		# > :ronni!ronni@ronni.tmi.twitch.tv PART #dallas
		if(middle.split(" ")[1] == "PART"):
			thisUser = middle.split("!")[0] 
			thisUserObject = Users.userList[thisUser]
			thisUserObject.inChannel = False
			return True

		return False

	def addNewUser(_userName):
		now = time.time()
		thisUser = User(_userName, now)
		Users.userList[_userName] = thisUser
		print("created new user "+thisUser.username)
		return _userName


class User():

	def __init__(self, username, timeJoined):
		self.twitchid = "unknown"
		self.username = username
		self.timeJoined = timeJoined
		self.points = USER_STARTING_POINTS
		self.messages = [] # [[timestamp, "messagetext"],[timestamp, "messagetext"], ...]
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

def isUserState(_msg):
	ma = _msg.split(":")
	if ma[1].split(" ")[1]=="USERSTATE":
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
	ma = _msg.split(":")
	if ma[1].split(" ")[1] == "PRIVMSG":
		return True
	else:
		return False

def loadUserListFromFile():
	print("loadUserListFromFile")
	with open('filestore/userlist.pkl', 'r+b') as f:
		if f.seek(0,2) == 0:
			return {}
		else:
			f.seek(0)
			return pickle.load(f)

def saveUserListToFile(_userListArr):
	print("saveUserListToFile")
	with open('filestore/userlist.pkl', 'wb') as f:
		pickle.dump(_userListArr, f, pickle.HIGHEST_PROTOCOL)
		print("saveUserListToFile END")
		return True

def isUserAfk(_userName):
	if _userName in Users.userList:
		if len(Users.userList[_userName].messages)==0:
			return True
		elif Users.userList[_userName].messages[0][0] > time.time()-USER_AFK_TIMER:
			return False
	else:
		True

def logMessage(_msg):
	front = _msg.split(":")[0]
	middle = _msg.split(":")[1]
	if(len(_msg.split(":"))>2): # does it even have a last part?
		last = _msg.split(":")[2]
	else:
		last = ""
	# log this users message
	thisUser = middle.split("!")[0] 
	Users.userList[thisUser].messages.insert(0,[time.time(), _msg])
	if len(Users.userList[thisUser].messages) > USER_MESSAGES_STORED:
		Users.userList[thisUser].messages.pop()

	# for testing
	#saveUserListToFile(Users.userList)