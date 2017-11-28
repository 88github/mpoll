#coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

# 投票项
@python_2_unicode_compatible
class Poll(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name
# 投票选项
@python_2_unicode_compatible
class Pollitem(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image_url = models.URLField(default="https://imgur.com/gallery/Ni56S.png")
    vote = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

# 投票重复检测
class VoteCheck(models.Model):
    userid = models.PositiveIntegerField()
    pollid = models.PositiveIntegerField()
    pollitemid = models.PositiveIntegerField()
    vote_date = models.DateField()