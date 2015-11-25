
def activefun(arg1, arg2):
    if arg2 == True:
        f = open("activevar.py", "w")
        f.write("activevar = 1")
        f.close()
    elif arg2 == False:
        f = open("activevar.py", "w")
        f.write("activevar = 0")
        f.close()
