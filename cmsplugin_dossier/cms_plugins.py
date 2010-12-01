from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
import forms 
import models 


class CMSDossierPlugin(CMSPluginBase):
    
    model = models.DossierPlugin
    name = _('Dossier')
    render_template = 'cmsplugin_dossier/dossier.html'
    search_fields = ('name', 'description',)
    
    class PluginMedia:
        js = ('js/cmsplugin_dossier.js', )
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        """Displays description field as WYMEditor """
        
        if db_field.name == 'photo':
            kwargs.pop('request', None)
            kwargs['widget'] = forms.AdminImageWidget
            return db_field.formfield(**kwargs)
        
        from cms.plugins.text.widgets import wymeditor_widget
        if db_field.name == 'description':
            kwargs['widget'] = wymeditor_widget.WYMEditor()
        
        return super(CMSDossierPlugin, self).formfield_for_dbfield(db_field, **kwargs) 
    
    def render(self, context, instance, placeholder):
        context.update({'dossier': instance})
        return context


plugin_pool.register_plugin(CMSDossierPlugin)