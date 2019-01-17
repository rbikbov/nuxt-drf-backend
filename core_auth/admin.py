from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

UserModel = get_user_model()

admin.site.register(UserModel, UserAdmin)
