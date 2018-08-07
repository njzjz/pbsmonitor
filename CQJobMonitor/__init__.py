import os
import subprocess as sp
from cqhttp import CQHttp
import time
from threading import Timer

class CQJobMonitor():
    def __init__(self,command="qstat",cqroot='http://219.228.63.56:5700/',group_id=312676525,keywords=['jzzeng','lqcao','jxiao'],timeinterval=300):
        self.tip="JobMonitor"
        print(self.tip)
        self.command=command
        self.group_id=group_id
        self.keywords=keywords
        self.bot = CQHttp(api_root=cqroot)
        self.timeinterval=timeinterval

    def jobstate(self):
        states=sp.check_output(self.command.split()).decode('utf-8').split("\n")
        states=[' '.join(line.split()) for line in states if any([keyword in line for keyword in self.keywords])]
        return states

    def sendstate(self):
        localtime = time.asctime(time.localtime(time.time()))
        message=localtime+"\n"+self.tip+"\n"
        message+="\n".join(self.jobstate())
        self.bot.send_group_msg(group_id=self.group_id,message=message)

    def loopmonitor(self):
        while not os.path.exists("pause"):
            timer=Timer(self.timeinterval,self.sendstate)
            timer.start()
            timer.join()

if __name__='__main__':
    CQJobMonitor().loopmonitor()
