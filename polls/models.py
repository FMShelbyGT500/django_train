from django.db import models
from django.utils import timezone
import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, default='write there')
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Another(models.Model):
    foreign_empty = models.ForeignKey(Question, on_delete=models.CASCADE)
    char_field_empty = models.CharField(max_length=500, default='boo')
    integer_empty = models.IntegerField(default=0)

    def __str__(self):
        return self.char_field_empty


