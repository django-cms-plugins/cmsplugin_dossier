from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _


class DossierPlugin(CMSPlugin):
    
    """
    Simplifies displaying personal data in DjangoCMS 
    """
    
    name = models.CharField(max_length=255, help_text=_('include title if applicable'))
    photo = models.ImageField(blank=True, upload_to='cmsplugin_dossier/photos/')
    description = models.TextField(blank=True)
    
    # in order to get indexed by DjangoCMS
    search_fields = ('name', 'description',)