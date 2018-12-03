from mongoengine import *

class User(Document):
  meta = {"strict": False}
  username = StringField()
  password = StringField()

# Test
if __name__ == "__main__":
  from ..mlab import connect
  connect()
  print("User ------------")