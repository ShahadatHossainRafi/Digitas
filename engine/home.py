#File name: home.py

from engine.save import value1
from engine.save import value2
import pickle

f = open('counter.data')
var = pickle.load(f)
f.close()

var = int(var)
limit = 9999999999

def Counter(display_text):
	global var
	if var < limit:
            var = var + 1
            display_text.text = str(var)
            f = open('counter.data', 'wb')
            val = str(var)
            pickle.dump(val, f)
            f.close()
	else:
            display_text.text = "%s" %var


def Back(display_text):
	val = display_text.text
	global var
	try:
		var = int(val)
		if var > 0:
			var = var - 1
			val = str(var)
			display_text.text = val
		else:
			var = 0
		f = open('counter.data', 'wb')
		pickle.dump(val, f)
		f.close()
	except ValueError:
		if var > 0:
			var = var - 1
			val = str(var)
			display_text.text = val
		else:
			var = 0
		f = open('counter.data', 'wb')
		pickle.dump(val, f)
		f.close()


def Reset(display_text):
	global var
	var = 0
	display_text.text = str(var)
	f = open('counter.data', 'wb')
	val = str(var)
	pickle.dump(val, f)
	f.close()


def Reset_to(reset_to_text):
	val = reset_to_text.text
	try:
		var = int(val)
		global limit
		if var <= limit:
			global var
			f = open('counter.data', 'wb')
			val = str(var)
			pickle.dump(val, f)
			f.close()
		else:
			reset_to_text.text = 'Limit imposed'
	except ValueError:
		global limit
		reset_to_text.text = str(var)
		if var <= limit:
			global var
			f = open('counter.data', 'wb')
			val = str(var)
			pickle.dump(val, f)
			f.close()
		else:
			reset_to_text.text = 'Limit imposed'


def Limit(limit_display):
	val = limit_display.text
	try:
		a = int(val)
		global limit
		global a
		limit = a
	except ValueError:
		limit = var

###############- Slot 1 -###############
def Save_Fun1(save_display):
    print save_display
    f = open("engine/slot1.data", "w")
    savedict = {"name": int(save_display)}
    pickle.dump(savedict,f)
    f.close()

def LoaderFun1():
    global var
    var = value1


###############- Slot 2 -###############
def Save_Fun2(save_display):
    print save_display
    f = open("engine/slot2.data", "w")
    savedict = {"another": int(save_display)}
    pickle.dump(savedict,f)
    f.close()

def LoaderFun2():
    global var
    var = value2


def TimeDate():
    var = "some date"

