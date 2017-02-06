# coding=utf-8

from __future__ import unicode_literals

from django.db import models


class Article(models.Model):
    article_name = models.CharField(max_length=30)
    # 文章名字
    subtitle = models.CharField(max_length=100)
    # 小字体副标题
    cover_image_url = models.URLField()
    # 封面照片地址
    publish_date = models.DateField()
    # 发布日期
    view_count = models.IntegerField()
    # 阅览总量统计
    article_url = models.URLField()
    # 文章地址
