from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers

UserModel = get_user_model()


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name',)


class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = UserModel
        fields = (
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'last_name',
            'bio',
            'location',
            'date_of_birth',
            'avatar_url',
            'groups',
        )
        read_only_fields = ('id',)
