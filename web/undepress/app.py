from flask import Flask, request, render_template
from flask_login import login_required, LoginManager, logout_user
from yaml import safe_load

import account

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

    return account.models.User(email, True)


@app.route('/account/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        account.register(request.form['email'], request.form['password'])
        return "Registered"


@app.route('/account/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        account.login(request.form['email'], request.form['password'])
        return "Logged in"


@app.route('/account/logout')
@login_required
def logout():
    logout_user()
    return "Logged out"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
