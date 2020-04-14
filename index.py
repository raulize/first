from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hi'

@app.route('/myhome')
def myhome():
    return 'This is my page!'


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)