from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from logging import DEBUG


app = Flask(__name__)
app.logger.setLevel(DEBUG)


class User:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def fullname(self):
        return f"{self.first} {self.last}"


bookmarks = []


def store_bookmark(url):
    bookmarks.append(dict(
        url=url,
        user='rabindra tamang',
        date=datetime.utcnow()
    ))


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Title", user=User("Rabindra", "Tamang"))


@app.route('/add-bookmark', methods=['GET','POST'])
def add_bookmark():
    if request.method == 'POST':
        url = request.form['url']
        store_bookmark(url)
        app.logger.debug('stored_url : '+url)
        return redirect(url_for('index'))

    return render_template('add.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(debug=True)
