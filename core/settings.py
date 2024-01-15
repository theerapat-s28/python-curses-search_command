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
    'name': 'Fedora - Check crontab status',
    'desc': 'systemctl status crond.service',
    'func': linux_command.fedora_crontab_status,
    'questions': [],
    'os': 'Fedora'
  },
  {
    'id': 3,
    'name': 'Linux - create softlink',
    'desc': 'ln -s ${target} ${location}',
    'func': linux_command.create_softlink,
    'questions': [
      'Target directory (ex. /home/user/.config/nvim',
      'Location of softlink(shortcut)'
    ],
    'os': 'Linux'
  },
  {
    'id': 4,
    'name': 'Linux - remove softlink',
    'desc': 'unlink ${target_link}',
    'func': linux_command.unlink_softlink,
    'questions': ['Softlink location (ex. /home/user/.config/nvim'],
    'os': 'Linux'
  },
  {
    'id': 5,
    'name': 'Linux - make folder sudoers permission for all scripts inside',
    'desc': 'This will make all scripts inside folder and all sub folder to have '
            + 'sudo permission (execute "sudo" command without asking password)\n'
            + 'Command Steps: \n'
            + '1. Check if there is duplicate name of permission in /etc/sudoers.d/${dir}\n'
            + '2. Create permisssion /etc/sudoers.d/${dir}\n'
            + '3. List all dir and sub dirs and write permission to above file\n',
    'func': linux_command.make_sudoer_permission,
    'questions': ['Username', 'Directory (ex. /home/user/02-scripts'],
    'os': 'Linux'
  },
  {
    'id': 6,
    'name': 'Fedora - Show dnf history',
    'desc': 'List history of dnf command with id. \n  dnf history',
    'func': linux_command.dnf_history_list,
    'questions': [],
    'os': 'Fedora'
  },
  {
    'id': 7,
    'name': 'Fedora - Roll back dnf commands',
    'desc': 'Rollback dnf command to specific id. \n'
            + '  14 | install wget \n'
            + '  13 | install unzip \n'
            + '  12 | install vim-X11\n\n'
            + 'With command `dnf history rollback 12` This action uninstalls '
            + 'the wget and unzip packages but leaves the vim-X11 package installed.',
    'func': linux_command.dnf_rollback,
    'questions': ['Rollback id'],
    'os': 'Fedora'
  },{
    'id': 8,
    'name': 'Fedora - Undo dnf commands',
    'desc': 'Undo dnf command to specific id. \n'
            + '  14 | install wget \n'
            + '  13 | install unzip \n'
            + '  12 | install vim-X11\n\n'
            + 'With command `dnf history undo 12` This action uninstalls '
            + '`vim-X11` package only.',
    'func': linux_command.dnf_rollback,
    'questions': ['Rollback id'],
    'os': 'Fedora'
  },
]
