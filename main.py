import curses, time, sys
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