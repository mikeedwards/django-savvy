from django.db.models.fields.related import ManyToManyField, ForeignKey
from django.contrib.auth.models import User
from django.db.models.fields import DateTimeField, TextField, BooleanField

from django_extensions.db.models import TitleSlugDescriptionModel,\
    TimeStampedModel
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
from mptt.managers import TreeManager

from savvy.lessons.models import Unit
    
class AssemblyType(TitleSlugDescriptionModel):
    
    def __unicode__(self):
        return self.title
    
class Assembly(MPTTModel,TitleSlugDescriptionModel,TimeStampedModel):
    type = ForeignKey("AssemblyType",related_name="assemblies")
    parent = TreeForeignKey("self",blank=True,null=True,related_name="children")
    leaders = ManyToManyField(User,blank=True,null=True, related_name='assemblies_lead')
    learners = ManyToManyField(User,blank=True,null=True, related_name='assemblies_attended')
    units = ManyToManyField(Unit,blank=True,null=True,related_name='assemblies',through='ScheduleEntry')
    
    objects = tree = TreeManager()
    
    class Meta:
        verbose_name_plural = "assemblies"
    
    def __unicode__(self):
        return self.title

class ScheduleEntry(TimeStampedModel):
    start = DateTimeField(blank=True,null=True)
    end = DateTimeField(blank=True,null=True)
    notes = TextField(blank=True,null=True)
    assembly = ForeignKey(Assembly)
    unit = ForeignKey(Unit)
