from pymongo import MongoClient

uri = "mongodb://admin:admin1@ds249503.mlab.com:49503/c4e23-blog"

#1 Connect
client = MongoClient(uri)

#2 Get default database
db = client.get_default_database()

#3 Get collection
posts = db["posts"] #lazy loading
movies = db["movies"]

#4 Create data
new_post = {
  "title": "Hôm nay trời nắng",
  "content": "Tôi vẫn ở nhà code",
}

new_movie = {
  "title": "Batman begins",
  "rating": 8.0
}

#5 Insert data
# posts.insert_one(new_post)
# movies.insert_one(new_movie)

# 5 Read data
post_list = posts.find()
# p = post_list[1]
for p in post_list:
  print(p["title"])
  print(p["content"])
  print("&&&&&&&&&&&&&&&&&")

#6 Close connection
client.close()