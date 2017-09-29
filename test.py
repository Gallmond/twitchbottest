
if False:
	print("HHHH")
else:
	print("RRRR")

# lip = "Lorem ipsum dolor sit amet, ius ex lorem minim adipisci, ex mei melius timeam postulant. In dicat nostro incorrupte vel. Eum at utroque sadipscing, id vitae numquam partiendo sed. Eu pri apeirian rationibus. Vim ad stet consetetur, nec ne justo intellegat appellantur. Sit ex ocurreret iracundia, sit esse nulla intellegam ea. Cum alii delenit neglegentur in, error nonumy vocent cu quo, sale persecuti his an. Dicant fastidii referrentur at est, purto adhuc meliore vix cu. Et eam libris electram consequuntur, est graecis corpora ea. Labore dissentiet ei pri."
# # 561 char

# t = "   www  ew    "
# t = t.strip()
# print("zz"+t+"zz")

# splitSize = 496
# splitSize = 50

# print(lip[0:5])

# def coolPrinter(_msg):
# 	print("> "+_msg)
# 	return True


# def coolPrinter2(_msg):
# 	if len(_msg)>500:
# 		splitMessage = [_msg[i:i+splitSize] for i in range(0, len(_msg), splitSize)]

# 		for i in range(0,len(splitMessage)):
# 			thisStr = ""
# 			if i == 0:
# 				print("> "+splitMessage[i].strip()+"--")
# 			elif i == len(splitMessage)-1:
# 				print("> --"+splitMessage[i].strip())
# 			else:
# 				print("> --"+splitMessage[i].strip()+"--")


# print(range(0,1,9))

# coolPrinter(lip)
# coolPrinter2(lip)


#s = print "Let's talk about %s." % my_name


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