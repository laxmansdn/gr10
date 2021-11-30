from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('first_name', 'last_name', 'username', 'email', 'date_created', 'last_login', 'is_active',)
    list_display_links = ('first_name', 'last_name', 'username', 'email',)
    ordering = ('-date_created',)
    readonly_fields = ('last_login', 'date_created',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
