"""
author: Edgar
课程相关的数据库模型
"""

from django.db import models

TYPES = (  # 课程的类型
    ("CO", "必修"),  # 必修
    ("El", "选修"),  # 选修
    ("Ex", '实验'),  # 实验
    ("Ot", '其他')  # 其他
)

SCHOOLS=(   #   学院名称
    ("1","电子信息与电气工程学院"),
    ("2","机械与动力工程学院"),
    ("3","船舶海洋与建筑工程学院"),
    ("4","生物医学工程学院"),
    ("5","航空航天学院"),
    ("6","数学科学院"),
    ("7","物理与天文学院"),
    ("8","化学化工学院"),
    ("9","致远学院"),
    ("10","医学院"),
    ("11","安泰经济与管理学院"),
    ("12","人文学院"),
)


class Course(models.Model):
    """课程数据库"""
    name = models.CharField(max_length=100, unique=True)  # 课程的名字
    type = models.CharField(choices=TYPES, max_length=30)  # 课程类型
    major = models.CharField(max_length=40)  # 专业名
    school= models.CharField(choices=SCHOOLS,max_length=40, default='')  #开设学院名
    class Meta:
        ordering = ("name", )  # 排序方式

    def __str__(self):
        return self.name


class TeacherOfCourse(models.Model):
    """课程的教师"""
    course_id = models.ForeignKey('Course',on_delete=models.CASCADE)  # 对应course的id
    name = models.CharField(max_length=40, null=True)  # 教师的姓名

    class Meta:
        ordering = ("course_id",)

    def __str__(self):
        return self.name


class CourseDes(models.Model):
    """相应老师的课程描述"""
    user_id = models.IntegerField(null=True, blank=True)  # 哪一个用户写的
    course_id = models.ForeignKey('Course',on_delete=models.CASCADE)  # 对应Course中自动生成的id
    des = models.TextField(default="暂无描述")  # 描述的信息course

    class Meta:
        ordering = ("des", )

    def __str__(self):
        return self.des


class Major(models.Model):

    """专业对应的信息"""
    name = models.CharField(max_length=40)  # 专业名
    academy = models.CharField(max_length=40)  # 所属的学院

    class Meta:
        ordering = ("name", )

    def __str__(self):
        return self.name


