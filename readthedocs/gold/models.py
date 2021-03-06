from django.db import models
from django.utils.translation import ugettext_lazy as _

LEVEL_CHOICES = (
    ('v1-org-patron', '$5'),
    ('v1-org-supporter', '$10'),
)


class GoldUser(models.Model):
    pub_date = models.DateTimeField(_('Publication date'), auto_now_add=True)
    modified_date = models.DateTimeField(_('Modified date'), auto_now=True)

    user = models.ForeignKey('auth.User', verbose_name=_('User'), unique=True, related_name='gold')
    level = models.CharField(_('Level'), max_length=20, choices=LEVEL_CHOICES, default='supporter')

    last_4_digits = models.CharField(max_length=4)
    stripe_id = models.CharField(max_length=255)
    subscribed = models.BooleanField(default=False)
