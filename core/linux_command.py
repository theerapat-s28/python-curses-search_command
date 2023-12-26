# Command id 0
def echo(text:str)->str:
  return f'echo "{text}"'

# Command id 1
def echo2(text:str, text2:str)->str:
  return f'echo {text} && echo {text2}'