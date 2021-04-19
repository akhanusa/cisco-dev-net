from flask import Flask

app = Flask(__name__)

@app.route('/index')
def default():
    return 'Hello World \n'

if __name__ == '__main__':
    app.run()
