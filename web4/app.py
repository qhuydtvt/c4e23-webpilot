from flask import Flask, request, render_template, session
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
    if username != "admin":
      return "No such users"
    elif password != "12345678":
      return "Wrong password"
    else:
      session["token"] = username
      return "OK"

@app.route("/logout")
def logout():
  del session["token"]
  return "Logged out"

if __name__ == '__main__':
  app.run(debug=True)