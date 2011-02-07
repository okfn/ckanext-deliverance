import logging

log = logging.getLogger(__name__)

from ckan.plugins import implements, SingletonPlugin
from ckan.plugins import IRoutes, IConfigurable

from controller import DeliveranceController, DeliveranceException

class DeliveranceRoutes(object):
    implements(IRoutes, inherit=True)
    implements(IConfigurable, inherit=True)
   
    def configure(self, config):
        self.config = config
        log.info("Loading deliverance CMS proxy...")
        if (not 'deliverance.rules' in config) or (not 'deliverance.base' in config):
            raise DeliveranceException("Missing deliverance configuration, must have: deliverance.rules, deliverance.base.")
        
    def after_map(self, map):
        
        # not entirely sure about the effects of this on the underlying CMSes:
        map.redirect('/*(url)/', '/{url}',
                     _redirect_code='301 Moved Permanently')
        #import ckanext.deliverance
        map.connect('/*url', controller='ckanext.deliverance:DeliveranceController', 
                             action='view')
        return map
    
    
