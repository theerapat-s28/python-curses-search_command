import curses
from core import app, settings
from log import console
from typing import List, Union


def _my_raw_input(window:curses.window, r, c, prompt_string):
  nlines, ncols = window.getmaxyx()

  curses.curs_set(1)
  window.clear()
  curses.echo()
  window.box()
  window.addstr(r, c, f'{prompt_string} :')
  window.addstr(nlines-1, c, 'Press enter to submit the answer.')
  window.refresh() #      v reading input at next line
  input = window.getstr(r + 1, c, 3*ncols)
  curses.curs_set(0)
  return input


def render(questions:[str]) -> Union[List[str],None]:
  '''
  desc: Render user input gui and return array or the answer.
  '''
  if len(questions) <= 0: return []

  scr = app.main_screen

  scr_h = int((curses.LINES-1)/2)
  scr_w = int((curses.COLS-1)/2)
  window_nlines = settings.MIN_TERMINAL_HEIGHT-5
  window_ncols = settings.MIN_TERMINAL_WIDTH-5
  window_oline = 3
  window_ocols = scr_w - int(window_ncols/2)
  main_window = curses.newwin(window_nlines,window_ncols,window_oline,window_ocols)

  answers = []
  q_index = 0

  while True:
    scr.clear()
    scr.refresh()
    main_window.clear()

    if q_index < len(questions):
      answers.append(_my_raw_input(main_window,3,3,questions[q_index]))
      q_index = q_index+1
    else:
      main_window.clear()
      main_window.addstr(3,3,'We got all input.')
      main_window.addstr(4,3,'Press "e" to proceed command or')
      main_window.addstr(5,3,'Press "q" to go back to previous.')
      main_window.refresh()

      key = scr.getkey()
      if key == 'q':
        return None
      elif key == 'e':
        return answers
      else:
        pass
