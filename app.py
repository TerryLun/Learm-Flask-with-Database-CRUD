from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# database setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
"""
create the db file by going to terminal:
>>> from app import db
>>> db.create_all()

in terminal:
    add entries:
    >>> db.session.add(ModelName(**kwargs))
    >>> db.session.commit()  # must commit or it disappear after session ends
    
    querys:
    >>> ModelName.query.all()
    >>> ModelName.query.first()
    >>> ModelName.query.get(index)
    >>> ModelName.query.all()[index]
    >>> ModelName.query.all()[index].key
    >>> ModelName.query.filter_by(key=value).all()
    >>> ModelName.query.order_by(BlogPost.date_posted).all()
    
    delete:
    >>> db.session.delete(ModelName.query...)
    >>> db.session.commit()
"""


# database schema/model
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)  # up to 100 characters
    content = db.Column(db.Text, nullable=False)  # Text has no length limit
    author = db.Column(db.String(20), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return 'Blog post ' + str(self.id)


# all_posts = [
#     {
#         'title': "Post 1",
#         'content': "This is the content of post 1.",
#         'author': 'Terry'
#     },
#     {
#         'title': "Post 2",
#         'content': "This is the content of post 2."
#     }
# ]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/posts', methods=['GET', 'POST'])
def posts():
    # POST
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']
        if post_title and post_content and post_author:
            new_post = BlogPost(title=post_title, content=post_content, author=post_author)
            db.session.add(new_post)  # insert
        db.session.commit()  # don't forget
        return redirect('/posts')
    # GET
    else:
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()  # retrieve
    return render_template('posts.html', posts=all_posts)


@app.route('/home/<string:name>/posts/<int:id>')
def hello(name, id):
    return 'Hi, ' + name + str(id)


@app.route('/onlyget', methods=['GET'])
def get_req():
    print("GET: /onlyget")
    return "GET"


if __name__ == '__main__':
    app.run(debug=True)
