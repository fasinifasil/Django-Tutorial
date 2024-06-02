from django.contrib import admin

from App1.models import Employee, SuggestionMsg, LeaveReport

# Register your models here.
admin.site.register(Employee)
admin.site.register(SuggestionMsg)
admin.site.register(LeaveReport)