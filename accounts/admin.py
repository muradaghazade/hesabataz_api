from django.contrib import admin
from .models import User, Company, Employee
from django.contrib.auth.models import Group

class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ['email', 'first_name', 'last_name', 'number', 'has_company', 'company_type','voen_number', 'has_worker','is_taxpayer', 'set_time', 'voen_number',] 
    list_display_links = ('email',)
    list_editable = ['first_name', 'last_name', 'number', 'has_company', 'company_type','voen_number', 'has_worker','is_taxpayer', 'set_time', 'voen_number',]

class CompanyAdmin(admin.ModelAdmin):
    model = Company
    list_display = ['company_name', 'category', 'passport_number', 'passport_fin', 'birth_date', 'address','address', 'document', 'voen', 'staff_count', 'company_sector', 'bank_rekvizit', 'income', 'expences',] 
    list_display_links = ('company_name',)
    list_editable = ['category', 'passport_number', 'passport_fin', 'birth_date', 'address', 'document', 'voen', 'staff_count', 'company_sector', 'bank_rekvizit', 'income', 'expences',]

class EmployeeAdmin(admin.ModelAdmin):
    model = Employee
    list_display = ['id', 'first_name', 'last_name', 'passport_number', 'company', 'position', 'salary', 'start_date', 'end_date',]
    list_display_links = ('id',)
    list_editable = ['first_name', 'last_name', 'passport_number', 'company', 'position', 'salary', 'start_date', 'end_date',]


admin.site.register(User, UserAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.unregister(Group)

admin.site.site_header = "Hesabat.az"
admin.site.index_title = "Hesabat.az"
admin.site.site_title = "Hesabat.az Administration"
