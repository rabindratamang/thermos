from flask import Flask, render_template, url_for

app = Flask(__name__)


class User:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def fullname(self):
        return f"{self.first} {self.last}"


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Title", user=User("Rabindra", "Tamang"))


@app.route('/add-bookmark')
def add_bookmark():
    return render_template('add.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(debug=True)
