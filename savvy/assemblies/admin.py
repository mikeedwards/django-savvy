'''
Created on Jan 8, 2012

@author: Mike_Edwards
'''
from django.contrib import admin
from assemblies.models import Assembly, AssemblyType, ScheduleEntry

admin.site.register(Assembly)
admin.site.register(AssemblyType)
admin.site.register(ScheduleEntry)
