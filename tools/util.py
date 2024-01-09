from core import settings
import random, string

def get_command_desc_by_name(target_name:str):
  for e in settings.COMMANDS:
      if e['name'] == target_name:
          return e['desc']
  return None  # Return None if the name is not found

def get_command_tag_by_name(target_name:str):
  for e in settings.COMMANDS:
      if e['name'] == target_name:
          return e['os']
  return None  # Return None if the name is not found

def get_command_questions_by_name(target_name:str):
  for e in settings.COMMANDS:
      if e['name'] == target_name:
          return e['questions']
  raise Exception('Error! Questions not found.')

def get_command_func_by_name(target_name:str):
  for e in settings.COMMANDS:
      if e['name'] == target_name:
          return e['func']
  raise Exception('Error! Command func not found.')


def get_key_by_keyword(obj, keyword):
    '''
    desc: Example of obj
          obj = {
            75: ('blue', 'sky'),
            10: ('monkey'),
            8: ('dog', 'cat')
          }
          If give any keyword contains in tuple it will return key number like
          get_key_by_keyword(obj, 'cat') -> 8
    '''
    for key, values in obj.items():
        if keyword in values:
            return key
    return None  # Return None if the keyword is not found in any values


def generate_random_4_digit():
    # Generate a random 4-digit string
    random_digits = ''.join(random.choices(string.digits, k=4))
    return random_digits
