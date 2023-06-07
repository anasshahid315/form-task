from django.contrib import admin
from .models import Employee, Country, State, City

admin.site.register((Employee, Country, State, City))
