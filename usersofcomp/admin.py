from django.contrib import admin

# Register your models here.
from usersofcomp.models import UsersRole, CompUsers

admin.site.register(UsersRole)
admin.site.register(CompUsers)

