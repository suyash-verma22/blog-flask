from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

#connecting to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

# localhost:5000/user/suyash/17103052 type url will work
@app.route('/user/<string:name>/<int:id>/')  
def print_hi(name,id):
    return "Hello, " + name + " Welcome " + "id: " + str(id); 

class BlogPosts(db_Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.string(100),nullable=False)
    content = db.Column(db.Text,nullable = False)
    author = db.Column(db.string(20),nullable = False, default = 'N/A')
    date_of_post = db.Column(db.datetime,nullable = False, default =datetime.utcnow)

    def __repr__(self):
        return "Blog post id: " + str(self.id)
if __name__ == '__main__':
    print('Suyash verma')
    app.run(debug = True)

"""all_posts = [
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

# localhost:5000/posts will work
@app.route('/posts')
def show_posts():
    return render_template('posts.html',posts = all_posts)
"""

