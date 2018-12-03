from mongoengine import Document, StringField, BooleanField

class User(Document):
  username = StringField()
  password = StringField()
  email_verified = BooleanField(default=False)