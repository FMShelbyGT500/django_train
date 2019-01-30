from django.db import models
from django.utils import timezone
import datetime
from django.shortcuts import reverse


class Question(models.Model):
    question_text = models.CharField(max_length=200, db_index=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    # choices = self.choice_set.all()

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text

    def get_absolute_url(self):
        return reverse("polls:detail_url", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["-pub_date"]
    


class Choice(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, db_index=True)
    votes = models.IntegerField(default=0, db_index=True)

    def __str__(self):
        return self.choice_text
