from mongoengine import Document, StringField, BooleanField

class Todo(Document):
  name = StringField()
  description = StringField()
  completed = BooleanField(default=False)
  def __str__(self):
    return '''Name: {0}
Description: {1}
Completed: {2} '''.format(self.name, 
                          self.description,
                          "Yes" if self.completed else "No")