from django.db import models
from django.utils.translation import gettext_lazy as _
from uuid import uuid4
from django.utils.text import slugify
from gi_test.models import AbstractDateTimeFieldBaseModel



class Note(AbstractDateTimeFieldBaseModel):
    title         = models.CharField(_('Title'),max_length=250,null=True, blank=True,db_index=True)
    description   = models.TextField(_('Description'),null=True, blank=True,db_index=True)
    
    def __str__(self):
        return str(self.pk)
    
    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Note"
