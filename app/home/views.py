#coding:utf8

from . import home
from flask import render_template, url_for, redirect

@home.route('/')
def index():
  return render_template('home/index.html')

@home.route('/login')
def login():
  # 一个是渲染某个模板
  return render_template('home/login.html')

@home.route('/logout')
def logout():
  # 一个是重定向到某个路由，使用函数名反推路由名，最后还是对应到模板上
  return redirect(url_for('home.login'))
  # return render_template('home/login.html')

@home.route('/search')
def search():
  return render_template('home/search.html')

@home.route('/regist')
def regist():
  return render_template('home/regist.html')

@home.route('/user')
def user():
  return render_template('home/user.html')
  
@home.route('/pwd')
def pwd():
  return render_template('home/pwd.html')

@home.route('/comment')
def comment():
  return render_template('home/comment.html')

@home.route('/loginlog')
def loginlog():
  return render_template('home/loginlog.html')

@home.route('/moviecol')
def moviecol():
  return render_template('home/moviecol.html')

@home.route('/play')
def play():
  return render_template('home/play.html')

