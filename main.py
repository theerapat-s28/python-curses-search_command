import curses, time
from curses import wrapper

from tools import word
from core import common, settings, app
from panel import footer, menu
from pages import loading, color, search, main as main_page
from log import console


def set_screen_size() -> None:
  '''
  Description: Raise exception if terminal screen size is less than settings.
  '''
  terminal_screen_width = curses.COLS
  terminal_screen_height = curses.LINES

  if terminal_screen_width < settings.MIN_TERMINAL_WIDTH:
    raise Exception(f'''Error: Terminal screen width less than {settings.MIN_TERMINAL_WIDTH} (Current width = {terminal_screen_width})''')
  if terminal_screen_height < settings.MIN_TERMINAL_HEIGHT:
    raise Exception(f"Error: Terminal screen height less than {settings.MIN_TERMINAL_HEIGHT} (Current width = {terminal_screen_height})")
  
  # If no error set to common
  common.terminal_width = terminal_screen_width
  common.terminal_height = terminal_screen_height

def set_app_color() -> None:
  '''
  Description: Create color pair and save in common.
  '''
  if curses.has_colors(): # If terminal has color
    if curses.can_change_color():
      curses.start_color()
      for i in range(1, curses.COLORS):
        curses.init_pair(i+1, 0, i)

  common.GREEN_AND_BLACK = curses.color_pair(36) | curses.A_REVERSE
  common.RED_AND_BLACK = curses.color_pair(197) | curses.A_REVERSE
  common.BLACK_AND_WHITE = curses.color_pair(8)
  common.YELLOW_AND_BLACK = curses.color_pair(227) | curses.A_REVERSE
  common.BLACK_AND_YELLOW = curses.color_pair(228)
  common.BLACK_AND_BLUE = curses.color_pair(70)


def initialize(stdscr:curses.window) -> None:
  '''
  Description: Do initial things like set size, color.
  '''
  app.main_screen = stdscr;
  set_screen_size()
  set_app_color()


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



def app_start() -> None:
  scr = app.main_screen

  while True:
    scr.addstr('s = Search Page\nm = Main Page\nc = Color Page')

    if app.current_page == settings.PAGE.MAIN:
      main_page.render()
    elif app.current_page == settings.PAGE.SEARCH:
      search.render()
    elif app.current_page == settings.PAGE.COLOR:
      color.render()
    elif app.current_page == None:
      pass

    key = scr.getkey()
    if key == 'm':
      app.current_page = settings.PAGE.MAIN
    elif key == 's':
      app.current_page = settings.PAGE.SEARCH
    elif key == 'c':
      app.current_page = settings.PAGE.COLOR


def main(stdscr:curses.window):
  initialize(stdscr)
  app_start()

if __name__ == "__main__":
  wrapper(main)