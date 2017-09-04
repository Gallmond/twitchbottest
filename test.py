from polls import poll, pollManager, addPoll
import module_share

module_share.all_polls = []

x = poll(["foo","bar"], -20);
addPoll(x)

print(x.confCode)

# cast a vote
pollManager.voteWasCast("barry", "foo")
pollManager.voteWasCast("farry", "foo")
pollManager.voteWasCast("warry", "bar")

for p in module_share.all_polls:
	print(p.optionsArr)

# end
pollManager.pollsChecker()

for p in module_share.all_polls:
	print(p.ended)
	print(p.returnCommandString())
	print(p.returnResultsString())


i = 0
while i < 5:
	print(i)
	i+=1

# arr = [["dada", "fafa", "5tg4wtw"], ["th", "fr", "re", "re", "te"], ["fr"]]


# class wowow():
# 	optionsArr = [["dada", "fafa", "5tg4wtw"], ["th", "fr", "re", "re", "te"], ["fr"]]

# 	def result(self):
# 		sortedArr = sorted(self.optionsArr, key=lambda optionsArr: len(optionsArr), reverse=True)
# 		self.sortedArr = sortedArr




# neww = wowow()
# print(neww.optionsArr)
# neww.result()
# print(neww.sortedArr)

