import datetime
import time
from datetime import datetime, date, time

class User:
    myName = ""
    mySchedule = None
    myBodyType = None
    myWorkoutSpecs = None

    def __init__(self, name, schedule=None, bodyType=None, workoutSpecs=None):
        self.myName = name
        self.mySchedule = schedule
        self.myBodyType = bodyType
        self.myWorkoutSpecs = workoutSpecs
    
    def __str__(self):
        return(self.myName + " " + str(self.mySchedule))
    @classmethod
    def getSchedule(self):
        return self.mySchedule
    @classmethod
    def getName(self):
        return self.myName

class schedule:
    courseList = []
    def __init__(self,cList):
        self.courseList = cList
    @classmethod
    def addCourse(self,c):
        self.courseList.append(c)
    @classmethod
    def removeCourse(self, c):
        self.courseList.remove(c)

    def __str__(self):
        printStatement = ""
        for i in self.courseList:
            printStatement = printStatement + " " + course.getName(i)
        return printStatement
    




class bodyType:
    height = 0
    weight = 0
    BMI = 0

    def __init__(self, h, w, bmi):
        self.height = h
        self.weight = w
        self.BMI = bmi

class workoutSpecs:
    benchMax = 0
    squatMax = 0
    deadliftMax = 0

    def __init__(self, bM, sM, dM):
        self.benchMax = bM
        self.squatMax = sM
        self.deadliftMax = dM

class course:
    courseName = ""
    courseStartTime = 0
    courseEndTime = 0
    courseDOW = ""
    
    def __init__(self, name, startTime=None, endTime=None, daysOfWeek=None):
        self.courseName = name
        self.courseStartTime = startTime
        self.courseEndTime = endTime
        self.courseDOW = daysOfWeek
    @staticmethod
    def getName(self):
        return(self.courseName)

    def __str__(self):
        return(self.courseName + "(" + str(self.courseStartTime) + "<-->" + str(self.courseEndTime) + ")")



courses = [course("cs"),course("math"),course("chem"),course("physics")]
c = course("cs", datetime.now(), datetime.now())
s = schedule(courses)
pat = User("pranay", s)

beta = datetime.date
print(str(c))

