import curses
from curses.textpad import Textbox, rectangle

from tools import word
from core import common, settings
from log import console


def update_menu_panel(window:curses.window, menus:[str], active_menu:int):
  window.clear()
  # window.border()
  
  menu_left_offset = 5
  height, width = window.getmaxyx()

  for i, e in enumerate(menus):
    if i == active_menu:
      window.addstr(
        i, 0,
        word.fill_space(e, width, menu_left_offset),
        curses.A_ITALIC | common.BLACK_AND_WHITE
      )
    else:
      window.addstr(i, menu_left_offset, e)

  window.refresh()


def update_main_menu(main_screen:curses.window ,active_menu:int = 0):

  start_row = 3
  start_col = 5
  main_window_padding = 5

  # === Draw border in background
  main_screen.attron(common.GREEN_AND_BLACK)
  rectangle(
    main_screen,
    start_row - 1,
    start_col - 1, 
    common.terminal_height - 2*start_row + 3, 
    common.terminal_width - 2*main_window_padding + 5)
  main_screen.attroff(common.GREEN_AND_BLACK)
  main_screen.refresh()
  # ===

  MAIN_WINDOW_PROP = {
    'WIDTH': common.terminal_width - 2*main_window_padding,
    'HEIGHT': common.terminal_height - 2*start_row,
    'START_ROW': start_row,
    'START_COL': start_col,
  }
  main_window_args = [
    MAIN_WINDOW_PROP['HEIGHT'],
    MAIN_WINDOW_PROP['WIDTH'],
    MAIN_WINDOW_PROP['START_ROW'],
    MAIN_WINDOW_PROP['START_COL']
  ]
  main_menu_window = curses.newwin(*main_window_args)
  update_menu_panel(main_menu_window, settings.MAIN_MENU, active_menu)
