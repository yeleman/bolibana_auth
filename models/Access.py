#!/usr/bin/env python
# encoding=utf-8
# maintainer: rgaudin

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


class Access(models.Model):

    class Meta:
        app_label = 'bolibana_auth'

    role = models.ForeignKey('Role')
    # entity
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    target = generic.GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return u"%(role)s on %(target)s" \
               % {'role': self.role, 'target': self.target}
