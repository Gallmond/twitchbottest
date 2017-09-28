import pickle
import os
import datetime
print(
    datetime.datetime.fromtimestamp(
        int("1284101485")
    ).strftime('%Y-%m-%d %H:%M:%S')
)

with open('filestore/userlist.pkl', 'rb') as f:
	UL = pickle.load(f)


for key_username in UL:
	thisU = UL[key_username] 
	print("========== "+key_username+" ==========")
	print("opstatus: "+str(thisU.opstatus))
	print("subscriber: "+str(thisU.subscriber))
	print("username: "+str(thisU.username))
	print("points: "+str(thisU.points))
	print("inChannel: "+str(thisU.inChannel))
	print("messages (desc): ")
	for m in thisU.messages:
		stringPart = m[1].split(":",2)[2]
		ts = m[0]
		niceTime = datetime.datetime.fromtimestamp(int(ts)).strftime('%Y-%m-%d %H:%M:%S')
		print(str(niceTime)+" > "+str(stringPart))

