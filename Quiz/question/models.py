from django.db import models
from django.contrib.auth.models import User

class Historyquiz(models.Model):
    option_choices = (
        ('A','A'),
        ('B','B'),
        ('C','C'),
        ('D','D'),
    )
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    question = models.TextField()
    ans_A = models.CharField(max_length=255)
    ans_B = models.CharField(max_length=255)
    ans_C = models.CharField(max_length=255)
    ans_D = models.CharField(max_length=255)
    correct_ans = models.CharField(max_length=2,choices=option_choices,default='A')
    def __str__(self):
        return ("question - "+ str(self.id))
    
class Geographyquiz(models.Model):
    option_choices = (
        ('A','A'),
        ('B','B'),
        ('C','C'),
        ('D','D'),
    )
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    question = models.TextField()
    ans_A = models.CharField(max_length=255)
    ans_B = models.CharField(max_length=255)
    ans_C = models.CharField(max_length=255)
    ans_D = models.CharField(max_length=255)
    correct_ans = models.CharField(max_length=2,choices=option_choices,default='A')
    def __str__(self):
        return ("question - "+ str(self.id))
    
class Astronomyquiz(models.Model):
    option_choices = (
        ('A','A'),
        ('B','B'),
        ('C','C'),
        ('D','D'),
    )
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    question = models.TextField()
    ans_A = models.CharField(max_length=255)
    ans_B = models.CharField(max_length=255)
    ans_C = models.CharField(max_length=255)
    ans_D = models.CharField(max_length=255)
    correct_ans = models.CharField(max_length=2,choices=option_choices,default='A')
    def __str__(self):
        return ("question - "+ str(self.id))