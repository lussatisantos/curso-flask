#Arquivo WEB estaticos
from flask import Flask

app = Flask(__name__, static_folder='')



if __name__ == '__main__':
    app.run()