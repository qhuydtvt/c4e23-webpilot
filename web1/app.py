from flask import Flask, render_template

app = Flask(__name__)

# function binding
@app.route("/")
def home():
  return "Hello Flask"

@app.route("/c4e")
def c4e():
  return "Hello C4E, hihi, haha"

@app.route("/hi/<name>")
def hi_nam(name):
  return "Hi " + name

@app.route("/add/<int:x>/<int:y>")
def add(x, y):
  s = x + y
  return str(s)


@app.route("/posts/<int:index>")
def posts(index):
  titles = [
    "Trời mưa to quá",
    "Trời nắng to quá",
    "Trời nhiều mây",
  ]
  contents = [
    "Ở nhà ngủ",
    "Viết gì bây giờ",
    "Tôi dốt văn quá",
  ]
  t = titles[index]
  c = contents[index]
  return render_template("post.html", title=t, content=c)

@app.route("/movie")
def movive():
  return render_template("movie.html", name="Deadpool", image="https://upload.wikimedia.org/wikipedia/en/thumb/2/23/Deadpool_%282016_poster%29.png/220px-Deadpool_%282016_poster%29.png")

@app.route("/movies")
def movies():
  # movie_titles = [
  #   "Deadpool",
  #   "Black widow",
  #   "Captain american",
  #   "Adam warlock"
  # ]
  movie_list = [
    {
      "title": "Deadpool",
      "image": "https://upload.wikimedia.org/wikipedia/en/thumb/2/23/Deadpool_%282016_poster%29.png/220px-Deadpool_%282016_poster%29.png",
    },
    {
      "title": "Black widow",
      "image": "https://static1.squarespace.com/static/51b3dc8ee4b051b96ceb10de/t/5bea011740ec9a97ddd3b6fe/1542062361805/?format=1500w",
    },
    {
      "title": "Adam warlock",
      "image": "https://d13ezvd6yrslxm.cloudfront.net/wp/wp-content/images/adam-warlock-700x300.jpg",
    }
  ]
  return render_template("movies.html", movies=movie_list)

if __name__ == "__main__":
  app.run(debug=True)