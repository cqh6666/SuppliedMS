# _*_ encoding:utf-8 _*_

from datetime import datetime

from django.db import models
from users.models import UserProfile
# Create your models here.


class SuppliedInfo(models.Model):
    """
    物资表-核心数据表，存储所有物资信息
    """
    name = models.CharField(verbose_name="物资名称",max_length=50)
    unit = models.CharField(verbose_name="单位",max_length=5)
    specification = models.CharField(verbose_name="规格",max_length=5)
    number = models.IntegerField(verbose_name=u"数量",default=1)
    price = models.IntegerField(verbose_name=u"借用价格",default=0)
    is_lend = models.BooleanField(verbose_name=u"是否可借用",default=False)

    class Meta:
        verbose_name = u"物资详情信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class SuppliedLend(models.Model):
    """
    物资外借表-核心数据表，存储所有物资外借情况的数据
    存储已经外借的物资
    """
    name = models.ForeignKey(SuppliedInfo, verbose_name=u"借用物资名称")
    specification = models.CharField(verbose_name="借用规格",max_length=5)
    number = models.IntegerField(verbose_name=u"数量",default=1)
    lend_time = models.DateTimeField(default=datetime.now, verbose_name=u"借用时间")
    return_time = models.DateTimeField(default=datetime.now, verbose_name=u"归还时间")
    organization = models.CharField(verbose_name="借用组织",max_length=50)

    class Meta:
        verbose_name = u"物资外借表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user


class LendTable(models.Model):
    """
    物资借用详情表-借用时在页面填写，存储借用的详细情况
    """
    name = models.ForeignKey(SuppliedInfo, verbose_name=u"借用物资名称")
    specification = models.CharField(verbose_name="借用规格",max_length=5)
    number = models.IntegerField(verbose_name=u"借用数量",default=1)
    lend_time = models.DateTimeField(default=datetime.now, verbose_name=u"借用时间")
    return_time = models.DateTimeField(default=datetime.now, verbose_name=u"归还时间")
    organization = models.CharField(verbose_name="借用组织",max_length=50)
    head_user = models.ForeignKey(UserProfile,verbose_name=u"负责人姓名")
    mobile = models.CharField(verbose_name="联系方式",max_length=11)
    submit_time = models.DateTimeField(default=datetime.now, verbose_name=u"提交时间")


    class Meta:
        verbose_name = "借用详情表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name