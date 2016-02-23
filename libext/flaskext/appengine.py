#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    flaskext.appengine
    ------------------

    Adds basic App Engine support for Flask.

    :copyright: (c) 2011 by tnakaura.
    :license: BSD, see LICENSE for more details.
"""
from functools import wraps
from google.appengine.api import users
from werkzeug.exceptions import (
    NotFound, Unauthorized, Forbidden,
)
from flask import (
    request, redirect,
)


class AppEngine(object):
    def __init__(self, app=None):
        if app is not None:
            self.app = app
            self.init_app(self.app)
        else:
            self.app = None

    def init_app(self, app):
        self.app = app
        self.app.context_processor(self._inject_users)

    def _inject_users(self):
        return dict(
            create_login_url=self.create_login_url,
            create_logout_url=self.create_logout_url,
            get_current_user=users.get_current_user,
            is_current_user_admin=users.is_current_user_admin)

    def create_login_url(self, url=None):
        """Computes the login URL for redirection.
        """
        if url is None:
            url = request.url
        return users.create_login_url(url)

    def create_logout_url(self, url=None):
        """Computes the logout URL for this request and specified destination URL,
        for both federated login App and Google Accounts App.
        """
        if url is None:
            url = request.url
        return users.create_logout_url(url)


def login_required(func):
    """A decorator to require that a user be logged in to access a view.
    """
    @wraps(func)
    def _login_required(*args, **kwargs):
        user = users.get_current_user()
        if user is None:
            if request.is_xhr:
                raise Unauthorized()
            else:
                return redirect(users.create_login_url(request.url))
        return func(*args, **kwargs)
    return _login_required


def admin_required(func):
    """A decorator to require that a user be admin to access a view.
    """
    @wraps(func)
    def _admin_required(*args, **kwargs):
        if not users.is_current_user_admin():
            user = users.get_current_user()
            if user:
                raise Forbidden()
            elif request.is_xhr:
                raise Unauthorized()
            else:
                return redirect(users.create_login_url(request.url))
        return func(*args, **kwargs)
    return _admin_required


def get_or_404(cls, key):
    model = cls.get(key)
    if not model:
        raise NotFound()
    return model


def get_by_key_name_or_404(cls, key_name):
    model = cls.get_by_key_name(key_name)
    if not model:
        raise NotFound()
    return model


def get_by_id_or_404(cls, id):
    model = cls.get_by_id(id)
    if not model:
        raise NotFound()
    return model


