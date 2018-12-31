from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
# the scope of the access
# in this case it is read only
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'

def main():
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))



# class schedule:
#     eventList = []
#     def __init__(self,events):
#         self.eventList = events
#     def addEvent(self,e):
#         self.eventList.append(e)
#     def removeEvent(self,name):
#         for event in self.eventList:
#             if (event.getName() == name):
#                 self.eventList.remove(event)
#     def toString(self):
#         s = "Schedule consists of "
#         for event in self.eventList:
#             if event != None:
#                 s = s + event.getName() + " from " + str(event.getTime()[0]) + " to " + str(event.getTime()[1])
#         return s

class event:

    def __init__(self, name, startTime, endTime):
        self.name = name
        self.startTime = startTime
        self.endTime = endTime
    def getName(self):
        return self.name
    @staticmethod
    #returns a dict of date of event and start and end times
    def getDateTime(event):
        start = event['start'].get('dateTime').split("T")[1].split("-")[0].split(':')
        end = event['end'].get('dateTime').split("T")[1].split("-")[0].split(':')
        date = event['start'].get('dateTime').split("T")[0].split("-")
        
        startDict = {'hour': int(start[0]), 'minute': int(start[1])}
        endDict = {'hour': int(end[0]), 'minute': int(end[1])}
        dateDict = {'year': int(date[0]), 'month': int(date[1]), 'day': int(date[2])}

        myDict = {'date': dateDict, 'startTime': startDict, 'endTime': endDict}
        
