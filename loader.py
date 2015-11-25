import pickle

f = open('counter.data')
var = pickle.load(f)
f.close()
