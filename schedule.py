class schedule:
    eventList = []
    def __init__(self,eventList):
        self.courseList = cList
    def addEvent(e):
        self.courseList.append(e)
    def removeEvent(name):
        for event in eventList:
            if (event.getName() == name):
                eventList.remove(event)
    def toString(self):
        s = "Schedule consists of "
        for event in self.eventList:
            if event != None:
                s = s + event.getName() + " from " + str(event.getTime()[0]) + " to " + + str(event.getTime()[1])
        return s

class event:
    def __init__(self, name, startTime, endTime):
        self.name = name
        self.startTime = startTime
        self.endTime = endTime
    def getName(self):
        return self.name
    def getTime(self):
        return [self.startTime, self.endTime]
