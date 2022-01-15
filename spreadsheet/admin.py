from django.contrib import admin
from django.db.models.fields import DateField
from .models import Subjects,Days, Spreadsheet
# Register your models here.

admin.site.register(Subjects)
admin.site.register(Days)
admin.site.register(Spreadsheet)