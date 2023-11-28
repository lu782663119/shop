from django.db import models


# Create your models here.

class User(models.Model):
    """
    User模型类，数据模型应该继承与model.Model或其子类
    """
    id = models.AutoField(primary_key=True)  # 创建主键
    username = models.CharField(max_length=32)  # 创建用户名字段 max_length字段长度
    password = models.CharField(max_length=32)  # 创建密码字段
    email = models.EmailField(max_length=30)  # 创建邮箱字段


class Article(models.Model):
    """
    文章模型类
    """
    id = models.AutoField(primary_key=True)  # 创建主键
    title = models.CharField(max_length=32)  # 创建标题字段
    content = models.TextField()  # 创建内容字段
    pub_time = models.DateTimeField()  # 创建时间字段
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 创建外键
