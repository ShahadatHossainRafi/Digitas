
#Changing "appvar" variable for controlling "App Sound" setting.
def AppVarFun(args1, args2):
    if args2 == True:
        f = open("engine/settings/appvar.py", "w")
        f.write("appvar = 1")
        f.close()
    elif args2 == False:
        f = open("engine/settings/appvar.py", "w")
        f.write("appvar = 0")
        f.close()


#Changing "startvar" variable for controlling "Startup Sound" setting.
def StartVarFun(args1, args2):
    if args2 == True:
        f = open("engine/settings/appvar.py", "w")
        f.write("appvar = 1")
        f.close()
    elif args2 == False:
        f = open("engine/settings/appvar.py", "w")
        f.write("appvar = 0")
        f.close()
