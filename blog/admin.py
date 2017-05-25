# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import BlogPost, BlogPostAdmin

admin.site.register(BlogPost, BlogPostAdmin)
