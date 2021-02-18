#todo-list

todo_list=[]

def menu():
  mode=input('Choose a mode by entering the numbers: 1:Add Task 2:View Task 3:Exit :')
  return mode

def add_task():
  while True:
    new_task=int(input('Type in the task to add to list or enter \'return\'to go back :\n')).strip().lower
    if new_task=='return':
      break
    else:
      todo_list.append(new_task)

def view_task():
  for task in todo_list:
    print('-{}'.format(task))

while True:
  option=menu()

  if option=='1':
    add_task() 
  elif option=='2':
    print('Tasks:')
    view_task() 
  else:
    print('Please enter 1,2 or 3') 

