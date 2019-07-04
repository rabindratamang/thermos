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


if __name__ == "__main__":
    app.run(debug=True)