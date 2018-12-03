from flask import Flask, render_template, request
import mlab
from movie import Movie
from user import User

mlab.connect()
app = Flask(__name__)

@app.route("/add_movie", methods=["GET", "POST"])
def add_movie():
  if request.method == "GET":
    # User request form
    return render_template("add_movie.html")
  elif request.method == "POST":
    form = request.form
    t = form["title"]
    img = form["image"]
    y = form["year"]
    
    m = Movie(title=t, image=img, year=y)
    m.save()
    return "Gotcha!!!!"

@app.route("/register", methods=["GET", "POST"])
def register():
  if request.method == "GET":
    return render_template("register.html")
  elif request.method == "POST":
    form = request.form
    u = form["username"]
    p = form["password"]

    exist_user = User.objects().first()
    if exist_user != None: # Found existing user
      return "User already exists!"
    else:
      user = User(username=u, password=p)
      user.save()
      return "OK!!!"

if __name__ == "__main__":
  app.run(debug=True)