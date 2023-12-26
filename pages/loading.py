import time
from core import app, settings

def render():
  '''
  Description: Loop for user interaction.
  '''
  scr = app.main_screen

  # === If no delay set to True, then you might need this. Otherwise the screen
  #       shall blinking while refresh the screen
  scr.nodelay(True)
  REFRESH_RATE = 50  # Reduce this too much might cause screen blinking
  loop = 0
  fps = settings.FPS
  frame_delay = 1.0 / fps
  # ===

  while True:
    loop = loop + 1;

    try:
      key = scr.getkey()
      last_key = key
    except:
      key = None

    # Provide some animation here
    if loop == REFRESH_RATE:
      loop = 0

    time.sleep(frame_delay)