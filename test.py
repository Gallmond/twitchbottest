# {'rubmybum': []}
# Traceback (most recent call last):
#   File "C:\Users\Gavin\Desktop\python\Run.py", line 57, in <module>
#     if f(line):			
#   File "C:\Users\Gavin\Desktop\python\Users.py", line 171, in UserListener
#     thisCommand = addPendingCommand(thisUser, "points", thisCommandDict)
#   File "C:\Users\Gavin\Desktop\python\Users.py", line 494, in addPendingCommand
#     if c["confcode"]==confcode:
# TypeError: string indices must be integers


o = {'rubmybum': []}
print(o)
for u in o:
	print(o[u])
	for c in o[u]:
		print(c)
		if c["confcode"]==confcode:
			continue
