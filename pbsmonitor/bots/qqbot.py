'''CoolQ bot.'''
from cqhttp import CQHttp

from . import Bot


class qqbot(Bot):
    """CoolQ Bot."""

    def __init__(self, cqroot, group_id):
        self._cqbot = CQHttp(api_root=cqroot)
        self.group_id = group_id

    def sendmessage(self, message):
        self._cqbot.send_group_msg(group_id=self.group_id, message=message)
