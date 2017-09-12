class fun_Obj():

	fun_arr = []

	def __init__(self, coolWord):
		self.fun_arr.append(coolWord)

	def printArr(self):
		print(self.fun_arr)


allobjs = []

fun_1 = fun_Obj("foo")
fun_2 = fun_Obj("bar")

allobjs.append(fun_1)
allobjs.append(fun_2)

for ob in allobjs:
	ob.printArr()




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