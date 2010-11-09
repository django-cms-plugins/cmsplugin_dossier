from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
import models 


class CMSDossierPlugin(CMSPluginBase):
    
    model = models.DossierPlugin
    name = _('Dossier')
    render_template = 'cmsplugin_dossier/dossier.html'
    
    class PluginMedia:
        js = ('js/cmsplugin_dossier.js', )
    
    def render(self, context, instance, placeholder):
        context.update({'dossier': instance})
        return context


plugin_pool.register_plugin(CMSDossierPlugin)