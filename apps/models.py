from django.contrib.auth.models import AbstractUser
from django.db.models import ImageField, CharField, EmailField, TextField, Model, IntegerField, ForeignKey, CASCADE, \
    DateTimeField, TextChoices


class Agent(AbstractUser):
    image = ImageField(upload_to='agent/', blank=True, null=True)
    fullname = CharField(max_length=100)
    phone = CharField(max_length=50)
    email = EmailField()
    about = TextField(null=True)
    instagram = CharField(max_length=50, null=True)
    linkedin = CharField(max_length=50, null=True)

    def __str__(self):
        return self.fullname


class Property(Model):
    image = ImageField(upload_to='property/', blank=True, null=True)
    plan_image = ImageField(upload_to='plan_property/', blank=True, null=True)
    name = CharField(max_length=50)
    about = TextField()
    location = CharField(max_length=255)
    area = CharField(max_length=20)
    room = CharField(max_length=255)
    floor = CharField(max_length=255)
    price = CharField(max_length=255)
    author = ForeignKey('apps.Agent', CASCADE, related_name='my_property')
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Blog(Model):
    class Status(TextChoices):
        TRAVEL = 'travel', 'Travel'
        DISCOUNT = 'discount', 'Discount'
        NEWS = 'news', 'News'
    image = ImageField(upload_to='jpg/', blank=True, null=True)
    title = CharField(max_length=50)
    category = CharField(max_length=50, choices=Status.choices, default=Status.TRAVEL)
    about = TextField()
    author = ForeignKey('apps.Agent', CASCADE, related_name='my_blog')
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class TextToProperty(Model):
    image = ImageField(upload_to='text_property/', blank=True, null=True)
    fullname = CharField(max_length=70)
    text = TextField()
    to_category = ForeignKey('apps.Property', CASCADE, related_name='my_family')
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname


class Comment(Model):
    fullname = CharField(max_length=70)
    email = EmailField()
    text = TextField()
    to_blog = ForeignKey('apps.Blog', CASCADE, related_name='my_comment')
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname


class Email(Model):
    name = CharField(max_length=70)
    email = EmailField()
    text = TextField()

    def __str__(self):
        return self.name

