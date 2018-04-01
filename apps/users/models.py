from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserProfile(AbstractUser):

    """
        用户表，新增字段如下
    """
    GENDER_CHOICES = (
        ("male", u"男"),
        ("female", u"女")
    )

    name = models.CharField(max_length=30, null=True, blank=True, verbose_name=u"姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name=u"出生年月")
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default="female", verbose_name=u"性别")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name=u"电话", help_text=u"电话号码")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name=u"邮箱")
    imei = models.CharField(max_length=100, verbose_name=u"手机序列号")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username