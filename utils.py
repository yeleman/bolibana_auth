#!/usr/bin/env python
# encoding=utf-8
# maintainer: rgaudin

import unicodedata
import random
import re

from django.contrib.auth.models import User

PASSWORD_LENGTH = 8
USERNAME_MIN_LENGTH = 4
USERNAME_MAX_LENGTH = 8


def random_password():
    """ random password suitable for mobile typing """
    return ''.join([random.choice('abcdefghijklmnopqrstuvwxyz1234567890') \
                        for i in range(PASSWORD_LENGTH)])


def username_from_name(first_name, last_name):
    """ available username to use on User forged from first and last name """

    def new_slug(text, salt=None):
        """ assemble text and salt providing optimum length """
        if salt:
            username = text[:(USERNAME_MAX_LENGTH - salt.__len__())] + salt
        else:
            username = text[:USERNAME_MAX_LENGTH]
        if username.__len__() < USERNAME_MIN_LENGTH:
            username = "{0:{1}<{2}}".format(username, "a", USERNAME_MIN_LENGTH)
        return username

    def is_available(username):
        """ DB check for username use """
        return User.objects.filter(username=username).count() == 0

    def jdoe(first, last):
        """ first name initial followed by last name format """
        return u"%s%s" % (first[0], last)

    def johndoe(first, last):
        """ first name followed by last name format """
        return u"%s%s" % (first, last)

    def iterate(username):
        """ adds and increment a counter at end of username """
        # make sure username matches length requirements
        username = new_slug(username)
        if not is_available(username):
            # find the counter if any
            sp = re.split(r'([0-9]+)$', username)
            if sp.__len__() == 3:
                # increment existing counter
                username = sp[0]
                salt = unicode(int(sp[1]) + 1)
            else:
                # start counter at 1
                salt = '1'
            # bundle counter and username then loop
            return iterate(new_slug(username, salt))
        else:
            # username is available
            return username

    # normalize first and last name to ASCII only
    first_name = unicodedata.normalize('NFKD', \
                         unicode(first_name.lower())).encode('ASCII', 'ignore')
    last_name = unicodedata.normalize('NFKD', \
                          unicode(last_name.lower())).encode('ASCII', 'ignore')

    # iterate over a jdoe format
    return iterate(jdoe(first_name, last_name))
