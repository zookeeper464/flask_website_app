from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()
basedir = os.path.abspath(os.path.dirname(__file__))

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI') or \
    'sqlite:///' + os.path.join(basedir, 'project.db')

    db.init_app(app)

    from routes import main
    app.register_blueprint(main.bp)

    return app


if __name__  == "__main__":
    app = create_app()
    app.run(debug=True)