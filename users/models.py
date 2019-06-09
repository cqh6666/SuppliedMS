# _*_ encoding:utf-8 _*_

from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class UserProfile(AbstractUser):
    """
    定义用户表,自带的已有username email is_superuser
    新增属性  学院 联系方式 组织 职务
    """
    college = models.CharField(verbose_name="学院",max_length=50)
    mobile = models.CharField(verbose_name="联系方式",max_length=11)
    organization = models.CharField(verbose_name="组织",max_length=50)
    position = models.CharField(verbose_name="职务",max_length=50)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class UserComment(models.Model):
    """
    定义用户评论表
    用户（外键）	留言内容 留言时间
    """
    user = models.ForeignKey(UserProfile,related_name='comment_user',verbose_name=u"用户")
    comments = models.CharField(max_length=200, verbose_name=u"评论")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = "用户评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.user,self.comments)
