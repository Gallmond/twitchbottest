class fun_Obj():

	def __init__(self, coolWord):
		self.name = coolWord

	def printName(self):
		print(self.name)

	def delSelf(self):
		allobjs.remove(self)

def getObByName(_name):
	for ob in allobjs:
		if ob.name == _name:
			return ob
	return False


allobjs = []

fun_1 = fun_Obj("foo")
fun_2 = fun_Obj("bar")
fun_3 = fun_Obj("deleteme")

allobjs.append(fun_1)
allobjs.append(fun_2)
allobjs.append(fun_3)

print(allobjs)

for ob in allobjs:
	ob.printName()

returnedOb = getObByName("deleteme")

if returnedOb in allobjs:
	print("foundit")
	# allobjs.remove(returnedOb)
	returnedOb.delSelf()

print(allobjs)

for ob in allobjs:
	ob.printName()

try:
	allobjs.remove(returnedOb)
except ValueError:
	print("no val")

class funClass():
	static_variable = "hiya"

	def __init__(self):
		instance_variable = "iruni is hot" 



# from polls import poll, pollManager, addPoll
# import module_share

# module_share.all_polls = []

# x = poll("Fave Harry Potter char?",["harry's balls","ron's arse","hedwig's knob","snape's turd"], -20);
# addPoll(x)

# print(x.confCode)

# # cast a vote
# pollManager.voteWasCast("barry", "ron")
# pollManager.voteWasCast("farry", "ron")
# pollManager.voteWasCast("warry", "hedwig")

# for p in module_share.all_polls:
# 	print(p.optionsArr)

# # end
# pollManager.pollsChecker()

# for p in module_share.all_polls:
# 	print(p.ended)
# 	print(p.returnCommandString())
# 	print(p.returnResultsString())


# print("======")
# print("======")
# print("======")

# sss = "fun string last word is woooo"
# lastspace = sss.rfind(" ")
# print(sss[lastspace+1:])