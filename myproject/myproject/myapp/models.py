# -*- coding: utf-8 -*-
from django.db import models
from myproject.myapp.storage import OverwriteStorage


class SourceDocument(models.Model):
    docfile = models.FileField(upload_to='documents/source',storage=OverwriteStorage())
    filename = models.CharField(max_length=256, default=True, primary_key=True)

class ObjectDocument(models.Model):
	objname = models.CharField(max_length=256, primary_key=True, default=True)
	stdout = models.CharField(max_length=2048, null=True)
	stderr = models.CharField(max_length=2048, null=True)
	p_status = models.CharField(max_length=2048, null=True)

class ExecuteDocument(models.Model):
	executablename = models.CharField(max_length=256, primary_key=True, default=True)
	stdout = models.CharField(max_length=2048, null=True)
	stderr = models.CharField(max_length=2048, null=True)
	p_status = models.CharField(max_length=2048, null=True)
