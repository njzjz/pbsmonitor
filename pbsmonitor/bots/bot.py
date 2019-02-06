'''Bot.'''
from abc import ABCMeta, abstractmethod
import thread


class Bot(metaclass=ABCMeta):
    """A bot class."""

    @abstractmethod
    def sendmessage(self, message):
        return


class Bots:
    
    def __init__(self, bots=None):
        self._bots = bots if bots else []

    def append(self, bot):
        if isinstance(bot, Bot):
            self._bots.append(bot)
        else:
            raise TypeError('Should be a Bot!')

    def sendmessage(self, message):
        for bot in self._bots:
            thread.start_new_thread(bot.sendmessage, message)
    
    def __len__(self):
        return len(self._bots)
