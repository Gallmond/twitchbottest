arr = [["dada", "fafa", "5tg4wtw"], ["th", "fr", "re", "re", "te"], ["fr"]]


class wowow():
	optionsArr = [["dada", "fafa", "5tg4wtw"], ["th", "fr", "re", "re", "te"], ["fr"]]

	def result(self):
		sortedArr = sorted(self.optionsArr, key=lambda optionsArr: len(optionsArr), reverse=True)
		self.sortedArr = sortedArr




neww = wowow()
print(neww.optionsArr)
neww.result()
print(neww.sortedArr)

