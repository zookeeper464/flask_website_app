from flask import Blueprint
from app import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return '''안녕하세요 :)
이름과 원하시는 원하시는 행동을 주소창에 넣어주세요.
예시는 다음과 같습니다.
/gil-Dong Hong/read'''

@bp.route('/<username>/', defaults={'method':'read'})
@bp.route('/<username>/<method>')
def show_me_the_music(username, method): # 유저 아이디를 입력하면 유저가 고른 음악을 보여준다.
    if username == 'api':
        return '잘못된 주소를 선택하셨습니다.'
    if method == 'read':
        from models import User, Input, Music
        lst = Music.query.join(Input, Music.id==Input.music_id).join(User, User.id==Input.user_id).filter(User.username==username).all()
        temp = ''
        for i in lst:
            temp += ' '.join(i)
            temp += '\n'
        return temp
        #return f'{userid}에 해당하는 id와 연관된 음악을 Music table에서 호출한다.'
    elif method == 'update':
        return f'/api/update/{username}로 이동해 주세요.'
        #return f'update를 하기 위한 페이지로 이동한다. (이곳에서 삭제도 담당한다.)'
    elif method == 'create':
        from models import User
        if not User.query.filter(User.username==username).first():
            q = User(username=username)
            db.session.add(q)
            db.session.commit()
            return '유저 데이터가 추가되었습니다.'
        else:
            return '유저 데이터가 이미 존재합니다.'
        #return f'create를 하기 위하여 새롭게 userid와 username을 User table에 추가한다.'
    elif method == 'predict':
        return f'/api/predict/{username}로 이동해 주세요.'
        #return f'username이 원하는 음악을 추천하는 페이지로 넘어간다.'
    else:
        return '잘못된 방법을 입력하셨습니다.'

@bp.route('/api/', defaults={'role':False,'username':False})
@bp.route('/api/<role>/', defaults={'username':False})
@bp.route('/api/<role>/<username>')
def add_user(username,role):
    if role == False:
        return '잘못된 주소로 들어왔습니다.'
    elif role == 'predict':
        return f'{username}에 해당하는 추천음악입니다.'
    elif role == 'update':
        from music_scraping import run
        return f'{username}에 해당하는 데이터입니다. 생성,수정, 삭제하고 싶은 내용을 입력하세요.'
    else:
        return '잘못된 방법을 입력하셨습니다.'