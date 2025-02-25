from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    type=models.CharField(max_length=50)

class User(models.Model):
    login_id=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    place=models.CharField(max_length=100)
    phone=models.BigIntegerField()



class Feedback(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    feedback=models.TextField()
    date = models.DateTimeField(auto_now_add=True)



