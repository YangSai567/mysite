from django.db import models
from django.utils import timezone

import datetime


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # pub_date = models.DateField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        print("------")
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # 实例化一个ForeignKey类为question
    choice_text = models.CharField(max_length=200)  # 实例化一个CharField类为choice_text
    votes = models.IntegerField(default=0)  # 每个choice对象都关联到一个question对象

    def __str__(self):
        return self.choice_text
