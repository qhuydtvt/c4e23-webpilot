favs = ["netflix", "redbull"]
print(*favs, sep=" | ")
new_item = input("Enter new thing: ")
favs.append(new_item)
print(*favs, sep=" | ")