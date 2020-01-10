from django.db import models

class contact(models.Model):
        name = models.CharField(max_length=30)
        mobile_no = models.CharField(max_length=30)


class registration(models.Model):
    name= models.CharField(max_length=30)
    email = models.EmailField()


class login(models.Model):
    email= models.EmailField()

