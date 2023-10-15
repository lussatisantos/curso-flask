from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/admin')
def admin():
    return '<h1>Admin</h1>'

@app.route('/guest/<name>')
def guest(name):
    return '<p> ola guest <b>%s</b></p>' % name

if __name__ == '__main__':
    app.run(debug=True)