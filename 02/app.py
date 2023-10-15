from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

def teste():
    return '<p> testando 1 </p>'

def teste2():
    return '<p> testando 2 </p>'

app.add_url_rule('/teste', 'teste', teste)
app.add_url_rule('/teste2', 'teste2', teste2)

if __name__ == '__main__':
    app.run(debug=True, port='3000')