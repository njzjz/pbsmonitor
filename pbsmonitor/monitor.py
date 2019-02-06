"""JobMonitor."""
import os
import subprocess as sp
import time
from threading import Timer


class Monitor:
    def __init__(self, bots, command, keywords=None,
                 title=None, timeinterval=300):
        self._tip = "PBSMonitor"
        if bots:
            self.bots = bots
        else:
            raise TypeError("No bot in bots.")
        self.command = command
        self.keywords = keywords if keywords else ['']
        self.timeinterval = timeinterval
        self.title = title
        self._pause = False

    @property
    def _jobstate(self):
        states = sp.check_output(
            self.command.split()).decode('utf-8').split("\n")
        states = [' '.join(line.split()) for line in states if any(
            [keyword in line for keyword in self.keywords])]
        return states

    def _sendstate(self):
        localtime = time.asctime(time.localtime(time.time()))
        messages = [localtime, self._tip]
        if self.title:
            messages.append(self.title)
        messages.extend(self._jobstate)
        self.bots.sendmessage('\n'.join(messages))

    def loopmonitor(self):
        while not os.path.exists("pause") or not self._pause:
            timer = Timer(self.timeinterval, self._sendstate)
            timer.start()
            timer.join()
        print("Exit per signal.")

    def pause(self):
        self._pause = True
