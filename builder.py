#File name: builder.py
#builder.py builds necessary pickles
#builder.py creates pickle of counter values in counter.data
#builder.py can be used to recover counter.data file
#builder.py builds dictionary for saving counts
#builder.py creates pickle of dictionary which store counter data


import pickle


a = '7'
f = open('counter.data', 'wb')
pickle.dump(a,f)
f.close()


file = open('store.data', 'wb')
store = {}
pickle.dump(store, file)
file.close()


