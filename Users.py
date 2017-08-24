import module_share
import uuid
import time
import pickle

from Read import getUser
from Settings import IDENT, USER_STARTING_POINTS, CHANNEL, USER_AFK_TIMER, USER_MESSAGES_STORED, FILE_SAVE_PERIOD
from Settings_points import POINTS_AK_ADD, POINTS_AK_PERIOD, POINTS_NAME_PLURAL, POINTS_NAME, POINTS_BAD_FORMAT, POINTS_GIFT_SELF, POINTS_NOT_ENOUGH, POINTS_CONFIRM, POINTS_BOT_RESPONSE
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
			parseUserStateChange(_msg)
			return True

		# ========= USER STATE CHANGE END


		# ========= WHISPERS FROM MODS
		if isWhisper(_msg):
			thisUser = middle.split("!")[0]
			if Users.userList[thisUser].opstatus == "+o":
				# ADMIN LISTENING HERE
				

				# !points username to list specific users points
				if userMessageStarts(_msg, "!points "):
					#check format
					userMsgArr = last.split(" ")
					if len(userMsgArr)!=2:
						return True # invalid foramt
					if userMsgArr[1] not in Users.userList:
						return True # user not exist
					else:
						thisUserPoints = Users.userList[userMsgArr[1]].points
						module_share.botObject.sendWhisper(userMsgArr[1]+" has "+str(thisUserPoints)+" points", thisUser)
				# !points username end


				# !allPoints to list every users points
				if userMessageStarts(_msg, "!allpoints"):
					outputStr = "|"
					for key in Users.userList:
						outputStr+= str(key)+": "+str(Users.userList[key].points)

					# is string too big?

					charMax = 450
					stringArr = [outputStr[i:i+charMax] for i in range(0, len(outputStr), charMax)]
					for element in stringArr:
						module_share.botObject.sendWhisper(element, thisUser)
					return True;
				# !allpoints end

				# !setpoints username number
				# !setpoints end



				# ADMIN LISTENING END



		# ========= WHISPERS FROM MODS END



		# ========= MESSAGES FROM CHAT USERS
		if isUserMessage(_msg) or isWhisper(_msg):

			#sendWhisper(self, _msg, _username)
			isWhisperType = isWhisper(_msg)
			thisUser = middle.split("!")[0]

			logMessage(_msg)

			# user typed "!points"
			if userMessageStarts(_msg, "!"+POINTS_NAME_PLURAL): 

				thisUserObject = Users.userList[thisUser]
				thisUserPoints = thisUserObject.points
				msg = thisUser+" has "+str(thisUserPoints)+" "+POINTS_NAME_PLURAL
				if isWhisperType:
					module_share.botObject.sendWhisper(msg, thisUser)
				else:
					module_share.botObject.sendMessage(msg)

				return True
			
			# user typed !give username X eccies
			if userMessageStarts(_msg, "!give"): 
				tempmsg = _msg.replace("\r\n","")
				if tempmsg.find(POINTS_NAME_PLURAL) == len(tempmsg)-len(POINTS_NAME_PLURAL) or tempmsg.find("1 "+POINTS_NAME) == len(tempmsg)-len("1 "+POINTS_NAME): # message ends with the plural name
					thisUserObject = Users.userList[thisUser]
					thisUserPoints = thisUserObject.points
					thisUserGiving = last.split(" ")
					if len(thisUserGiving)!=4:
						if isWhisperType:
							module_share.botObject.sendWhisper(POINTS_BAD_FORMAT, thisUser)
						else:
							module_share.botObject.sendMessage(POINTS_BAD_FORMAT)

						return True
					else:
						targetUser = thisUserGiving[1].lower()

					#can't give to self, bot can though
					if targetUser == thisUser:
						if isWhisperType:
							module_share.botObject.sendWhisper(POINTS_GIFT_SELF, thisUser)
						else:
							module_share.botObject.sendMessage(POINTS_GIFT_SELF)

						return True

					#does user even have this many points?
					if int(thisUserPoints) < int(thisUserGiving[2]):
						msgToSend = POINTS_NOT_ENOUGH
						msgToSend = msgToSend.replace("{pointamount}", str(thisUserPoints))
						if isWhisperType:
							module_share.botObject.sendWhisper(msgToSend, thisUser)
						else:
							module_share.botObject.sendMessage(msgToSend)

						return True
					else:
						pointsToGive = int(thisUserGiving[2])

					#does target user exist
					if targetUser in Users.userList:
						Users.userList[targetUser].points += pointsToGive;
						Users.userList[thisUser].points -= pointsToGive;
						msgToSend = POINTS_CONFIRM.replace("{giver}", str(thisUser))
						msgToSend = msgToSend.replace("{target}", str(targetUser))
						msgToSend = msgToSend.replace("{amountgiven}", str(pointsToGive))

						# if gifting to the bot
						if targetUser == IDENT.lower():
							msgToSend+=POINTS_BOT_RESPONSE
						print(msgToSend)
						if isWhisperType:
							module_share.botObject.sendWhisper(msgToSend, thisUser)
						else:
							module_share.botObject.sendMessage(msgToSend)
					else:
						if isWhisperType:
							module_share.botObject.sendWhisper(targetUser+" doesn't exist", thisUser)
						else:
							module_share.botObject.sendMessage(targetUser+" doesn't exist")



		# ========= MESSAGES FROM CHAT END



		


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
		self.opstatus = "unknown"
		self.subscriber = "unknown"
		self.usertype = "unknown"
		self.username = username
		self.timeJoined = timeJoined
		self.points = USER_STARTING_POINTS
		self.messages = [] # [[timestamp, "messagetext"],[timestamp, "messagetext"], ...]
		self.inChannel = True



# helpers for checking what kind of incoming message
def userMessageStarts(_msg, _keyword):
	ma = _msg.split(":")
	print(ma[2])

	print(_keyword)

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
	with open('filestore/userlist.pkl', 'r+b') as f:
		if f.seek(0,2) == 0:
			print("loaded empty userlist")
			return {}
		else:
			f.seek(0)
			print("loaded userlist from file")
			return pickle.load(f)

def saveUserListToFile(_userListArr):
	with open('filestore/userlist.pkl', 'r+b') as f:
		pickle.dump(_userListArr, f, pickle.HIGHEST_PROTOCOL)
		print("saved userlist to file")
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

def parseUserStateChange(_msg):
	states = _msg.split(":")[0] # this contains all states
	if states.find("@")==0:
		states = states[1:] # snip the @ off the front
	states = states.split(";")
	tempDict = {}
	for i in states:
		tempDict[i.split("=")[0]] = i.split("=")[1]

	if "display-name" in tempDict and tempDict["display-name"]!="":
		thisUserName = tempDict["display-name"].lower()
	else:
		return False

	if "mod" in tempDict:
		if tempDict["mod"] == 1:
			Users.userList[thisUserName].opstatus = "+o"
	if "subscriber" in tempDict:
		if tempDict["subscriber"] == 1:
			Users.userList[thisUserName].subscriber = True
	if "userType" in tempDict:
		if tempDict["userType"] == 1:
			Users.userList[thisUserName].usertype = tempDict["userType"]
	return True


