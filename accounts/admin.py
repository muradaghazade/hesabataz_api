from django.contrib import admin
from .models import User, Employee, Income, Expence, WorkField, Invoice, Document, DocumentExample, CobsOffer, WorkCategory
from django.contrib.auth.models import Group


class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ['email', 'first_name', 'last_name', 'number', 'has_company', 'company_type','voen_number', 'has_worker','is_taxpayer', 'set_time', 'voen_number',] 
    list_display_links = ('email',)
    list_editable = ['first_name', 'last_name', 'number', 'has_company', 'company_type','voen_number', 'has_worker','is_taxpayer', 'set_time', 'voen_number',]


# class CompanyAdmin(admin.ModelAdmin):
#     model = Company
#     list_display = ['company_name', 'category', 'passport_number', 'passport_fin', 'birth_date', 'address','address', 'document', 'voen', 'staff_count', 'company_sector', 'bank_rekvizit',] 
#     list_display_links = ('company_name',)
#     list_editable = ['category', 'passport_number', 'passport_fin', 'birth_date', 'address', 'document', 'voen', 'staff_count', 'company_sector', 'bank_rekvizit',]


class EmployeeAdmin(admin.ModelAdmin):
    model = Employee
    list_display = ['id', 'first_name', 'last_name', 'passport_number', 'user', 'position', 'salary', 'start_date', 'end_date',]
    list_display_links = ('id',)
    list_editable = ['first_name', 'last_name', 'passport_number', 'user', 'position', 'salary', 'start_date', 'end_date',]


class IncomeAdmin(admin.ModelAdmin):
    model = Income
    list_display = ['id', 'title', 'amount', 'date',] 
    list_display_links = ('id',)
    list_editable = ['title', 'amount', 'date',]


class ExpenceAdmin(admin.ModelAdmin):
    model = Expence
    list_display = ['id', 'title', 'amount', 'date',] 
    list_display_links = ('id',)
    list_editable = ['title', 'amount', 'date',]


class ExpenceAdmin(admin.ModelAdmin):
    model = Expence
    list_display = ['id', 'title', 'amount', 'date',] 
    list_display_links = ('id',)
    list_editable = ['title', 'amount', 'date',]


class WorkFieldAdmin(admin.ModelAdmin):
    model = WorkField
    list_display = ['id', 'title', 'mdss', 'its', 'summary_amount',] 
    list_display_links = ('id',)
    list_editable = ['title', 'mdss', 'its',]


admin.site.register(User, UserAdmin)
admin.site.register(WorkField, WorkFieldAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Income, IncomeAdmin)
admin.site.register(Expence, ExpenceAdmin)

admin.site.register([Invoice, CobsOffer, Document, DocumentExample, WorkCategory,])

admin.site.unregister(Group)

admin.site.site_header = "Hesabat.az"
admin.site.index_title = "Hesabat.az"
admin.site.site_title = "Hesabat.az Administration"
