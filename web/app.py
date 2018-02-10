from flask import Flask, request, Response
from flask_login import login_user, logout_user, LoginManager
from yaml import safe_load

from user import User

with open('config.yml', 'r') as file:
    config = safe_load(file)

app = Flask(__name__)
app.secret_key = config['SECRET_KEY']

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(email):
    # TODO: implement db
    # return db.query.get(email)

    pass


@app.route('/user/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return Response('''
        <form action="" method="post">
            <p><input type=text name=email>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
        ''')
    elif request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User(email, password)
        login_user(user)

        return "Logged in"


@app.route('/user/logout')
def logout():
    logout_user()

    return "Logged out"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
