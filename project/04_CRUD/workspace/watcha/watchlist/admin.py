from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Movie

# Register your models here.
@admin.register(Movie)
class PersonAdmin(ImportExportModelAdmin):
    pass