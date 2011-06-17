#!/usr/bin/env python
# encoding=utf-8
# maintainer: rgaudin

from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


class Access(models.Model):
    """ Bundle of a Role for a target object. Usually an Entity.

        Access itself doesn't grant anything. It's just a holder
        Add an access to a Provider instead """

    class Meta:
        app_label = 'bolibana_auth'
        unique_together = ('role', 'content_type', 'object_id')
        verbose_name = _(u"Access")
        verbose_name_plural = _(u"Access")

    role = models.ForeignKey('Role', verbose_name=_(u"Role"))
    # entity
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    target = generic.GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return ugettext(u"%(role)s on %(target)s") \
               % {'role': self.role, 'target': self.target}
