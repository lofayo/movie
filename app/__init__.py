#coding:utf8
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import pymysql
from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

pymysql.install_as_MySQLdb()
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://lofayo:123456@127.0.0.1:3306/movie'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


app.config["SECRET_KEY"] = '\xdd\xc0\x04\xc3\xd1\xfbW\x18\t\xc3\x0c\x10\x89\xae\x89\x13\xfc\xab\x84\\\xf5\xd4-\x96'
app.config["WTF_CSRF_SECRET_KEY"] = '\xdd\xc0\x04\xc3\xd1\xfbW\x18\t\xc3\x0c\x10\x89\xae\x89\x13\xfc\xab\x84\\\xf5\xd4-\x96'

db = SQLAlchemy(app)
# 导入蓝图


# 注册蓝图
app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix='/admin')
