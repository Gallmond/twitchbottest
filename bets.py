import time
import module_share
import string
import random
import re

from Settings_bets import BET_CHECK_FREQUENCY, BET_HOUSE_TAKE
# from Users import UserPoints

# only addpoll and end bet insance should send messages via bot

class betManager(): #always static
	lastTimeRun = 0

	def castBet(_bettingUser, _betOption ,_stakeAmount): # better can bet on each option, but only once per option
		#does ths option exist in any bet?
		for bet in module_share.all_bets:
			for option in bet.optionsArray:
				if _bettingUser.lower() in bet.optionsArray[option]:
					return False
				if _betOption.lower() == option.lower():
					# this option exists
					bet.optionsArray[option][_bettingUser.lower()] = int(_stakeAmount)
					return True
		return False

	def betsChecker():
		tnow = time.time()
		if betManager.lastTimeRun < tnow - BET_CHECK_FREQUENCY:
			for betObj in module_share.all_bets:
				if betObj.created+betObj.timeoutSeconds < tnow:
					betObj.end()

	def calcAllPayouts(_betDict): # this calculates payout rates and totals for all current bets in dict
		# total pool, and pools per option
		totalPool = 0
		optionsPools = {}
		for option in _betDict:
			optionsPools[option] = {"stakes":0,"total":0,"payoutrate":0}
			for better in _betDict[option]:
				totalPool+= _betDict[option][better]
				optionsPools[option]["total"]+= _betDict[option][better]
				optionsPools[option]["stakes"]+= 1

		# total pool sans house cut
		houseCut = round(totalPool*BET_HOUSE_TAKE)
		newTotalPool = totalPool-houseCut

		# calculate payout rate for each option
		for option in optionsPools:
			# skip maths if 0 stakes
			if optionsPools[option]["total"] != 0:
				optionsPools[option]["payoutrate"] = round(newTotalPool/optionsPools[option]["total"],2)

		return {"totalpool":totalPool, "options":optionsPools}

	def calcPayout(_betDict, _winnerStr):
		# get the total pool, and a dict of the totals for each option
		_winnerStr = _winnerStr.lower()
		totalPool = 0
		optionPool = {}
		for option in _betDict:
			optionPool[option] = 0;
			for better in _betDict[option]:
				optionPool[option]+= _betDict[option][better]
				totalPool+= _betDict[option][better]

		# now see how much the house gets, and take it off the total pool
		houseCut = round(totalPool*BET_HOUSE_TAKE)
		newTotalPool = totalPool-houseCut

		# calculate the payout rate with newTotalPool/winningoptiontotal
		payoutRate = round(newTotalPool/optionPool[_winnerStr],2) # like 1.25 ie. this would be a 25% return

		# calculate how much each winning better gets relative to their stake
		totalPaidOut = 0
		payouts = {}
		for better in _betDict[_winnerStr]:
			thisPayoutAmount = round(_betDict[_winnerStr][better]*payoutRate) 
			payouts[better] = thisPayoutAmount
			totalPaidOut += thisPayoutAmount

		# return dictionary of winner and how many points they've won
		return [payouts, totalPaidOut, payoutRate]

	def addBet(_betObj):
		if _betObj not in module_share.all_bets:
			module_share.all_bets.append(_betObj)
			module_share.botObject.sendMessage(_betObj.returnQuestionString())
			module_share.botObject.sendMessage(_betObj.returnVoteInstructions())
			return _betObj.confCode

	def betCancel(_confCode):
		for bet in module_share.all_bets:
			if bet.confCode == _confCode:
				module_share.all_bets.remove(bet)
				return True
		return False

	def betStatus(_confCode):
		# show current bet totals per option, and calculate rate like:
		# red:450(4/1) blue:100(2/1)
		returnString = ""
		for bet in module_share.all_bets:
			if _confCode == bet.confCode:
				infoDict = betManager.calcAllPayouts(bet.optionsArray)
				returnString += "Total staked:%s in " % infoDict["totalpool"]
				optionStringArr = []
				for option in infoDict["options"]:
					thisOptionString = "%s:%s(%s betters with rate %s)" % (option, infoDict["options"][option]["total"], infoDict["options"][option]["stakes"] ,infoDict["options"][option]["payoutrate"])
					optionStringArr.append(thisOptionString)
				returnString+= " ".join(optionStringArr)
		if returnString=="":
			returnString = "no such bet."
		return returnString

	def endBet(_confCode, _winnerStr):
		for bet in module_share.all_bets:
			if bet.confCode == _confCode:
				bet.end(None, _winnerStr)
				return True
		return False

class bet():

	def __init__(self, _creatingUser, _questionString, _optionsArray):
		self.createdBy = _creatingUser
		self._questionString = _questionString
		self.optionsArray = {}
		for i in _optionsArray:
			i = i.lower()
			self.optionsArray[i] = {} 

		N = 6
		self.confCode = ''.join(random.choices(string.ascii_uppercase, k=N))

	# this shows the command string for admins
	def returnCommandString(self):
		returnString = "\"!betcancel "+self.confCode+"\" to cancel bet. "
		returnString+= "\"!betend "+self.confCode+" winningoption\" to end the bet. "
		returnString+= "\"!betstatus "+self.confCode+"\" to see current bet amounts. "
		return returnString

	# this is the Q sent to the chat
	def returnQuestionString(self):
		returnString = self._questionString
		optionsString = ", ".join(self.optionsArray)
		returnString+= " "+optionsString
		return returnString

	# this is the line that explains how to vote
	def returnVoteInstructions(self):
		for option in self.optionsArray:
			anOption = option
			break
		returnString = "to place a bet type !stake followed by an option, and the number of points you are staking. eg: \"!stake "+anOption+" 140\""
		return returnString

	def sendResultString(self, _calculatedArr, _winnerStr):
		responseString = _winnerStr+" is the winner. Congrats. Paying out "+str(_calculatedArr[1])+" at rate of "+str(_calculatedArr[2])
		module_share.botObject.sendMessage(responseString)
		return True

	def placeBet(self, _userName, _option, _amount):
		# check option exists
		if _option not in self.optionsArray:
			return False
		self.optionsArray[_option][_userName] = _amount
		return True

	def end(self, _endingUser, _winningOption):
		payoutsArr = betManager.calcPayout(self.optionsArray, _winningOption)
		self.sendResultString(payoutsArr, _winningOption)
		module_share.UserPoints.betPayout(payoutsArr)
		module_share.all_bets.remove(self)
		return True
