from flask import Flask, render_template
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
    
    return all entries:
    >>> ModelName.query.all()
"""


# database schema/model
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)  # up to 100 characters
    content = db.Column(db.Text, nullable=False)  # Text has no length limit
    author = db.Column(db.String(20), nullable=False, default='N/A')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return 'Blog post ' + str(self.id)


all_posts = [
    {
        'title': "Post 1",
        'content': "This is the content of post 1.",
        'author': 'Terry'
    },
    {
        'title': "Post 2",
        'content': "This is the content of post 2."
    }
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/posts')
def posts():
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
