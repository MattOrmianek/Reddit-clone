import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, User, Post, Comment, Subreddit
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'mysql+pymysql://user:password@localhost/reddit')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([
        {
            'id': p.id,
            'title': p.title,
            'content': p.content,
            'author': p.author.username,
            'subreddit': p.subreddit.name
        }
        for p in posts
    ])


@app.route('/posts', methods=['POST'])
def create_post():
    data = request.json
    post = Post(title=data['title'], content=data['content'],
                user_id=data['user_id'], subreddit_id=data['subreddit_id'])
    db.session.add(post)
    db.session.commit()
    return jsonify({'status': 'created', 'id': post.id}), 201


@app.route('/comments', methods=['POST'])
def create_comment():
    data = request.json
    comment = Comment(content=data['content'], user_id=data['user_id'], post_id=data['post_id'])
    db.session.add(comment)
    db.session.commit()
    return jsonify({'status': 'created', 'id': comment.id}), 201


@app.route('/subreddits', methods=['GET'])
def get_subreddits():
    subs = Subreddit.query.all()
    return jsonify([{'id': s.id, 'name': s.name} for s in subs])


if __name__ == '__main__':
    app.run(debug=True)
