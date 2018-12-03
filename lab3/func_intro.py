def add(a, b):
  r = a + b
  return r

# call function
# s = add(7, 8)
# print(s)

def eval(a, b, op):
  if op == "+":
    r = a + b
  elif op == "-":
    r = a - b
  elif op == "*":
    r = a * b
  elif op == "/":
    r = a / b
  else:
    print("Unsupported operation!!")
  return r

# s = eval(9, 10, "*")
# print(s)