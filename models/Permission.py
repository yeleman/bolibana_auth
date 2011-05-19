#!/usr/bin/env python
# encoding=utf-8
# maintainer: rgaudin

from django.db import models


class Permission(models.Model):

    class Meta:
        app_label = 'bolibana_auth'

    slug = models.SlugField(max_length=50, primary_key=True)

    def __unicode__(self):
        return self.slug
