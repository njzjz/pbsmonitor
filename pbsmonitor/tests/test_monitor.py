from threading import Timer

from pbsmonitor import Monitor, Bots
from pbsmonitor.bots.qqbot import qqbot


class Test_monitor:

    def test_monitor(self, httpserver):
        httpserver.serve_content(
            '''{"data":null,"retcode":1,"status":"async"}''')

        bots = Bots()
        bots.append(qqbot(cqroot=httpserver.url, group_id=123456))
        Monitor(bots=bots, command='uname -a', timeinterval=1)._sendstate()
