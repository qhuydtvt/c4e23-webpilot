teen_dict = {
  "eny": "Em nguoi yeu",
  "any": "Anh nguoi yeu",
  "ngta": "Nguoi ta",
}

while True:
  code = input("Enter code: ")
  if code in teen_dict:
    print(teen_dict[code])
  else:
    print("Not found")
    action = input("Contribute (Y/N)? ").upper()
    if action == "Y" or action == "YES":
      trans = input("Your translation: ")
      teen_dict[code] = trans
