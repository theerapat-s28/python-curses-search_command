from pathlib import Path
from enum import Enum

from core import linux_command, common

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

MIN_TERMINAL_WIDTH = 75
MIN_TERMINAL_HEIGHT = 15

MAIN_MENU = ['Main', 'Menu 2', 'Menu 3', 'Menu 4']

LIVE_RESULT_LOG = "command_result.log"

FPS = 30

class PAGE(Enum):
  MAIN = 0
  SEARCH = 1
  LOADING = 2
  COLOR = 3

MAX_COMMAND_DESC_LINES = 10000

COMMANDS = [
  {
    'id': 0,
    'name': 'Command 0',
    'desc': 'This is description of command 0, In your specific case, where' +
            ' you want to return the index, you can modify the code as needed.' +
            'If the item is not found, you can return a specific value or ' +
            'handle it in a way that fits your requirements.',
    'func': linux_command.echo,
    'questions': ['Text to echo is']
  },
  {
    'id': 1,
    'name': 'Command 1',
    'desc': 'echo number 2',
    'func': linux_command.echo2,
    'questions': ['Text =', 'Text2 =']
  },
  {
    'id': 2,
    'name': 'Command 2',
    'desc': 'Description of command 2',
    'questions': []
  },
  {
    'id': 3,
    'name': 'Command 3',
    'desc': 'Description of command 3',
    'questions': []
  },
  {
    'id': 4,
    'name': 'Command 4',
    'desc': 'Description of command 4',
    'questions': []
  },
    {
    'id': 5,
    'name': 'Command 5',
    'desc': 'Description of command 5',
    'questions': []
  },
  {
    'id': 6,
    'name': 'Command 6',
    'desc': 'Description of command 6',
    'questions': []
  },
  {
    'id': 7,
    'name': 'Command 7',
    'desc': 'Description of command 7',
    'questions': []
  },
  {
    'id': 8,
    'name': 'Command 8',
    'desc': 'Description of command 8',
    'questions': []
  }
  ,
  {
    'id': 9,
    'name': 'Command 9',
    'desc': 'Description of command 9',
    'questions': []
  },
  {
    'id': 10,
    'name': 'Command 10',
    'desc': 'Description of command 10',
    'questions': []
  }
]


def command0():
  pass