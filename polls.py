import time
import module_share
import string
import random

from Settings_polls import POLL_TIME_LIMIT, POLL_CHECK_FREQUENCY

class pollManager(): # STATiC ONLY
	lastTimeRun = 0

	def pollsChecker():
		tnow = time.time()
		if pollManager.lastTimeRun < tnow - POLL_CHECK_FREQUENCY:
			for pollObj in module_share.all_polls:
				if pollObj.created+pollObj.timeoutSeconds < tnow:
					pollObj.end()

	def voteWasCast(_votingUserName, _verboseVote):
		# check all options in all active polls
		for pollObj in module_share.all_polls:
			pollObj.voteFor(_votingUserName, _verboseVote)



def addPoll(pollObj):
	if pollObj not in module_share.all_polls:
		module_share.all_polls.append(pollObj)
		return True
	else:
		return False

def getPollByCode(code):
	for pollObj in module_share.all_polls:
		if pollObj.confCode == code:
			return pollObj
	return False

class poll():

	created = time.time()
	confCode = ""
	optionsArr = {}
	timeoutSeconds = POLL_TIME_LIMIT
	ended = False
	numOfTopResults = 3

	def __init__(self, _optionsArr, timer):
		for i in _optionsArr:
			self.optionsArr[i] = []
		self.timeoutSeconds = timer
		N = 6
		self.confCode = ''.join(random.choices(string.ascii_uppercase, k=N))


	def voteFor(self, _votingUserName, _verboseVote):
		for i in self.optionsArr:
			if _verboseVote.lower() == i.lower():
				self.optionsArr[i].append(_votingUserName)
				return True
		return False

	def results(self):
		sortedArr = sorted(self.optionsArr, key=lambda optionsArr: len(optionsArr), reverse=True)
		self.resultsArr = sortedArr
		return sortedArr

	def returnCommandString(self):
		returnString = "\"!poll "+self.confCode+" cancel\" to cancel poll. "
		returnString+= "\"!poll "+self.confCode+" end\" to end poll early. "
		returnString+= "\"!poll "+self.confCode+" status\" to see current votes. "
		return returnString

	def totalVotes(self):
		n = 0
		for option in self.optionsArr:
			for name in self.optionsArr[option]:
				n+=1
		return n

	def returnResultsString(self):
		#return True
		totalVoteNumber = self.totalVotes()
		resultsList = self.results()
		print(resultsList)
		resultsPart = []
		# get top X results
		i = 0
		for k in resultsList:
			thisCount = len(self.optionsArr[k])
			thisPercentage = (thisCount/totalVoteNumber)*100
			resultsPart.append(k+":"+str(thisCount)+"("+str(round(thisPercentage,2))+"%)") #someoption(100/50%)'
			i+=1
			if i >= self.numOfTopResults:
				break
		returnString = "poll ended! top results: "+(", ".join(resultsPart))
		return returnString






		# poll ended! top results: someoption(100/50%), anotheroption(48/22%), thirdoption(12/5%)

	def end(self):
		self.ended = True;
		# send results to chat
