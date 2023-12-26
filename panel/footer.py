import curses
from core import common
from tools import word, util




def update(window:curses.window, text:str, options=[], color_pair:int = common.BLACK_AND_WHITE):
  '''
  desc: Example of options
        options = [
          [7, curses.A_ITALIC | curses.color_pair(1)],
          [13: curses.A_ITALIC | curses.color_pair(2)]
        ]

        Key of option is number of column to be changed the style.
  '''

  num_line = common.terminal_height - 1

  window.addstr(
    num_line, 0,
    word.fill_space(text, common.terminal_width, 3),
    curses.A_ITALIC | color_pair
  )

  if len(options)>0:
    try:
      for option in options:
        num_col = option[0]
        style = option[1]
        window.chgat(num_line, num_col, 1, style)
    except:
      pass

  window.refresh()

def update_right_status(window:curses.window, text:str):
  window.addstr(
    common.terminal_height - 1,
    common.terminal_width - 1 - len(text) -2,
    text,
    curses.A_ITALIC | common.BLACK_AND_WHITE
  )

def update_left_status(window:curses.window, text:str, style:int = common.GREEN_AND_BLACK):
  window.addstr(
    common.terminal_height - 1,
    0,
    text,
    style
  )