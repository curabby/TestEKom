from django.contrib import admin
from .models import CustomUser, FormTemplates
# Register your models here.
# Регистрация CustomUser
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_admin', )
    list_filter = ('is_admin', )
    search_fields = ('email', 'first_name', 'last_name', )
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_admin', 'is_superuser')}),
    )


@admin.register(FormTemplates)
class FormTemplatesAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'date', 'user_template')
    list_filter = ('date', 'user_template')
    search_fields = ('name', 'email', 'phone_number')
    fields = ('user_template', 'name', 'email', 'phone_number', 'date', 'description')
    ordering = ('-date',)
