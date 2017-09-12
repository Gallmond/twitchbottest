import time
import module_share
import string
import random
import re

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
			if pollObj.voteFor(_votingUserName, _verboseVote):
				return True
		return False


def addPoll(_pollObj):
	print(module_share.all_polls)
	print(_pollObj)
	module_share.all_polls.append(_pollObj)
	# echo the poll question
	module_share.botObject.sendMessage(_pollObj.questionStr)
	module_share.botObject.sendMessage(_pollObj.returnVoteInstructions())
	return True

def getPollByCode(code):
	for pollObj in module_share.all_polls:
		if pollObj.confCode == code:
			return pollObj
	return False

class poll():

	def __init__(self, _questionStr, _optionsArr, timer):
		
		#defaults
		self.created = time.time()
		self.confCode = ""
		self.questionStr = ""
		self.optionsArr = {}
		self.timeoutSeconds = POLL_TIME_LIMIT
		self.ended = False
		self.numOfTopResults = 3
		self.allVoters = []

		for i in _optionsArr:
			self.optionsArr[i] = []
		self.timeoutSeconds = timer
		self.questionStr = _questionStr
		N = 6
		self.confCode = ''.join(random.choices(string.ascii_uppercase, k=N))

	def voteFor(self, _votingUserName, _verboseVote):
		if _votingUserName in self.allVoters:
			return False
		for i in self.optionsArr:
			if re.sub('[^0-9a-zA-Z ]', '', _verboseVote.lower()) == re.sub('[^0-9a-zA-Z ]', '', i.lower()):
			# if _verboseVote.lower() == i.lower():
				self.allVoters.append(_votingUserName)
				self.optionsArr[i].append(_votingUserName)
				return True
		return False

	def results(self): #d, key=lambda k: len(d[k]), reverse=True
		sortedArr = sorted(self.optionsArr, key=lambda k: len(self.optionsArr[k]), reverse=True)
		self.resultsArr = sortedArr
		print(sortedArr)
		return sortedArr

	def returnVoteInstructions(self):
		optionsWords = []
		for option in self.optionsArr:
			optionsWords.append(option)

		returnString = "Type !vote followed by: \""+("\", \"".join(optionsWords))+"\" to vote for that option. eg: \"!vote "+optionsWords[0]+"\""
		
		return returnString

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
			if thisCount == 0:
				break
			thisPercentage = (thisCount/totalVoteNumber)*100
			resultsPart.append(k+":"+str(thisCount)+"("+str(round(thisPercentage,2))+"%)") #someoption(100/50%)'
			i+=1
			if i >= self.numOfTopResults:
				break
		returnString = "Poll results: "+(", ".join(resultsPart))
		return returnString






		# poll ended! top results: someoption(100/50%), anotheroption(48/22%), thirdoption(12/5%)

	def end(self):
		self.ended = True;
		# send results to chat
