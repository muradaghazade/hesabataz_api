from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group

class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ['email', 'first_name', 'last_name', 'number', 'has_company', 'company_type',] 
    list_display_links = ('email',)
    list_editable = ['first_name', 'last_name', 'number', 'has_company', 'company_type',]
    # search_fields = ('retailer',)

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

admin.site.site_header = "Hesabat.az"
admin.site.index_title = "Hesabat.az"
admin.site.site_title = "Hesabat.az Administration"
