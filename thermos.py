import os

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from forms import BookmarkForm

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = b'\xb9\xa0(6hq\xd0]\x89>C\x8dn\xabo\xff\xf2~&\x1a\x9b\xa2\xef\x84'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'thermos.db')
db = SQLAlchemy(app)


import models


@app.route('/')
def index():
    return render_template('index.html', new_bookmarks=models.Bookmark.newest(5))


@app.route('/add-bookmark', methods=['GET', 'POST'])
def add_bookmark():
    form = BookmarkForm()
    # checks http request and form
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        bm = models.Bookmark(url=url, description=description)
        db.session.add(bm)
        db.session.commit()
        flash(f"stored bookmark: {url}")
        return redirect(url_for('index'))
    return render_template('add.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(debug=True)
