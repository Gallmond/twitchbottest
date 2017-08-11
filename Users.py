# =============================== user class
# - array of users
# - info like: username, id, inroom, lastmessage, opstatus, currencyamt
import uuid
import time

from Settings import USER_STARTING_POINTS



class Users():
	
	allUsers = [] # [guid, User]

	def newUser(self, username):
		now = time.time()
		newID = uuid.uuid4().hex
		thisUser = User(username, now)
		self.allUsers.append([newID, thisUser])
		return newID

	def getUserByUsername(self, _username):
		for i in self.allUsers:
			if i[1].username == username:
				return i
		return False

	def getUserById(self, _id):
		for i in self.allUsers:
			if i[0] == _id:
				return i
		return False


class User():

	def __init__(self, username, timeJoined):
		self.username = username
		self.timeJoined = timeJoined
		self.points = USER_STARTING_POINTS
		self.messages = [] # [[timestamp, "messagetext"],[timestamp, "messagetext"], ...]
		self.afk = False
		self.opstatus = "unknown"
