from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm


# Register your models here.


class MyUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active','is_lecture','is_student')
    list_filter = ('email', 'first_name', 'last_name', 'is_staff', 'is_active','is_lecture','is_student')
    fieldsets = ((None, {'fields': ('email', 'password', 'first_name', 'last_name')}),
                  ('Permissions', {'fields': ('is_staff', 'is_active','is_lecture','is_student')}),
                 )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, MyUserAdmin)
