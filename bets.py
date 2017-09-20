import time
import module_share
import string
import random
import re

from Settings_bets import BET_CHECK_FREQUENCY

# odds work like fractions or decimals:
# 4/1 or 4.00
# ie, for every 1 bet, you get 4 back (your stake + 3). or:
# winnings = stake*odds

# if options are blue and orange to win and bets are like:
# 	orange:
# 		barry: 25
# 		gavin: 50
# 		terry: 100

# 	blue:
# 		harry: 90
# 		james: 40

# the total in the pool is
# 	175 in orange
# 	130 in blue
# 	or 305 in total

# only two options with 2/1 odds each means that if orange wins the total payout would be:
# 	barry: 50
# 	gavin: 100
# 	terry: 200
# 	or 350 in total
# which is more than the entire pool and points have been added to the total system, rather than removed or transferred from some players to others...

# get around this by only allowing bets to go ahead if the total pool is higher than the biggest paying out option?
# 	That would cause a lot of dead end bets though... 

# change payout odds dynamically depending on how loaded an option is?




class betManager(): #always static
	lastTimeRun = 0

	def betsChecker():
		tnow = time.time()
		if betManager.lastTimeRun < tnow - BET_CHECK_FREQUENCY:
			for betObj in module_share.all_bets:
				if betObj.created+betObj.timeoutSeconds < tnow:
					betObj.end()



class bet():

	def __init__(self, _creatingUser, _questionString, _optionsArray, _houseTake):
		if _winRate is null:
			self.houseTake = BET_HOUSE_TAKE
		else:
			self.houseTake = _houseTake

		self.createdBy = _creatingUser
		self._questionString = _questionString
		self.optionsArray = {}
		for i in _optionsArray:
			# like:
			# self.optionsArray: {
			# 	blue:[
			# 			{barry:25},
			# 			{gavin:50},
			# 			{terry:100}
			# 		], 
			# 	orange:[
			# 			{harry:99},
			# 			{james:40}
			# 		]	
			# }
			self.optionsArray[i] = {} 

		N = 6
		self.confCode = ''.join(random.choices(string.ascii_uppercase, k=N))