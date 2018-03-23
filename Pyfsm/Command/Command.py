from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.contrib.completers import WordCompleter
from pygments.lexers.python import Python3Lexer

from pygments.style import Style
from pygments.token import Token
from pygments.styles.monokai import MonokaiStyle


class CommandStyle(Style):
    styles = {}
    styles.update(MonokaiStyle.styles)


class Command:
    """docstring for Command."""

    def __init__(self):
        super(Command, self).__init__()
        self._Command = None
        self._Completer = WordCompleter(['Machine'])
        self.commandLine()

    def getCommand(self):
        return self._Command

    def commandLine(self):
        history = InMemoryHistory()
        while True:
            self._Command = prompt(
                "> ",
                lexer=Python3Lexer,
                completer=self._Completer,
                style=CommandStyle,
                history=history)
            print('You entered:', self._Command)
        print("Goodbye~")
