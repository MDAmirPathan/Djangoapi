from django.contrib import admin
from api.models import Employee, Company
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'company')
    search_fields = ('name','position')
    list_filter = ('company',)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name',)




admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)