#!/usr/bin/env python
# encoding=utf-8
# maintainer: rgaudin

from django.db import models
from django.contrib.auth.models import User, UserManager


class Provider(User):

    class Meta:
        app_label = 'bolibana_auth'

    phone_number = models.CharField(max_length=12, unique=True, \
                                    null=True, blank=True)
    access = models.ManyToManyField('Access', null=True, blank=True)

    objects = UserManager()

    def save(self, *args, **kwargs):

        if not self.phone_number:
            self.phone_number = None

        super(Provider, self).save(self, *args, **kwargs)
