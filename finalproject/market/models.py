from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Profile(models.Model):
        name = models.CharField(max_length=30)
        imageUrl = models.ImageField(upload_to='images/', null=True)
        numbersOfPoints = models.IntegerField(null=True)
        type = models.ForeignKey(User, related_name='profiles', on_delete=models.CASCADE, null=True)

        def __str__(self):
            return f'{self.name}'

class Message(models.Model):
                name = models.CharField(max_length=30)
                message = models.CharField(max_length=200)
                numbersOfPoints = models.IntegerField(null=True)
                type = models.ForeignKey(User, related_name='message', on_delete=models.CASCADE, null=True)

                def __str__(self):
                        return f'{self.name}'


class Buy(models.Model):
        name = models.CharField(max_length=30)
        country = models.CharField(max_length=30)
        imageUrl = models.ImageField(upload_to='images/', null=True)
        price = models.IntegerField(null=True)
        type = models.ForeignKey(User, related_name='buy', on_delete=models.CASCADE, null=True)

        def __str__(self):
            return f'{self.name}'


'''class Question(models.Model):
    category = models.CharField(max_length=30)
    text = models.CharField(max_length=100, unique=True)
    difficulty = models.IntegerField(null=False)

    def __repr__(self):
        return f"Q{self.id}: {self.text}"

    def __str__(self):
        return f"Q{self.id}: {self.text}"


class Answer(models.Model):
    text = models.CharField(max_length=50)
    points = models.IntegerField(default=5)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="the_answers")

    def __repr__(self):
        return f"A{self.id}: {self.text}"'''


