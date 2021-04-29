from flask_migrate import Migrate, MigrateCommand, Manager

from run import app
from service_api.app import db

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
