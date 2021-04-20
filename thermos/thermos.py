from flask import Flask, render_template, url_for

app = Flask(__name__)


class user:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return "{}. {}.".format(self.firstname, self.lastname)

@app.route('/index')

def default():
    return render_template('index.html', title="This is Abid Title", user=user('Abid','Khan'))

@app.route('/add')

def add():
    return render_template('add.html')

@app.errorhandler(404)

def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()
