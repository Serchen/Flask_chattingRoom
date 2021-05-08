from os import access

from flask import Flask
from config import Config  # 从config模块导入Config类
from flask_sqlalchemy import SQLAlchemy  # 从包中导入类
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_babel import Babel
from flask import request
from flask_babel import Babel, lazy_gettext as _l

app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)  # 数据库对象
migrate = Migrate(app, db)  # 迁移引擎对象
login = LoginManager(app)
login.login_view = 'login'
login.login_message = _l('Please log in to access this page.')
mail = Mail(app)
babel = Babel(app)
bootstrap = Bootstrap(app)


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


from app import routes, models  # 导入一个新模块models，它将定义数据库的结构，目前为止尚未编写
