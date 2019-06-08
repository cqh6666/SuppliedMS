# _*_ encoding:utf-8 _*_

from datetime import datetime

from django.db import models

from supplied.models import LendTable
# Create your models here.


class CheckTable(models.Model):
    """
    借用申请表-用户查看是否通过审核，管理员审核
    """
    name = models.ForeignKey(LendTable, verbose_name=u"借用物资名称")
    organization = models.CharField(verbose_name="借用组织",max_length=50)
    lend_time = models.DateTimeField(default=datetime.now, verbose_name=u"借用时间")
    return_time = models.DateTimeField(default=datetime.now, verbose_name=u"归还时间")
    is_ok = models.BooleanField(verbose_name=u"是否可借用",default=False)

    class Meta:
        verbose_name = u"借用审核表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name