from django.shortcuts import render

# Create your views here.
from dataclasses import fields
from django.http import HttpResponse
from django.views.generic import CreateView
from .models import Days, Spreadsheet, Subjects
from django_tables2 import SingleTableView
from spreadsheet.tables import SubjectsTable

class HomeView(SingleTableView):
    model = Subjects
    template_name = 'home.html'
    table_class = SubjectsTable

class AddSpreadsheet(CreateView):
    model = Spreadsheet
    template_name = 'spreadsheet.html'
    fields = ('course','days',)
