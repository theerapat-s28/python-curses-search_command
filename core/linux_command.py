# Command id 0
def check_session()->str:
  return "loginctl show-session $(loginctl|grep $(whoami) |awk '{print $1}') -p Type"

# Command id 1
def samba_list(ip:str)->str:
  return f'smbclient -L {ip} -N'

# Command id 2
def fedora_crontab_status():
  return f'systemctl status crond.service'