# tutorial/tables.py
import django_tables2 as tables
from spreadsheet.models import Subjects

class SubjectsTable(tables.Table):
    class Meta:
        model = Subjects
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", )
