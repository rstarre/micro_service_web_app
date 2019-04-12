#!/usr/bin/env python3
# services/users/manage.py
import unittest

from flask.cli import FlaskGroup

from project import create_app, db
from project.api.models import User

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command('recreate_db')
def recreate_db():
    print(db)
    db.drop_all()
    print("dropped")
    db.create_all()
    print("created")
    db.session.commit()
    print("commited")


@cli.command('test')
def test():
    """runs the test without code coverage"""
    tests = unittest.TestLoader().discover('project.tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    else:
        return 1


if __name__ == '__main__':
    cli()
