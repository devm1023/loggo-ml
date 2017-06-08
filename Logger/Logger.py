'''
Author: Abhijit Annaldas
Github: http://github.com/avannaldas/PythonHelpers
'''
import datetime

class TimeLogger:
  '''
  Standard output printing helper which prefixes timestamp, elapsed time in seconds with every message. Can be used in long running operations as an indication of progress and time taken
  '''
  def __init__(self, startTime, showDate=True, showTime=True, showTotalElapsed=True, showElapsedSinceLastLog=True):
    self.startTime = startTime
    self.showDate = showDate
    self.showTime = showTime
    self.showTotalElapsed = showTotalElapsed
    self.showElapsedSinceLastLog = showElapsedSinceLastLog
    self.previousLogTime = startTime

  def log(self, msg = ""):
    msgStr = ""
    now = datetime.datetime.now()

    if(self.showDate == True and self.showTime == False):
      msgStr = msgStr + '[' + now.strftime("%d-%m-%Y") + ']:'
    elif(self.showDate == False and self.showTime == True):
      msgStr = msgStr + '[' + now.strftime("%H:%M:%S") + ']:'
    elif (self.showDate and self.showTime):
      msgStr = msgStr + '[' + now.strftime("%d-%m-%Y %H:%M:%S") + ']:'

    if(self.showTotalElapsed):
      msgStr = msgStr + '[Total Elapsed Seconds:' + str(int((now - self.startTime).total_seconds())) + ']:'

    if(self.showElapsedSinceLastLog):
      msgStr = msgStr + '[Elapsed seconds (diff):' + str(int((now - self.previousLogTime).total_seconds())) + ']:'
      self.previousLogTime = now

    print(msgStr + msg)
