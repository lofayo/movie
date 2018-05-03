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
      ],
      description='标签',
      render_kw={
        'class': 'form-control',
        'id': 'input_name',
        "placeholder": "请输入标签名称！"
      }
    )
    submit = SubmitField(
      '编辑',
      render_kw={
          "class": "btn btn-primary",
      }
    )
