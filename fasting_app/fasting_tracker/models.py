from django.conf import settings
from django.db import models
# Create your models here.
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

from fasting_app.core.models import AuditableModel
from fasting_app.fasting_tracker.managers import FastingSessionManager


# from fasting_app.fasting_app.fasting_tracker.managers import FastingSessionManager


class FastingSession(AuditableModel, TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('User'), related_name='fasting_sessions',
                             on_delete=models.PROTECT)
    start_date = models.DateTimeField(_('Start date'))
    end_date = models.DateTimeField(_('End date'), null=True, blank=True)
    duration = models.FloatField(_('Duration'), default=0)
    target_duration = models.PositiveSmallIntegerField(_('Target duration'), default=16)
    comments = models.CharField(_('Comments'), max_length=180, null=True, blank=True)

    objects = FastingSessionManager()
