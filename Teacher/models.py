from __future__ import unicode_literals

from django.db import models


class Class(models.Model):
    name = models.CharField(u'Class Name', max_length=256)
    time = models.DateTimeField(u'Class Time', auto_now_add=False, editable=True)
    point1 = models.CharField(u'BulletPoint1', max_length=256)
    point2 = models.CharField(u'BulletPoint2', max_length=256)
    point3 = models.CharField(u'BulletPoint3', max_length=256)
    point4 = models.CharField(u'BulletPoint4', max_length=256)
    point5 = models.CharField(u'BulletPoint5', max_length=256)
    teacher = models.CharField(u'Teacher', max_length=256, default="null")

    def __unicode__(self):
        return self.name


class Question(models.Model):
    name = models.CharField(u'Class Name', max_length=256)

    def __unicode__(self):
        return self.name