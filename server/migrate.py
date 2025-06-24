# late-show-api-challenge/migrate.py
from flask_migrate import Migrate
from server.app import app, db

migrate = Migrate(app, db)

if __name__ == '__main__':
    import sys
    from flask_migrate import cli
    cli.main()