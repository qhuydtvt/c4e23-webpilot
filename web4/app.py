from flask import Flask, request, render_template, session, redirect
from models.user import User
import mlab

mlab.connect()
app = Flask(__name__)
app.config["SECRET_KEY"] = "dlgoiq454uwlfmsdl;fs"

@app.route("/profile")
def profile():
  if "token" in session:
    return render_template("profile.html")
  else:
    return "Forbidden!!!!"

@app.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "GET":
    return render_template("login.html")
  else:
    form = request.form
    username = form["username"]
    password = form["password"]
    found_user = User.objects(username=username).first()
    if found_user is None:
      return "No such users"
    elif found_user.password != password:
      return "Wrong password"
    else:
      session["token"] = username
      return "OK"

@app.route("/logout")
def logout():
  if "token" in session:
    del session["token"]
  return redirect("login")

if __name__ == '__main__':
  app.run(debug=True)