from django.db import models

from users.models import User


class Test(models.Model):
    TYPE_CHOICES = (('cognitive', 'cognitive test'),
                    ('skill', 'skill evaluation'),
                    ('interview', 'structured interview'))
    type = models.CharField(max_length=255, choices=TYPE_CHOICES)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    class Meta:
        unique_together = ('type', 'title')


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    sequence = models.IntegerField()
    title = models.CharField(max_length=255)
    duration = models.DurationField()

    class Meta:
        unique_together = ('test', 'sequence')


class UserTest(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()

    class Meta:
        unique_together = ('test', 'user')


class UserQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    start_time = models.DateTimeField()

    class Meta:
        unique_together = ('question', 'user')
