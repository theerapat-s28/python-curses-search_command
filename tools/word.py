import random


def truncate_string(input_string, max_chars):
  '''
  Description: Replace exceed string char with ...
  '''
  if len(input_string) <= max_chars:
    return input_string
  else:
    return input_string[:max_chars - 3] + '...'

def fill_space(str:str, width:int, indent:int) -> str:
  if len(str)+indent > width:
    str = truncate_string(str, width-indent-4)
  num_fill_space = width - indent - len(str) - 1
  for i in range(indent):
    str = " " + str
  for i in range(num_fill_space):
    str = str + " "
  return str

def filter_by_keyword(data, keywords, case_sensitive:bool = False):
    if case_sensitive:
      return [item for item in data if all(keyword in item for keyword in keywords)]
    else:
      return [item for item in data if all(keyword.lower() in item.lower() for keyword in keywords)]


def get_random_emoji():
    emojis = ['😀', '🌍', '🎉', '🐱', '🌺', '🍕', '🎸', '🚀', '🌈', '📚']
    random_emoji = random.choice(emojis)
    return random_emoji