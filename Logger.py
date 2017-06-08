'''
Author: Abhijit Annaldas
Github: http://github.com/avannaldas/PythonLogger
'''
import datetime

class Logger:
  '''
  Standard output printing helper which prefixes useful info with message.
  Can be used with long running operations to indicate progress/running time.
  All options can be configured through constructor and has sensible defaults.
  '''
  def __init__(self,
    startTime=datetime.datetime.now(),
    showDate=False,
    showTime=True,
    showTotalElapsed=False,
    showElapsedSinceLastLog=True,
    showTimeLoggerInitMessage=True,
    addLineBreaks=False,
    referenceId="NA"):

    self.startTime = startTime
    self.showDate = showDate
    self.showTime = showTime
    self.showTotalElapsed = showTotalElapsed
    self.showElapsedSinceLastLog = showElapsedSinceLastLog
    self.previousLogTime = startTime
    self.referenceId = referenceId
    self.addLineBreaks = addLineBreaks

    if(showTimeLoggerInitMessage):
      self.log("TimeLogger initialized")

  def getLogString(self, msg="", eventName=""):
    now = datetime.datetime.now()
    msgStr = ""
    if(self.referenceId != "NA"):
      msgStr = "[ReferenceId:" + self.referenceId + "]:"

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

    if(len(eventName)>0):
      msgStr = msgStr + '[Event:' + eventName + ']:'

    if(self.addLineBreaks):
      msgStr = msgStr + "\n" + msg
    else:
      msgStr = msgStr + msg

    return (msgStr)

  def log(self, msg="", eventName=""):
    print(self.getLogString(msg, eventName))
