'''
Created on Jan 3, 2012

@author: Mike_Edwards
'''
from django.conf.urls.defaults import patterns, url
from django.views.generic.list import ListView
from savvy.lessons.models import Worksheet
from django.views.generic.detail import DetailView
from savvy.lessons.views import PlanDetailView, TakeDetailView, GradeDetailView

urlpatterns = patterns('',
    url(r'^worksheets/(?P<pk>[0-9]+)/plan/$', PlanDetailView.as_view(model=Worksheet,template_name="lessons/worksheet_plan.html",),name="lessons_worksheet_plan"),
    url(r'^worksheets/(?P<pk>[0-9]+)/take/$', TakeDetailView.as_view(model=Worksheet,),name="lessons_worksheet_take"),
    url(r'^worksheets/(?P<pk>[0-9]+)/grade/$', GradeDetailView.as_view(model=Worksheet,),name="lessons_worksheet_grade"),
    url(r'^worksheets/$', ListView.as_view(model=Worksheet,),name="lessons_worksheet_list"),
    url(r'^eval/$','savvy.lessons.views.eval',name='lessons_eval'),
    url(r'^$','savvy.lessons.views.index',name='lessons_index'),
)