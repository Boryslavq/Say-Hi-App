from flask import Flask, request, render_template
from sqlalchemy import exc

from database.db_model import Users
from db import db

from data import config

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = config.POSTGRES_URI


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('your-name')
        user = Users(name=name)
        try:
            db.session.add(user)
            db.session.commit()  # сохраняем изменения и закрываем данную сессию
            return render_template('hello.html', title='Hello', name=name)
        except exc.IntegrityError:
            db.session.rollback()
            return render_template('hello.html', title='We have already seen', name=name)
    return render_template('index.html')


@app.route('/users')
def users():
    names = Users.query.all()
    return render_template('users.html', users=names)


if __name__ == '__main__':
    with app.app_context():
        db.init_app(app)
        db.create_all()
    app.run()
