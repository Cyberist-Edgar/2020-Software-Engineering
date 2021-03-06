"""
author: Edgar
用户相关的数据库模型
"""
from django.db import models
from django.contrib.auth.models import User as AuthUser
from django.utils import timezone

GRADES = (('FR', '大一'),
          ('SO', '大二'),
          ('JR', '大三'),
          ('SR', '大四'),
          ("OT", '其他'),
          ("UN", "未知")
          )

EXP_TYPE = (("PHYSICAL", "物理实验"),
            ("CHEMICAL", "化学实验"),
            ("CIRCUIT", "基电实验"),
            ("ELECTRONIC", "电子技术实验"),
            ("OTHERS", "其他实验")
            )


class User(models.Model):
    """用户数据库"""
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)  # 与django自带的User进行连接
    sex = models.BooleanField(default=True, blank=True, null=True)  # 性别 男 -> True
    profile = models.CharField(max_length=100, null=True, blank=True)  # 头像路径  可以为空
    academy = models.CharField(max_length=40, null=True, blank=True)  # 学院名  可以为空
    grade = models.CharField(choices=GRADES, max_length=30, default="UN", blank=True, null=True)  # 年级
    # 密保及对应答案  author 祁山青
    question = models.CharField(max_length=200, null=True, blank=True)  # 密保问题
    answer = models.CharField(max_length=200, null=True, blank=True)  # 答案

    def __str__(self):
        return self.user.username


class Files(models.Model):
    """文件"""
    user_id = models.IntegerField()  # 上传文件的用户
    type = models.CharField(choices=EXP_TYPE, max_length=40)  # 课程类型
    date = models.DateTimeField(default=timezone.now)  # 上传文件的时间
    download_times = models.IntegerField()  # 下载次数
    path = models.CharField(max_length=100)  # 实验数据的路径, 路径下的文件名需要进行一下处理，以免冲突
    name = models.CharField(max_length=40)  # 实验数据的名称
    desc = models.TextField(default="暂无描述")  # 文件的描述信息

    class Meta:
        ordering = ("-date",)

    def __str__(self):
        return self.name


class Notice(models.Model):
    """消息通知"""
    content = models.CharField(max_length=100)  # 通知内容
    date = models.DateTimeField(default=timezone.now)
    url = models.CharField(max_length=200)  # 产生通知的url
    read = models.BooleanField(default=False)  # 是否已读
    user_id = models.IntegerField()  # 用户id
