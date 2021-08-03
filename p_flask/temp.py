#db를 새로 만들 때 사용하는 파일
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI') or \
'sqlite:///' + os.path.join(basedir, 'project.db')

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String,nullable=False)

    inputs = db.relationship('Input', backref='user', lazy=True)
    Datas = db.relationship('Data', backref='user', lazy=True)

    def __repr__(self):
        return f'User_id {self.id}, username is {self.username}'

class Input(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    music_id = db.Column(db.String, db.ForeignKey('music.id'), nullable=False)

    def __repr__(self):
        return f'User_id {self.user_id}, music_id is {self.music_id}'

class Music(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    music = db.Column(db.String)
    musician = db.Column(db.String)
    tag = db.Column(db.String)

    inputss = db.relationship('Input', backref='music', lazy=True)

    def __repr__(self):
        return f'musician {self.musician}, music is {self.music}'

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    tag = db.Column(db.String)

    def __repr__(self):
        return f'user_id {self.user_id}, tag_id is {self.tag}'

db.create_all()
db.session.commit()
### 멜론 주제로 탐색https://www.melon.com/search/total/index.htm?q={가수이름}+{노래제목}&section=&searchGnbYn=Y&kkoSpl=Y&kkoDpType=&linkOrText=T&ipath=srch_form
### 여기에서 a를 찾아 처음 곡으로 이동
### 여기에서 테그를 찾아서 태그 가져오고 저장