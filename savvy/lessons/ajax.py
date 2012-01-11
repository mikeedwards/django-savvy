'''
Created on Jan 6, 2012

@author: Mike_Edwards
'''
from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from django_extensions.utils.uuid import uuid4
from savvy.lessons.models import Worksheet
import logging 
from logging import DEBUG
log = logging.getLogger("django.response")
 
@dajaxice_register
def position_widget(request,top,left,current_id):

    print "Got here"
    print top,left,current_id
    if current_id is None:
        id = uuid4().hex
    else:
        id = current_id
    return simplejson.dumps({'id':id,'x':left,'y':top})

@dajaxice_register
def save(request,pk,widgets):
    pk = int(pk)
    for widget in widgets:
        widget['left'] = widget['left']/float(widget['backgroundWidth'])
        widget['top'] = widget['top']/float(widget['backgroundHeight'])
        widget['width'] = widget['width']/float(widget['backgroundWidth'])
        widget['height'] = widget['height']/float(widget['backgroundHeight'])
        
        log.log(DEBUG, widget)
    
    worksheet = Worksheet.objects.get(pk=pk)
    worksheet.field_data = simplejson.dumps(widgets)
    worksheet.save();
    return simplejson.dumps({'pk':pk,'widgets':widgets})
