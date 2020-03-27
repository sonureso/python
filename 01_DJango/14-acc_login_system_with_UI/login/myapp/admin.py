from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active','first_name','last_name',)
    list_filter = ('email', 'is_staff', 'is_active','first_name','last_name',)
	# to be displayed while editing a user.
    fieldsets = (
        (None, {'fields': ('first_name','last_name','email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
	# to be displayed while adding a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name','last_name','email', 'password1', 'password2', 'is_staff', 'is_active')}
			
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
