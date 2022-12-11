import time, os
def view():
  print()
  for item in list:
   print(item)
  print()
list = []
while True:
  print("🤖 Smart List Manager🧾")
  statement = input('What item do you want to add, remove, or view? ')
  if statement == 'add':
    item = input('What item do you want to add? ')
    list.append(item)
    view()
  elif statement =='remove':
    item = input('What item do you want to remove? ')
    if item in list:
      list.remove(item)
      view()
    else:
      print('Item not found')
  elif statement == 'view':
    view()
  else:
    print('Invalid input')
  time.sleep(1)
  os.system('clear')
  