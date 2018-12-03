p_list = [
  {
    'name': 'H.Duc',
    'age': 23,
    'mul': 2,
    'city': 'Hai Phong',
  },
  {
    'name': 'Quan',
    'age': 24,
    'mul': 3,
    'city': 'Hanoi'
  }
]

x = sum([p['age'] * p['mul'] for p in p_list])
print(x)

# JSON

# print(p_list)
for p in p_list:
  print(p['age'])
  print("-------------")
# for i in [0, 1, 2, "Hihi", 4]:
#   print(i)

# for k in person.keys(): # tuple ~ list
#   print(k, person[k])

# for v in person.values():
#   print(v)

# for k, v in person.items():
#   print(k, v)