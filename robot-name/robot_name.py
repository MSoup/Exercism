import random as r

class Robot:
    def __init__(self):
        self.nameList = []
        self.name = self.genName()

    def genName(self):
        newName = chr(r.randint(65,90)) + chr(r.randint(65,90)) + str(r.randint(0,9)) + str(r.randint(0,9)) + str(r.randint(0,9))

        if self.isValid(newName):
            self.nameList.append(newName)
            return newName
        else:
            return self.genName()
    
    def reset(self):
        self.name = self.genName()
        return self.name 
        
    def isValid(self, name):
        if name in self.nameList:
            return False
        return True