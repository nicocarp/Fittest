from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index'

@app.route('/hello')
def hello_world():
    return 'Hola mundo'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'Procesar el login post'
    else:
        return 'Mostrar form login'

@app.route('/algo/<int:algo_id>')
def show_post(algo_id):
    return 'Post %d' % algo_id


if __name__ == '__main__':
    app.run(debug = True)