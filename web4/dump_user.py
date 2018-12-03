import mlab
from models.user import User

mlab.connect()
# User.drop_collection()

# User(username="admin", password="321").save()
# User(username="huynq", password="huynq").save()
# User(username="quan", password="quan").save()
# for user in User.objects():
#   print(user.username, user.password)