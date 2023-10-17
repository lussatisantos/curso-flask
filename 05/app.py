# Metodos HTTP

from flask import Flask

app = Flask(__name__, static_folder='public')

@app.route('/add/', methods=["POST"])
def add():
    return 'OKK'

if __name__ == '__main__':
    app.run()