from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_auth.serializers import PasswordResetSerializer
from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _

UserModel = get_user_model()


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)


class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = UserModel
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'groups',
            'bio',
            'location',
            'date_of_birth',
            'avatar_url',
        )
        read_only_fields = ('id', 'email',)


class CustomPasswordResetSerializer(PasswordResetSerializer):
    def validate_email(self, value):
        self.reset_form = self.password_reset_form_class(data=self.initial_data)
        if not self.reset_form.is_valid():
            raise serializers.ValidationError(self.reset_form.errors)

        if not UserModel.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError(_('Электронная почта не найдена'))

        return value
