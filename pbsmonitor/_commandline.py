import argparse

from . import Monitor
from .bots import Bots
from .bots.qqbot import qqbot


def _commandline():
    parser = argparse.ArgumentParser(description='PBSMonitor')
    parser.add_argument(
        '-c', '--command', help='Command for monitoring, e.g. qstat, bjobs',
        required=True)
    parser.add_argument('-k', '--keywords',
                        help='Keywords for monitoring, e.g. jzzeng',
                        nargs='*', required=True)
    parser.add_argument('--title', help='Title, e.g. GPU1')
    parser.add_argument('-t', '--time', help='Time interval', default=300, type=int)

    # QQ
    parser.add_argument(
        '-r', '--cqroot', help='CoolQ HTTP Server Url, e.g. 192.168.1.1:6000')
    parser.add_argument('-g', '--groupid', help='QQ Group ID, e.g. 123456789', type=int)

    args = parser.parse_args()

    bots = Bots()
    if args.cqroot:
        bots.append(qqbot(cqroot=args.cqroot, group_id=args.groupid))
    Monitor(bots=bots, command=args.command, keywords=args.keywords,
            title=args.title, timeinterval=args.time).loopmonitor()
