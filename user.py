class User:


    def __init__(self, name, times):
        self.myName = name
        self.mySchedule = times
        
    def getSchedule(self):
        return self.mySchedule
    def getName(self):
        return self.myName
