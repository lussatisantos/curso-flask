from flask import Flask

app = Flask(__name__)

@app.route('/hello')
@app.route('/hello/<nome>')
def hello(nome=''):
    return '<h1> Hello {}</h1>'.format(nome)

if __name__ == '__main__':
    app.run(debug=True)