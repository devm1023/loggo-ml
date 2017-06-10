"""
Author: Abhijit Annaldas
GitHub: http://github.com/avannaldas/PythonLogger
"""

import datetime

class Logger:
  """
  Standard output printing helper which prefixes useful info with message.
  Can be used with long running operations to indicate progress/running time.
  All options can be configured through constructor and has sensible defaults.
  """

  def __init__(self,
    startTime=datetime.datetime.now(),
    showDate=False,
    showTime=True,
    showTotalElapsed=False,
    showElapsedSinceLastLog=True,
    showLoggerInitMessage=True,
    addLineBreaks=False,
    returnLogStringInstead=False,
    referenceId="NA"):

    self.startTime = startTime
    self.showDate = showDate
    self.showTime = showTime
    self.showTotalElapsed = showTotalElapsed
    self.showElapsedSinceLastLog = showElapsedSinceLastLog
    self.previousLogTime = startTime
    self.referenceId = referenceId
    self.addLineBreaks = addLineBreaks
    self.returnLogStringInstead = returnLogStringInstead
    self.eventsDict = { }

    if(showLoggerInitMessage):
      print(self.getLogString("Logger initialized"))


  def getLogString(self, msg="", eventName="", elapsed=None):
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

    if(elapsed is None and self.showElapsedSinceLastLog):
      msgStr = msgStr + '[Elapsed Seconds (diff):' + str(int((now - self.previousLogTime).total_seconds())) + ']:'
    elif(elapsed is not None):
      msgStr = msgStr + '[Elapsed Seconds:' + elapsed + ']:'
    self.previousLogTime = now

    if(eventName is not None and len(eventName)>0):
      msgStr = msgStr + '[Event:' + eventName + ']:'

    if(self.addLineBreaks):
      msgStr = msgStr + "\n"

    return (msgStr + msg)

  def log(self, msg="", eventName="", elapsed=None):
    if(self.returnLogStringInstead):
      return self.getLogString(msg, eventName, elapsed)
    print(self.getLogString(msg, eventName, elapsed))

  def logStartEvent(self, name):
    self.eventsDict[name] = datetime.datetime.now()
    return self.log("Event started.", name)

  def logEndEvent(self, name):
    now = datetime.datetime.now()
    if (name in self.eventsDict):
      startEvent = self.eventsDict[name]
      del self.eventsDict[name]
      return self.log("Event complete.", name, str(int((now - startEvent).total_seconds())))
    else:
      return self.log("Event complete, logStartEvent() not called or logEndEvent() already called.", name)
