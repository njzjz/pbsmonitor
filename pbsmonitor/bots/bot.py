'''Bot.'''
from abc import ABCMeta, abstractmethod
import threading


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
        threads = []
        for bot in self._bots:
            thread = threading.Thread(target=bot.sendmessage, args=(message,))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()

    def __len__(self):
        return len(self._bots)
