import pickle

###############- Slot 1 -###############
f = open("engine/slot1.data")
savedict = pickle.load(f)
print savedict
f.close()

for slot1, value1 in savedict.items():
    slot1 = slot1
    value1 = value1


###############- Slot 2 -###############
f = open("engine/slot2.data")
savedict = pickle.load(f)
print savedict
f.close()

for slot2, value2 in savedict.items():
    slot2 = slot2
    value2 = value2
