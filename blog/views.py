# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
from blog.models import BlogPost

def archive(request):
	posts = BlogPost.objects.all()
	t = loader.get_template("archive.html")
	c = {'posts' : posts }
	return HttpResponse(t.render(c))
