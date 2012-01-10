'''
Created on Jan 3, 2012

@author: Mike_Edwards
'''
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.generic.detail import DetailView

def index(request):
    response = render_to_response('lessons/index.html', locals(), context_instance=RequestContext(request))
    return response

class PlanDetailView(DetailView):
    template_name = "lessons/worksheet_plan.html"

class TakeDetailView(DetailView):
    template_name = "lessons/worksheet_take.html"

class GradeDetailView(DetailView):
    template_name = "lessons/worksheet_grade.html"

def plan(request):
    response = render_to_response('lessons/plan.html', locals(), context_instance=RequestContext(request))
    return response

def take(request):
    response = render_to_response('lessons/take.html', locals(), context_instance=RequestContext(request))
    return response

def grade(request):
    response = render_to_response('lessons/grade.html', locals(), context_instance=RequestContext(request))
    return response

def eval(request):
    response = render_to_response('lessons/eval.html', locals(), context_instance=RequestContext(request))
    return response

