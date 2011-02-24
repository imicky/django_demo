from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
    author = models.ForeignKey(User)
    content = models.CharField(max_length='140')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=True, editable=False)
    
    def __unicode__(self):
        return self.content[:30] if self.content else ''
