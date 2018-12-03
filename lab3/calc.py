a = int(input("a = "))
op = input("Operation (+, -, *, /): ")
b = int(input("b = "))

if op == "+":
  r = a + b
elif op == "-":
  r = a - b
elif op == "*":
  r = b * b
elif op == "/":
  r = a / b
else:
  print("Unsupported operation!!")

print(r)