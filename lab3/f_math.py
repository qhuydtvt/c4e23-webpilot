# 1. Generate quiz
from random import randint, choice
from func_intro import eval

def generate_quiz():
  x = randint(0, 10)
  y = randint(0, 10)
  error = randint(-2, 2)
  o = choice(["+", "-", "*", "/"])
  r = eval(x, y, o) + error

  return x, y, o, r

a, b, op, r = generate_quiz()

print(a, op, b, "=", r) # string formatting

# User input & result
user_answer = input("Your guess (Y/N)").upper()
if user_answer == "Y":
  if error == 0:
    print("Yay")
  else:
    print("Nay")
else:
  if error == 0:
    print("Nay")
  else:
    print("Yay")
