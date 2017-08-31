import time
import module_share

from Settings_polls import POLL_TIME_LIMIT

def pollChecker():
	# does poll exist in shared?
	for p in module_share.all_polls:


class poll():

	created = time.time()
	confCode = ""
	optionsArr = []
	timeoutSeconds = POLL_TIME_LIMIT

	def __construct__(self, _optionsArr, timer, _confCode):
		for i in _optionsArr:
			self.optionsArr[i] = []
		self.timeoutSeconds = timer
		self.confCode = _confCode
		return self.timeoutSeconds

	def voteFor(self, _votingUserName, _verboseVote):
		for i in self.optionsArr:
			if _verboseVote.lower() == i.lower():
				self.optionsArr[i].append(_votingUserName)
				return True
		return False

	def results(self):
		sortedArr = sorted(self.optionsArr, key=lambda optionsArr: len(optionsArr), reverse=True)
		selt.resultsArr sortedArr
		return sortedArr