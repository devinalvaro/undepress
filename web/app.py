from flask import Flask

import src.undepress

app = Flask(__name__)


@app.route('/')
def welcome():
    return src.undepress.welcome()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
