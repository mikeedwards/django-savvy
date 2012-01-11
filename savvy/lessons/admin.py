'''
Created on Jan 8, 2012

@author: Mike_Edwards
'''
from django.contrib import admin
from savvy.lessons.models import Unit, Worksheet, RelatedContent, UnitType, Assignment, Engagement,\
    Assessment

admin.site.register(Assignment)
admin.site.register(Assessment)
admin.site.register(Engagement)
admin.site.register(RelatedContent)
admin.site.register(Unit)
admin.site.register(UnitType)
admin.site.register(Worksheet)
