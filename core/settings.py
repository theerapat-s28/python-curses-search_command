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
    'name': 'Fedora - Check whether Wayland or X11 is being used',
    'desc': "loginctl show-session $(loginctl|grep $(whoami) |awk '{print $1}') -p Type",
    'func': linux_command.check_session,
    'questions': [],
    'os': 'Fedora'
  },
  {
    'id': 1,
    'name': 'List samba shared folder',
    'desc': 'smbclient -L ${ip} -N',
    'func': linux_command.samba_list,
    'questions': ['Samba ip server (Ex. 192.168.1.20 or samba.lan) '],
    'os': 'Linux'
  },
  {
    'id': 2,
    'name': 'Echo world',
    'desc': 'echo ${text} && echo ${text1}',
    'func': linux_command.echo,
    'questions': ['text 1 ', 'text 2 '],
    'os': 'Linux'
  },
  {
    'id': 3,
    'name': 'Command 3',
    'desc': 'Description of command 3',
    'questions': [],
    'os': 'Ubuntu'
  },
  {
    'id': 4,
    'name': 'Command 4',
    'desc': 'Description of command 4',
    'questions': [],
    'os': 'Linux'
  },
    {
    'id': 5,
    'name': 'Command 5',
    'desc': 'Description of command 5',
    'questions': [],
    'os': 'Linux'
  },
  {
    'id': 6,
    'name': 'Command 6',
    'desc': 'Description of command 6',
    'questions': [],
    'os': 'Linux'
  },
  {
    'id': 7,
    'name': 'Command 7',
    'desc': 'Description of command 7',
    'questions': [],
    'os': 'Linux'
  },
  {
    'id': 8,
    'name': 'Command 8',
    'desc': 'Description of command 8',
    'questions': [],
    'os': 'Linux'
  }
  ,
  {
    'id': 9,
    'name': 'Command 9',
    'desc': 'Description of command 9',
    'questions': [],
    'os': 'Linux'
  },
  {
    'id': 10,
    'name': 'Command 10',
    'desc': 'Description of command 10',
    'questions': [],
    'os': 'Linux'
  }
]