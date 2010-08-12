import codecs
import os
from pylons import config, request, app_globals as g
from swiss.deliveranceproxy import create_deliverance_proxy

from ckan.lib.base import render, abort, BaseController

class DeliveranceException(Exception): pass

class DeliveranceController(BaseController):

    def view(self, url):
        # wordpress requires trailing '/' (o/w get redirect)
        if config.get('deliverance.add_slash'):
            if not request.environ['PATH_INFO'].endswith('/'):
                request.environ['PATH_INFO'] = request.environ['PATH_INFO'] + '/'
        out_html = self.deliverance(request.environ, self.start_response)
        if config.get('deliverance.replace_url'):
            site_url = config.get('ckan.site_url')
            if site_url:
                if not site_url.endswith('/'):
                    site_url += '/'
                out_html = out_html.replace(config.get('deliverance.base'), site_url)
        return out_html
    
    
    @property
    def deliverance(self):
        if not hasattr(self, '_deliverance'):
            # where we are proxying from
            proxy_base_url = config.get('deliverance.base')
            
            rules_file = config.get('deliverance.rules', 'deliverance_rules.xml')
            if not os.path.exists(rules_file):
                raise DeliveranceException("Cannot find rules: %s" % rules_file)
            rules_fh = codecs.open(rules_file, 'r', 'utf-8')
            rules = rules_fh.read()
            rules_fh.close()
            
            theme_html = render('home/index.html')
            self._deliverance = create_deliverance_proxy(proxy_base_url,
                    theme_html, rules_xml=rules)
        return self._deliverance

