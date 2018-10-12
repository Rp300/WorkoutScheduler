class User:
    myCourses = None
    myBodyType = None
    myWorkoutSpecs = None
    def __init__(self, courses, bodyType, workoutSpecs):
        self.myCourses = courses
        self.myBodyType = bodyType
        self.myWorkoutSpecs = workoutSpecs
class schedule:
    courseList = []
    def __init__(self,cList):
        self.courseList = cList
    
    def addCourse(self,c):
        self.courseList.append(c)
    
    def removeCourse(self, c):
        self.courseList.remove(c)


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
    
    def __init__(self, name, startTime, endTime):
        self.courseName = name
        self.courseStartTime = startTime
        self.courseEndTime = endTime
