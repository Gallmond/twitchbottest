import pickle
import os

with open('filestore/userlist.pkl', 'rb') as f:
	UL = pickle.load(f)


for key_username in UL:
	thisU = UL[key_username] 
	print("=========="+key_username+"==========")
	print("twitchid: "+str(thisU.twitchid))
	print("username: "+str(thisU.username))
	print("timeJoined: "+str(thisU.timeJoined))
	print("points: "+str(thisU.points))
	print("messages: ")
	for m in thisU.messages:
		print(m)
	print("opstatus: "+str(thisU.opstatus))
	print("inChannel: "+str(thisU.inChannel))
