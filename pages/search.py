import curses, subprocess, time
from curses.textpad import Textbox, rectangle

from core import app, common, settings
from panel import footer
from log import console
from tools import word, util
from pages import input



class Border:
  '''
  desc: Class that keep border variables for search app.
  '''

  # Vertical Border
  left = None
  middle = None
  right = None
  # Horizontal Border
  top = None
  bottom = None


  def __init__(self) -> None:
    self.left = 5
    self.middle = int(common.terminal_width/2)
    self.right = common.terminal_width - 1 - 5
    self.top = 3
    self.bottom = common.terminal_height - 1 - 2

  def draw(self, screen:curses.window) -> None:
    screen.attron(common.GREEN_AND_BLACK)
    rectangle(
      screen, 
      self.top + 2, self.left,
      self.bottom, self.middle
    )
    rectangle(
      screen, 
      self.top, self.left,
      self.bottom, self.middle
    )
    rectangle(
      screen, 
      self.top, self.middle + 1,
      self.bottom, self.right
    )
    screen.attroff(common.GREEN_AND_BLACK)

class DescPad:


  def __init__(self, nlines:int, ncols:int, row_origin:int, col_origin:int) -> None:
    self._pad = curses.newpad(nlines, ncols)
    self._origin = {'row': row_origin, 'col': col_origin}
    self._end = {'row': row_origin + nlines - 1, 'col': col_origin + ncols - 1}

    self._tag_window = curses.newwin(
      1, ncols, 
      self._origin['row'] + nlines - 1, self._origin['col']
    )


  def render(self, highlight_item_ided_command:str, style:int = curses.A_ITALIC) -> None:
    self._pad.clear()

    desc = util.get_command_desc_by_name(highlight_item_ided_command)
    
    if desc == None:
      self._pad.addstr(0,0,'None ...',style)
    else:
      self._pad.addstr(0,0,desc,style)

    self._pad.refresh(
      0,0,
      self._origin['row'], self._origin['col'],
      self._end['row'], self._end['col']
    )

  def render_tag(self, tag:str):
    self._tag_window.clear()
    if tag == 'Linux':
      self._tag_window.addstr(tag, curses.A_BOLD | curses.color_pair(12))
    elif tag == 'Fedora':
      self._tag_window.addstr(tag, curses.A_BOLD | curses.color_pair(28))
    elif tag == 'Ubuntu':
      self._tag_window.addstr(tag, curses.A_BOLD | curses.color_pair(2))
    self._tag_window.refresh()
  

class LiveProcessWindow():
  '''
  desc: window that show the output of subprocess in almost realtime.
  '''
  def __init__(self) -> None:
    self._window = curses.newwin(
      common.terminal_height-2, 
      common.terminal_width-1, 
      1, 1)

  def clear_log_content(self):
    # Remove existing content in live process log file.
    result_file = open(settings.LIVE_RESULT_LOG, "w")
    result_file.write("")
    result_file.close()

  def render_live(self, command):
    self.clear_log_content()

    f = open(settings.LIVE_RESULT_LOG, "w")
    process = subprocess.Popen(
      command, 
      stdout=f, 
      stderr=subprocess.STDOUT, 
      text=True, 
      shell=True
    )
    f.close()

    self._window.clear()
    self._window.addstr('Command on progress ...')
    self._window.refresh()

    #(v) Wait the process to finish
    process.wait()

    self._window.clear()
    self._window.refresh()

    scr = app.main_screen
    footer.update(
      scr, 
      '           Press "j", "k" for scrolling, and other keys for exit to search page.', 
      [
        [21, curses.color_pair(197) | curses.A_REVERSE],
        [26, curses.color_pair(197) | curses.A_REVERSE]
      ],
      curses.color_pair(34) | curses.A_REVERSE
    )

    footer.update_left_status(
      scr,
      f'  Terminal  ',
      common.BLACK_AND_BLUE | curses.A_BOLD
    )
    scr.refresh()

    # == Get max cols to be declared in pad create
    max_cols = 0
    with open(settings.LIVE_RESULT_LOG, 'r') as f:
      line = f.readline()
      if len(line) > max_cols:
        max_cols = len(line)
    # ==

    f = open(settings.LIVE_RESULT_LOG, "r")
    contents = f.readlines()
    f.close()

    contents_longstr = ''.join(contents)

    _pad = curses.newpad(len(contents)+2, max(2*common.terminal_width, 2*max_cols))
    _pad.addstr(contents_longstr)
    _pad.addstr(word.fill_space('Done !!', common.terminal_width-1, 4), curses.color_pair(3))

    num_lines, num_cols = _pad.getyx()
    num_lines_used_in_pad = num_lines + 1


    if num_lines_used_in_pad <= common.terminal_height-3:
      start_showing_line = 0
    else:
      start_showing_line = num_lines_used_in_pad - common.terminal_height-3 +2 +3

    _pad.refresh(
      start_showing_line, 0,
      0, 0,
      common.terminal_height-3, common.terminal_width-5
    )


    max_start_line = start_showing_line
    while True:
      key = self._window.getkey()

      if key == 'j':
        start_showing_line = start_showing_line + 1
        if start_showing_line > max_start_line: start_showing_line = max_start_line
        _pad.refresh(
          start_showing_line, 0,
          0, 0,
          common.terminal_height-3, common.terminal_width-5
        )
      elif key == 'k':
        start_showing_line = start_showing_line - 1
        if start_showing_line < 0: start_showing_line = 0
        _pad.refresh(
          start_showing_line, 0,
          0, 0,
          common.terminal_height-3, common.terminal_width-5
        )
      else:
        return


def update_footer(is_normal_mode:bool)->None:
  scr = app.main_screen

  if is_normal_mode:
    mode_status = 'Normal'
    footer.update(
      scr, 
      '         Press "i" for insert mode, "j,k" for navigation and "l" to enter.',
      [
        [19, curses.color_pair(197) | curses.A_REVERSE],
        [40, curses.color_pair(197) | curses.A_REVERSE],
        [42, curses.color_pair(197) | curses.A_REVERSE],
        [65, curses.color_pair(197) | curses.A_REVERSE],
      ],
      curses.color_pair(34) | curses.A_REVERSE
    )
  else:
    mode_status = 'Insert'
    footer.update(
      scr, 
      '         Press "ESC" for normal mode.',
      [
        [19, curses.color_pair(197) | curses.A_REVERSE],
        [20, curses.color_pair(197) | curses.A_REVERSE],
        [21, curses.color_pair(197) | curses.A_REVERSE],
      ],
      curses.color_pair(34) | curses.A_REVERSE
    )

  footer.update_left_status(
    scr,
    f'  {mode_status}  ',
    common.BLACK_AND_BLUE | curses.A_BOLD
  )

def get_menu_showing_range(
  highlight_item_id_id:int, min:int, max:int
)->[int]:
  # Scroll menu down
  if highlight_item_id_id > max:
    max = highlight_item_id_id
    min = min + 1
  # Scroll menu up
  if highlight_item_id_id < min:
    min = highlight_item_id_id
    max = max - 1

  return [min, max]

def fetch_command_data(menu_pad:curses.window)->[]:
  all_commands = []
  filtered_commands = []
  for i, e in enumerate(settings.COMMANDS):
    all_commands.append(e['name'])
    filtered_commands.append(e['name'])
    menu_pad.addstr(
      i, 0, 
      word.fill_space(e['name'], int(common.terminal_width/2) - 1, 5), 
      curses.A_ITALIC
    )

  return [all_commands, filtered_commands]


def render():
  scr = app.main_screen
  curses.curs_set(0)  # Hide the cursor

  border = Border()

  highlight_item_id = 0

  min_showing_index = 0
  max_showing_index = (border.bottom - 1) - (border.top + 3)

  main_pad = curses.newpad(
    len(settings.COMMANDS) + 10,
    int(common.terminal_width/2) - 1
  )

  desc_panel_size = [border.bottom - border.top - 1, border.right - border.middle - 4]
  desc_panel_location = [border.top + 1, border.middle + 3]
  desc_n_lines, desc_n_cols = desc_panel_size
  desc_row_location, desc_col_location = desc_panel_location
  desc_pad = DescPad(desc_n_lines, desc_n_cols, desc_row_location, desc_col_location)

  search_window = curses.newwin(1, border.middle-border.left-1, border.top+1, border.left+1)
  live_process_window = LiveProcessWindow()

  all_commands, filtered_commands = fetch_command_data(main_pad)

  key = 0
  insert_mode = False
  normal_mode = True
  search_text = ''

  while True:
    scr.clear()
    main_pad.clear()

    border.draw(scr)  # draw main border
    update_footer(normal_mode)  # update scr footer
    scr.refresh()
    
    # ==== Update filtered menu if there is search keyword
    if search_text == '':
      filtered_commands = all_commands
    else:
      include_words, exclude_words = word.extract_search_words(search_text)
      filtered_commands = word.filter_array_by_keywords(all_commands, include_words, exclude_words)

    if len(filtered_commands) < 1:
      main_pad.addstr(
        0, 0, 
        word.fill_space('None ... ', border.middle - 1, 5), 
        curses.A_DIM
      )
    else:
      for i, e in enumerate(filtered_commands):
        if i == highlight_item_id:
          main_pad.addstr(
            i, 0, 
            word.fill_space(e, border.middle - 1, 5), 
            curses.A_BOLD | common.BLACK_AND_WHITE
          )
        else:
          main_pad.addstr(
            i, 0, 
            word.fill_space(e, border.middle - 1, 5), 
            curses.A_DIM
          )
    # ====

    # ===== Update showing menu due to scrolling
    min_showing_index, max_showing_index = get_menu_showing_range(
      highlight_item_id, min_showing_index, max_showing_index)
    main_pad.refresh(
      min_showing_index,0,
      border.top + 3, border.left + 1,
      border.bottom - 1, border.middle - 1
    )
    # =====

    # === Render highlighted command description
    if len(filtered_commands) > 0:
      desc_pad.render(filtered_commands[highlight_item_id])
      # OS tag
      desc_pad.render_tag(util.get_command_tag_by_name(filtered_commands[highlight_item_id]))
    else:
      desc_pad.render("None")
    # ===

    # == Update search box
    search_text_position = int(common.terminal_width/4 - len(search_text)/2 - border.left + 1)
    search_window.addstr(0, search_text_position,search_text, curses.A_ITALIC)
    search_window.refresh()
    # ==

    # ======================= Handle Key Event =================================
    if insert_mode:
      key = scr.getch()
      char = chr(key)

      if key == 27:  # ESC
        normal_mode = True
        insert_mode = False
        curses.curs_set(0)
      elif key == 263: # Backspace
        search_text = search_text[:-1]
      else:
        search_text = search_text + char

    elif normal_mode:
      key = scr.getch()
      if key == 106: # j
        if highlight_item_id >= len(filtered_commands) - 1:
          highlight_item_id = len(filtered_commands) - 1
        else:
          highlight_item_id = highlight_item_id + 1
      elif key == 107: # k
        if highlight_item_id == 0:
          pass
        else:
          highlight_item_id = highlight_item_id - 1
      elif key == 105: #i
        normal_mode = False
        insert_mode = True
        curses.curs_set(1)

      elif key == 108: #l
        
        # === Check if command need any user inputs
        command_name = filtered_commands[highlight_item_id]
        questions = util.get_command_questions_by_name(command_name)
        params_for_command = []
        command = ''

        if len(questions) > 0:
          params_for_command = input.render(questions)
          if params_for_command is not None:
            command = util.get_command_func_by_name(command_name)(*params_for_command)
        else:
          command = util.get_command_func_by_name(command_name)()
        # ===

        # ==== Proceed command
        if params_for_command is not None:
          live_process_window.render_live(command)
        # ====
    # ==========================================================================
