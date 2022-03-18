from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Skills, Post


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class Geeks(object):
    def __init__(self, languages, level, username):
        self.languages = languages
        self.level = level
        self.hidden = username


class SkillsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skills
        username = serializers.HiddenField(default=serializers.CurrentUserDefault())
        fields = ('languages', 'level', 'username')


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = ['id', 'project_name', 'description', 'max_collaborators', 'collaborators', 'owner']





