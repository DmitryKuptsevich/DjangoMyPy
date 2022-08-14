from django.db import models

class Teacher(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()



class Tutorials(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    teacher = models.ForeignKey('Teacher', related_name='articles', on_delete=models.CASCADE)


