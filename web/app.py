from flask import Flask, request

app = Flask(__name__)


@app.route('/user/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    return username + ' ' + password


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
