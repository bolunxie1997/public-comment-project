from flask_migrate import MigrateCommand,Migrate
from flask_script import Manager
from app import app,db
from models import User,Shop,Comment,Goods,Reply,ShopType

manager = Manager(app)

migrate = Migrate(app,db)

manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()