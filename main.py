from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/user/<string:name>/<int:id>/')  
def print_hi(name,id):
    return "Hello, " + name + " Welcome " + "id: " + str(id); 
all_posts = [
    {
    'title': 'Post 1',
    'content': 'This is my content of post 1',
    'author': 'Suyash verma'
    },
    {
    'title': 'Post 2',
    'content': 'This is my content of post 2',
    }
]
@app.route('/posts')
def show_posts():
    return render_template('posts.html',posts = all_posts)

if __name__ == '__main__':
    print('Suyash verma')
    app.run(debug = True)

