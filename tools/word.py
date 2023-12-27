import random
import re


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

def filter_array_by_keywords(data:[str], include_keywords:[str], exclude_keywords:[str]):
    return [item for item in data
            if all(keyword.lower() in item.lower() for keyword in include_keywords)
            and all(keyword.lower() not in item.lower() for keyword in exclude_keywords)]

def extract_search_words(input_string):
    '''
    desc: Extract include and exclude words from a string using * symbol.
          Ex.
            'cron install *status fedora'
            include_words -> ['cron', 'install', 'fedora']
            exclude_words -> ['status']
    '''
    words = re.findall(r'\b\w+\b|\*\w+', input_string)
    all_words = [word[1:] if word.startswith('*') else word for word in words]
    exclude_words = [word[1:] for word in words if word.startswith('*')]
    include_words = [element for element in all_words if element not in exclude_words]

    return include_words, exclude_words


def get_random_emoji():
    emojis = ['😀', '🌍', '🎉', '🐱', '🌺', '🍕', '🎸', '🚀', '🌈', '📚']
    random_emoji = random.choice(emojis)
    return random_emoji