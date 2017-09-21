import time
import module_share
import string
import random
import re

from Settings_bets import BET_CHECK_FREQUENCY, BET_HOUSE_TAKE
from Users import UserPoints

# only addpoll and end bet insance should send messages via bot

class betManager(): #always static
	lastTimeRun = 0

	def betsChecker():
		tnow = time.time()
		if betManager.lastTimeRun < tnow - BET_CHECK_FREQUENCY:
			for betObj in module_share.all_bets:
				if betObj.created+betObj.timeoutSeconds < tnow:
					betObj.end()

	def calcPayout(_betDict, _winnerStr):
		# get the total pool, and a dict of the totals for each option
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
		payoutRate = round(newTotalPool/optionPool[_winnerStr],2) # like 1.25

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
		return True

class bet():

	def __init__(self, _creatingUser, _questionString, _optionsArray):
		self.createdBy = _creatingUser
		self._questionString = _questionString
		self.optionsArray = {}
		for i in _optionsArray:
			self.optionsArray[i] = {} 

		N = 6
		self.confCode = ''.join(random.choices(string.ascii_uppercase, k=N))

	# this is the Q sent to the chat
	def returnQuestionString(self):
		return self._questionString

	# this is the line that explains how to vote
	def returnVoteInstructions(self):
		for option in self.optionsArray:
			anOption = option
			break
		returnString = "to place a bet type !stake followed by an option, and the number of points you are staking. eg: \"!stake "+anOption+" 140\""
		return True

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
		UserPoints.betPayout(payoutsArr)
		return True





