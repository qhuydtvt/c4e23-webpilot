a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

delta = b*b - 4*a*c
a_2 = a * 2
if delta < 0:
  print("No solutions")
elif delta == 0: # !=
  x = -b / a_2
  print("1 solution: ", x)
else:
  delta_sqrt = delta**0.5
  x1 = (-b + delta_sqrt) / a_2
  x2 = (-b - delta_sqrt) / a_2
  print("2 solutions: ", x1, x2)