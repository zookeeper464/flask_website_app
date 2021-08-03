from app import db

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

#class predict(db.Model):
#count하여 제일 높은 태그 2개를 뽑아 1,2위를 통해 예측모델을 세운다.

