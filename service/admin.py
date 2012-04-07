"""
Enum all classes to be updated by Django BackOffice
"""

from tilota.service import models
from django.contrib import admin

for model_name in models.__all__:
    admin.site.register(getattr(models, model_name))
