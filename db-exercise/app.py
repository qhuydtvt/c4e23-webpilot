import mlab
from todo import Todo

mlab.connect()

loop = True
while loop:
  print('''1. New todo
2. View ALL Todos
3. Mark a Todo COMPLETED
4. Delete a Todo
5. Exit''')
  cmd = input("Enter your command? ").upper()
  if cmd == "1":
    name = input("Name: ")
    description = input("Description: ")
    new_todo = Todo(name=name, description=description)
    new_todo.save()
  elif cmd == "2":
    print("= " * 20)
    if Todo.objects().count() == 0:
      print("EMPTY")
    else:
      todo_list = Todo.objects()
      todo_no = 1
      for todo in todo_list:
        print(todo_no, todo, sep=". ")
        todo_no += 1
        print()
    print("= " * 20)
  elif cmd == "3":
    i = int(input("Which one? ")) - 1
    todo_list = Todo.objects()
    todo_list[i].update(set__completed=True)
    print("Updated")
  elif cmd == "4":
    i = int(input("Which one? ")) - 1
    todo_list = Todo.objects()
    todo_list[i].delete()
    print("Deleted")
  elif cmd == "5":
    loop = False
  
  input("Press Enter to continue ...")