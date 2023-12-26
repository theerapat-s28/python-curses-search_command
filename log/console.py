def log(value:any):
  text = str(value)
  with open('console.log', 'w') as file:
    file.write(text)