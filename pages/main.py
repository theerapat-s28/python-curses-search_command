import curses
from core import app, common, settings
from panel import menu, footer


def key_action(key:str) -> None:

  scr = app.main_screen

  #================================== On main page =============================
  if common.actived_page == 0:
    if key == 'h':
      footer.update(scr, f'{key} is not set in page {common.actived_page}')
    elif key == 'j':
      common.actived_menu = common.actived_menu + 1
      if common.actived_menu >= len(settings.MAIN_MENU): common.actived_menu = len(settings.MAIN_MENU) - 1
      menu.update_main_menu(scr, common.actived_menu)
      footer.update(scr, f'Actived page = {common.actived_page}, Actived menu = {common.actived_menu}, Last key = {key}')
    elif key == 'k':
      common.actived_menu = common.actived_menu - 1
      if common.actived_menu < 0: common.actived_menu = 0
      menu.update_main_menu(scr, common.actived_menu)
      footer.update(scr, f'Actived page = {common.actived_page}, Actived menu = {common.actived_menu}, Last key = {key}')
    elif key == 'l':
      footer.update(scr, f'{key} is not set in page {common.actived_page}')
    elif key == ' ':
      common.actived_page = common.actived_menu
      common.actived_menu = 0
      menu.update_main_menu(scr, common.actived_menu)
      footer.update(scr, f'Enter to Actived page {common.actived_page}')
    elif key == 'q':
      exit()
    elif key == None:
      pass
    else:
      footer.update(scr, f'{key} is not set in page {common.actived_page}')

    return  # If not return here, it will process below code.
  #=============================================================================

  #================================== Other page ===============================
  if common.actived_page != 0:
    if key == 'h':
      footer.update(scr, f'{key} is not set in page {common.actived_page}')
    elif key == 'j':
      common.actived_menu = common.actived_menu + 1
      if common.actived_menu >= len(settings.MAIN_MENU): common.actived_menu = len(settings.MAIN_MENU) - 1
      menu.update_main_menu(scr, common.actived_menu)
      footer.update(scr, f'Actived page = {common.actived_page}, Actived menu = {common.actived_menu}, Last key = {key}')
    elif key == 'k':
      common.actived_menu = common.actived_menu - 1
      if common.actived_menu < 0: common.actived_menu = 0
      menu.update_main_menu(scr, common.actived_menu)
      footer.update(scr, f'Actived page = {common.actived_page}, Actived menu = {common.actived_menu}, Last key = {key}')
    elif key == 'l':
      footer.update(scr, f'{key} is not set in page {common.actived_page}')
    elif key == ' ':
      footer.update(scr, f'Execute command [{common.actived_page}][{common.actived_menu}]')
    elif key == 'q':
      exit()
    elif key == 'KEY_BACKSPACE':
      common.actived_page = 0
      common.actived_menu = 0
      menu.update_main_menu(scr, common.actived_menu)
      footer.update(scr, f'Go back to Actived page = {common.actived_page}')
    elif key == None:
      pass
    else:
      footer.update(scr, f'{key} is not set in page {common.actived_page}')

    return
  #=============================================================================


def render():
  scr = app.main_screen
  
  while True:
    scr.clear()

    curses.curs_set(0)  # Hide the cursor
    footer.update(scr, 'Use <h j k l> for navigation, otherwise exit.')
    menu.update_main_menu(scr, common.actived_menu)

    scr.refresh()
    key = scr.getkey()
    key_action(key)
