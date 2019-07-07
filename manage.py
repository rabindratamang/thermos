from thermos import app, db
from flask_script import Manager, prompt_bool

manager = Manager(app)


@manager.command
def initdb():
    db.create_all()
    print('Initialized the database')


@manager.command
def dropdb():
    if prompt_bool("Are you sure you want to drop db?"):
        db.drop_all()
        print('Dropped databases')


if __name__ == '__main__':
    manager.run()
