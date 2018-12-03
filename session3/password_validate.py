pwd = input("Enter your password: ")

while True:
  print("Not OK")
  if (len(pwd) <= 8):
    print("Password length must be greater than 8")
  elif pwd.isalpha():
    print("Password must contain number")
  elif pwd.isupper() or pwd.islower() or pwd.isdigit():
    print("Password must contain both upper and lower characters")
  else:
    break
  pwd = input("Enter your password")
