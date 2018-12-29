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
        if self.mySchedule != None:
            return(self.myName + " " + str(self.mySchedule.toString()))
        else:
            return(self.myName)
    def getSchedule(self):
        return self.mySchedule
    def getName(self):
        return self.myName


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
