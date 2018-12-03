# item1 = "Phở xào"
# item2 = "Ghẹ"
# item3 = "Sò huyết"
# item4 = "Cháo"
# item5 = "Cơm rang"

# items = [] # Empty list
# print(items)
# print(type(items))

# items = ["Ghẹ"]
# print(items)

# x = 5
# print(x)
# x = 7

items = ["Ghẹ", "Sò huyết", "Cháo"]

print(items)
i = int(input("Index: "))
new_value = input("New value: ")
items[i] = new_value
print(items)

# print(items)
# items.pop(1)
# print(items)

print(items)
items.remove("Sò huyết")
print(items)
