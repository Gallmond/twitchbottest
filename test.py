
s = "!stake red team 150"
amount = s.rsplit(" ",1)[1]

if not amount.isdigit():
	print("not digit")

option = s.split(" ",1)[1]
option = option.rsplit(" ",1)[0]

print(amount)
print(option)


# from bets import betManager, bet
# import module_share

# module_share.all_bets = []

# class botObject():

# 	def sendMessage(self, _msg):
# 		print("< "+_msg);
# 		return True

# module_share.botObject = botObject()



# thisBet = bet("gavTest", "who will win", ["red", "blue", "orange"]) # _creatingUser, _questionString, _optionsArray 
# betManager.addBet(thisBet)



# for bet in module_share.all_bets:
# 	print(bet)

# print("end")

# houseTake = 0.05 # 5%

# bets = {
# 	"orange":{"barry":25,"gavin":50,"terry":100},
# 	"blue":{"harry":90,"james":40},
# 	"green":{"ron":60,"july":70},
# 	"yellow":{"fred":15}
# }

# # test overwhelming winner
# bets = {
# 	"orange":{"barry":25,"gavin":50,"terry":100,"roger":30,"grace":50,"lauren":75,"alex":50,"hollie":30},
# 	"blue":{"harry":90,"james":40}
# }

# print("all bets:")
# print(bets)

# winTotals = {}
# totalPool = 0

# for colour in bets:
# 	winTotals[colour] = 0
# 	for better in bets[colour]:
# 		winTotals[colour] += bets[colour][better]
# 		totalPool+= bets[colour][better]

# winner = "orange"

# print("total pool:"+str(totalPool))
# print("house take is: "+str(houseTake))

# poolMinusTake = round(totalPool-(totalPool*houseTake),2)
# print("pool sans the houses take of "+str((totalPool*houseTake))+" is "+str(poolMinusTake))

# calcNumber = round(poolMinusTake/winTotals[winner],2)
# print("payout odds based on amount bet:"+str(calcNumber))

# # so the people get back their stake x that number
# payoutTotal = 0
# for name in bets[winner]:
# 	thisPayout = round(bets[winner][name]*calcNumber)
# 	payoutTotal+= thisPayout
# 	print(name+" gets "+str(thisPayout))

# print("total payout was: "+str(payoutTotal))
# print("calculated house take plus payout is "+str((totalPool*houseTake)+payoutTotal))

 #$881.51 / $110.00 = 8.01

#poolminustake / winningpool = 

# 	orange:
# 		barry: 25
# 		gavin: 50
# 		terry: 100

# 	blue:
# 		harry: 90
# 		james: 40

# class fun_Obj():

# 	def __init__(self, coolWord):
# 		self.name = coolWord

# 	def printName(self):
# 		print(self.name)

# 	def delSelf(self):
# 		allobjs.remove(self)

# def getObByName(_name):
# 	for ob in allobjs:
# 		if ob.name == _name:
# 			return ob
# 	return False


# allobjs = []

# fun_1 = fun_Obj("foo")
# fun_2 = fun_Obj("bar")
# fun_3 = fun_Obj("deleteme")

# allobjs.append(fun_1)
# allobjs.append(fun_2)
# allobjs.append(fun_3)

# print(allobjs)

# for ob in allobjs:
# 	ob.printName()

# returnedOb = getObByName("deleteme")

# if returnedOb in allobjs:
# 	print("foundit")
# 	# allobjs.remove(returnedOb)
# 	returnedOb.delSelf()

# print(allobjs)

# for ob in allobjs:
# 	ob.printName()

# try:
# 	allobjs.remove(returnedOb)
# except ValueError:
# 	print("no val")

# class funClass():
# 	static_variable = "hiya"

# 	def __init__(self):
# 		instance_variable = "iruni is hot" 



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