fileName = "config.cfg"

def buildConfig():
    configFile = open(fileName, "w")
    configFile.write()

def readConfig():
    configFile = open(fileName, "r")
    out = configFile.readline()
    if out.startswith("##"):
        print("its a header")
    while out != "":
        print(out)
        out = configFile.readline()
        if out.startswith("##"):
            print("its a header")





def updateConfig(fieldToUpdate, value):
    readConfig()

readConfig()