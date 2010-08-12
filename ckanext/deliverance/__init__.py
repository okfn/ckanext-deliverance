import logging

log = logging.getLogger(__name__)

from controller import DeliveranceController, DeliveranceException

# monkey-patch pylons a bit:
import pylonspatch

class DeliverancePlugin(object):
    
    def __init__(self, config):
        self.config = config
        log.info("Loading deliverance CMS proxy...")
        if (not 'deliverance.rules' in config) or (not 'deliverance.base' in config):
            raise DeliveranceException("Missing deliverance configuration, must have: deliverance.rules, deliverance.base.")
        
    def make_map_end(self, map):
        
        # not entirely sure about the effects of this on the underlying CMSes:
        map.redirect('/*(url)/', '/{url}',
                     _redirect_code='301 Moved Permanently')
        #import ckanext.deliverance
        map.connect('/*url', controller='ckanext.deliverance:DeliveranceController', 
                             action='view')
        return map
    
    
