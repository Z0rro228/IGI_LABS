from datetime import datetime

from django.db import models
from django.core import validators

# Create your models here.


class About(models.Model):
    description = models.TextField()

    class Meta:
        verbose_name_plural = "About us"

    def __str__(self):
        return "Description"


class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "FAQ"

    def __str__(self):
        return self.question


class UserFAQ(models.Model):
    question = models.CharField(max_length=255)
    new_question = models.CharField(max_length=255)
    new_answer = models.CharField(max_length=255)


class Contacts(models.Model):
    image = models.ImageField(upload_to="images/", default="images/no_image.jpg")
    name = models.CharField(max_length=255)
    position = models.TextField()
    phone = models.TextField()
    email = models.EmailField()

    class Meta:
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.name


class ConfidentialityPolicy(models.Model):
    policy = models.TextField()

    class Meta:
        verbose_name_plural = "Confidentiality Policy"

    def __str__(self):
        return "Policy"


class Vacancies(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Vacancies"

    def __str__(self):
        return self.name


class Feedback(models.Model):
    feedback = models.TextField()
    user_name = models.TextField()
    rate = models.PositiveIntegerField(
        validators=[
            validators.MaxValueValidator(10)
        ]
    )
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Feedback"

    def __str__(self):
        return self.feedback


class Places(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Places"

    def __str__(self):
        return self.address
