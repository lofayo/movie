# coding:utf8
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# 标签表单类
class TagForm(Form):
  name = StringField(
    label='名称',
    validators=[
          DataRequired("请输入标签！")
      ]
  )
  submit = SubmitField(
    '编辑'
  )