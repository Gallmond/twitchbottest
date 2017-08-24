pendingCommand = {"type":"point", "params":{"amnt": +122, "target": "barry"}}
print(pendingCommand)

pendingCommand2 = {}
pendingCommand2["type"] = "point"
pendingCommand2["params"] = {"amnt": +122, "target": "barry"}
print(pendingCommand2)

st = "number -11"
sa = st.split(" ")
print(sa)
print(int(sa[1]))
print(100+int(sa[1]))

string = "-1, -2, 3, 4, 5"
print([int(el) for el in string.split(',')]) 