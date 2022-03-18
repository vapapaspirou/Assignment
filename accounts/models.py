from django.db import models
from django.contrib.auth.models import User

Languages = (
    ('C++','C++'),
    ('Java', 'Java'),
    ('Javascript','Javascript'),
    ('Python', 'Python'),
    ('Lua','Lua'),
    ('Rust', 'Rust'),
    ('Go','Go'),
    ('Julia','Julia'),
)


class Skills(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    languages = models.CharField(max_length=30, choices=Languages, default='0')
    level = models.CharField(max_length=200)


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    project_name = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=100, blank=True, default='')
    max_collaborators = models.CharField(max_length=100, blank=True, default='')
    collaborators = models.CharField(max_length=100, blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
