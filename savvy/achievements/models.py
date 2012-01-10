from django.db import models
from lessons.models import Unit, Engagement, Assessment
from badger.models import Badge, Progress, BadgeAlreadyAwardedException
from django.db.models.fields.related import ForeignKey
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save, pre_save

@receiver(post_save,sender=Engagement)
def post_save_engagement(sender, **kwargs):
    engagement = kwargs['instance']
    user = engagement.user
    unit = engagement.assignment.unit
    
    #check to see if this unit has goals
    for goal in unit.goals.all():
        Progress.objects.get_or_create(badge=goal.badge,user=user)
    
    for unit in unit.get_ancestors():
        for goal in unit.goals.all():
            Progress.objects.get_or_create(badge=goal.badge,user=user)
        
@receiver(pre_save,sender=Assessment)
def pre_save_engagement(sender, **kwargs):
    assessment = kwargs['instance']
    if assessment.points_awarded > 0 and not assessment.has_awarded:
        assessment.has_awarded = True
        
        for goal in assessment.engagement.assignment.unit.goals.all():
            try:
                progress,created = Progress.objects.get_or_create(badge=goal.badge,user=assessment.engagement.user)
            except BadgeAlreadyAwardedException, e:
                continue
            progress.increment_by(assessment.points_awarded)
            progress.update_percent(progress.counter,goal.badge.points)
            if goal.badge.is_awarded_to(assessment.engagement.user):
                award =  goal.badge.award_to(assessment.engagement.user)
                if award.creator is None:
                    award.creator = assessment.assessor
                    award.save()

        for unit in assessment.engagement.assignment.unit.get_ancestors():
            for goal in unit.goals.all():
                try:
                    progress,created = Progress.objects.get_or_create(badge=goal.badge,user=assessment.engagement.user)
                except BadgeAlreadyAwardedException, e:
                    continue
                progress.increment_by(assessment.points_awarded)
                progress.update_percent(progress.counter,goal.badge.points)
                if goal.badge.is_awarded_to(assessment.engagement.user):
                    award =  goal.badge.award_to(assessment.engagement.user)
                    if award.creator is None:
                        award.creator = assessment.assessor
                        award.save()


class Goal(models.Model):
    unit = ForeignKey(Unit, related_name="goals")
    badge = ForeignKey(Badge, related_name="goals")

    def __unicode__(self):
        return u"%s is a goal for %s" % (self.badge,self.unit)