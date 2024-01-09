import os
from tools import util
from log import console

# Command id 0
def check_session()->str:
  return "loginctl show-session $(loginctl|grep $(whoami) |awk '{print $1}') -p Type"

# Command id 1
def samba_list(ip:str)->str:
  return f'smbclient -L {ip} -N'

# Command id 2
def fedora_crontab_status()->str:
  return f'systemctl status crond.service'

# Command id 3
def create_softlink(target:str, location:str)->str:
  return f'ln -s {target} {location}'

# Command id 4
def unlink_softlink(target_name:str)->str:
  return f'unlink {target_name}'

# Command id 5
def make_sudoer_permission(username:str, path:str)->str:
    directories = [f'{path}/*']
    for root, dirs, files in os.walk(path):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name) + '/*'
            directories.append(dir_path)

    folder_name = os.path.basename(path.rstrip('/'))
    sudoers_path = '/etc/sudoers.d/' + folder_name
    if os.path.exists(sudoers_path):  # If permission name is duplicated
        sudoers_path = sudoers_path + util.generate_random_4_digit()

    console.log(directories)

    last_index = len(directories) - 1
    command = ''
    for index, dir in enumerate(directories):
        p0 = f'{username} ALL=NOPASSWD: '
        p1 = f'{dir}'
        if index == last_index:
            command = command + f'echo {p0}{p1} >> {sudoers_path}'
        else:
            command = command + f'echo {p0}{p1} >> {sudoers_path} &&'

    command = command + '&&' + 'echo "==== Add permission completed ===="'
    command = command + '&&' + f'echo " - Permission file path is {sudoers_path}"'
    command = command + '&&' + 'echo " - Dont forget to add shebang and +x for the scripts"'
    command = command + '&&' + 'echo ""'

    return command

