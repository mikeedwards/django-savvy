from django.db.models.fields import TextField, URLField, BooleanField, CharField,\
    DateTimeField, FloatField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ManyToManyField, ForeignKey
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from django_extensions.db.models import TitleSlugDescriptionModel,\
    TimeStampedModel
from django_extensions.db.fields import json, AutoSlugField
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
from mptt.managers import TreeManager

class ContentModel(TimeStampedModel):
    title = CharField(_('title'), max_length=255)
    slug = AutoSlugField(_('slug'), populate_from='generate_slug')
    description = TextField(_('description'), blank=True, null=True)
    authors = ManyToManyField(User, blank=True, null=True, related_name='%(class)ss')

    class Meta:
        abstract = True

    def generate_slug(self):
        return self.title
    
    def __unicode__(self):
        return self.title

class RelatedContent(ContentModel):
    url = URLField(blank=True,null=True)
    is_video = BooleanField(default=False)
    does_continue = BooleanField(default=False)

class Worksheet(ContentModel):
    instructions = TextField(blank=True,null=True)
    background = ImageField(upload_to="lessons/worksheets/backgrounds/")
    field_data = json.JSONField(blank=True,null=True)
    related_content = ManyToManyField(RelatedContent, blank=True, null=True, related_name='worksheets')

class UnitType(TitleSlugDescriptionModel):
    
    def __unicode__(self):
        return self.title
    
class Assignment(MPTTModel,TimeStampedModel):
    parent = TreeForeignKey("self",blank=True,null=True,related_name="children")
    worksheet = ForeignKey(Worksheet,related_name="assignments")
    unit = ForeignKey("Unit",related_name="assignments")
    start = DateTimeField(blank=True,null=True)
    end = DateTimeField(blank=True,null=True)
    hide_until_start = BooleanField(default=False)
    users = ManyToManyField(User, related_name="assignments", through="Engagement")
    
    objects = tree = TreeManager()

    def __unicode__(self):
        name = "%s assigned for %s %s" % (self.worksheet,self.unit.type,self.unit)
        if self.start:
            name += " starting %s" % (self.start)
        if self.end:
            name += " until %s" % (self.end)
                
        return name
    
class Engagement(TimeStampedModel):
    user = ForeignKey(User, related_name="engagements")
    assignment = ForeignKey(Assignment, related_name="engagements")
    field_data = json.JSONField(blank=True,null=True)
    
    def __unicode__(self):
        return "%s is engaging %s" % (self.user,self.assignment.worksheet)
    
class Assessment(TimeStampedModel):
    assessor = ForeignKey(User, related_name="assessment")
    engagement = ForeignKey(Engagement, related_name="assessments")
    field_data = json.JSONField(blank=True,null=True)
    notes = TextField(blank=True,null=True)
    points_awarded = FloatField(default=0.0)
    has_awarded = BooleanField(default=False)
    
    def __unicode__(self):
        return "%s assessed %s on %s" % (self.assessor,self.engagement.user,self.engagement.assignment.worksheet)
    
class Unit(MPTTModel,ContentModel):
    parent = TreeForeignKey("self",blank=True,null=True,related_name="children")
    type = ForeignKey("UnitType",related_name="units")
    worksheets = ManyToManyField("Worksheet",blank=True,null=True,related_name="units",through=Assignment)
    
    objects = tree = TreeManager()
        
    def __unicode__(self):
        return self.title
