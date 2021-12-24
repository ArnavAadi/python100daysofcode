from flask import Flask, render_template
import requests
from post import Post


app = Flask(__name__)

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url)
blogs = response.json()
posts_objs = [Post(blog["title"], blog["subtitle"],
                   blog["body"], blog["id"]) for blog in blogs]


@app.route('/')
def home():
    return render_template("index.html", posts=posts_objs)


@app.route("/post/<blog_id>")
def get_blog(blog_id):
    req_post = None
    for post in posts_objs:
        print(post.id)
        print(blog_id)
        if int(post.id) == int(blog_id):
            req_post = post
    return render_template("post.html", reqpost=req_post)


if __name__ == "__main__":
    app.run(debug=True)
