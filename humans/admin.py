from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(DefaultUserAdmin):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fieldsets += (('Key options', {
            'classes': ('collapse',),
            'fields': ('fingerprint', 'keyserver_url', 'public_key'),
        }),)


admin.site.site_header = "HawkPost Administration"
admin.site.site_title = "HawkPost Admin"
admin.site.index_title = "Project Models"
