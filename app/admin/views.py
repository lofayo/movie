# coding:utf8

from . import admin
from flask import render_template, url_for, redirect, flash
from app.admin.forms import TagForm

from app.models import db, Tag

# from app.models import app


# 主页
@admin.route('/')
def index():
    return render_template('admin/index.html')


# 登录
@admin.route('/login')
def login():
    return render_template('admin/login.html')


# 退出
@admin.route('/logout')
def logout():
    return redirect(url_for('admin.login'))


# 修改密码
@admin.route('/pwd')
def pwd():
    return render_template('admin/pwd.html')


# 添加标签
@admin.route('/tag/add', methods=['GET', 'POST'])
def tag_add():
    # 1、生成标签表单
    form = TagForm()
    # 3、表单提交POST请求，验证数据合法性
    if form.validate_on_submit():
        data = form.data
        # 查询数据是否重复
        query_tag = Tag.query.filter_by(name=data['name']).count()
        if query_tag == 1:
            flash('名称已经存在', 'err')
            return redirect(url_for('admin.tag_add'))
        # 将数据生成为表的一行记录，并存于数据库
        tag = Tag(name=data['name'])
        db.session.add(tag)
        db.session.commit()
        flash('标签添加成功', 'ok')
        return redirect(url_for('admin.tag_add'))
    # 2、一开始执行的是GET请求，将生成的表单渲染进模板，以实现模板的安全登录
    return render_template('admin/tag_add.html', form=form)


# 标签列表
@admin.route('/tag/list/<int:page>', methods=['GET'])
def tag_list(page):
    page_data = Tag.query.paginate(page=page, per_page=2)
    # printt(page_data)
    return render_template('admin/tag_list.html', page_data=page_data)


# 标签编辑
@admin.route('/tag/edit/<int:id>', methods=['GET', 'POST'])
def tag_edit(id):
    form = TagForm()
    tag = Tag.query.get_or_404(id)
    if form.validate_on_submit():
        data = form.data
        tag_count = Tag.query.filter_by(name=data['name']).count()
        if tag_count == 1:
            flash('标签名已经存在', 'err')
            return redirect(url_for('admin.tag_edit', id=id))
        tag.name = data['name']
        db.session.add(tag)
        db.session.commit()
        flash('标签修改成功', 'ok')
        return redirect(url_for('admin.tag_edit', id=id))
    return render_template('admin/tag_edit.html', form=form, tag=tag)


# 删除标签
@admin.route('/tag/del/<int:id>', methods=['GET', 'POST'])
def tag_del(id):
    tag = Tag.query.get_or_404(id)
    if tag:
        db.session.delete(tag)
        db.session.commit()
        flash('标签已删除', 'ok')
        return redirect(url_for('admin.tag_list', page=1))

