from django.contrib import admin
# Import import_export model for admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import Result

@admin.register(Result)
class PersonAdmin(ImportExportModelAdmin):
     list_display = ('id', 'name', 'sex', 'email', 'age', 'answer', 'person_type', 'work_exp',  'submitted_date')

#admin.site.register(Result);
