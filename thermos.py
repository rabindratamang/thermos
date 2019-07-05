from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = b'\xb9\xa0(6hq\xd0]\x89>C\x8dn\xabo\xff\xf2~&\x1a\x9b\xa2\xef\x84'


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


def new_bookmarks(num):
    return sorted(bookmarks, key=lambda bm: bm['date'], reverse=True)[:num]


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', new_bookmarks=new_bookmarks(5))


@app.route('/add-bookmark', methods=['GET', 'POST'])
def add_bookmark():
    if request.method == 'POST':
        url = request.form['url']
        store_bookmark(url)
        flash(f"stored bookmark: {url}")
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
