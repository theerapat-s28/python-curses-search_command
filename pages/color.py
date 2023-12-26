import curses
from core import app

def render():
  scr = app.main_screen
  curses.curs_set(0)  # Hide the cursor
  
  scr.clear()
  if curses.has_colors(): # If terminal has color
    if curses.can_change_color():
      curses.start_color()
      # curses.use_default_colors()
      for i in range(0, curses.COLORS):
        curses.init_pair(i+1, 0, i)
      
      curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        
      try:
        for i in range(0, 256):
          scr.addstr(f' {i}', curses.color_pair(i) | curses.A_BOLD)
        scr.addstr('\n')
        for i in range(0, 256):
          scr.addstr(f' {i}', curses.color_pair(i) | curses.A_BOLD | curses.A_REVERSE)
      except curses.ERR:
        pass

      # Manually set
      scr.addstr('\n\n')
      scr.addstr(f'Choose {1}\n', curses.color_pair(1) | curses.A_BOLD)
      scr.addstr(f'Choose {36}\n', curses.color_pair(36) | curses.A_BOLD | curses.A_REVERSE)

  scr.refresh()
  scr.getkey()
  return