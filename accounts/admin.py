from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

#admin.site.register(User,UserAdmin)



class MyUserAdmin(UserAdmin):
    model = User

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('user_type',)}),
    )
    list_display=('username','user_type',)

admin.site.register(User, MyUserAdmin)