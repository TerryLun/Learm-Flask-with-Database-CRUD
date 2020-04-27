from flask import Flask, render_template

app = Flask(__name__)

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
