from polls import poll, pollManager, addPoll
import module_share

module_share.all_polls = []

x = poll("Fave Harry Potter char?",["harry's balls","ron's arse","hedwig's knob","snape's turd"], -20);
addPoll(x)

print(x.confCode)

# cast a vote
pollManager.voteWasCast("barry", "ron")
pollManager.voteWasCast("farry", "ron")
pollManager.voteWasCast("warry", "hedwig")

for p in module_share.all_polls:
	print(p.optionsArr)

# end
pollManager.pollsChecker()

for p in module_share.all_polls:
	print(p.ended)
	print(p.returnCommandString())
	print(p.returnResultsString())


print("======")
print("======")
print("======")

sss = "fun string last word is woooo"
lastspace = sss.rfind(" ")
print(sss[lastspace+1:])