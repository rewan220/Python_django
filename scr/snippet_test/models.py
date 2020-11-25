from django.db import models
from django.conf import settings

# Create your models here.
class SnippetTest(models.Model):
    id                   = models.AutoField(primary_key=True)
    title                = models.CharField(max_length=50, null=False, blank=False)
    subject              = models.CharField(max_length=50, null=False, blank=False)
    description          = models.CharField(max_length=5000, null=False, blank=False)
    url                  = models.URLField (max_length=200)
    snippet              = models.TextField(max_length=5000, null=False, blank=False)
    date_published       = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    date_updated         = models.DateTimeField(auto_now=True, verbose_name="date updated")
    author               = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
