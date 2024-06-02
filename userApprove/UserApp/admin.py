from django.contrib import admin, messages

from UserApp.models import Employee

# Register your models here.
def make_approve(modeladmin,request,queryset):
    queryset.update(approve=True)
    messages.success(request, 'Employee Approved')


def remove_approve(modeladmin,request,queryset):
    queryset.update(approve=False)
    messages.success(request,'Employee Rejected')

class Employeetable(admin.ModelAdmin):
    list_display = ('Emp_Name','Emp_Team')
    actions = [make_approve,remove_approve]

    # def has_add_permission(self, request):
    #     return True
    def has_delete_permission(self, request, obj=None):
        return True
    # def has_change_permission(self, request, obj=None):
    #     return False

admin.site.register(Employee,Employeetable)