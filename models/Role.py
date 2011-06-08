#!/usr/bin/env python
# encoding=utf-8
# maintainer: rgaudin

from django.db import models


class Role(models.Model):

    class Meta:
        app_label = 'bolibana_auth'

    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=15, primary_key=True)
    permissions = models.ManyToManyField('Permission', null=True, blank=True)

    def __unicode__(self):
        return self.name
