from pylons.wsgiapp import PylonsApp
import pkg_resources
import logging

log = logging.getLogger(__name__)

log.info("Monkey-patching Pylons to allow loading of controllers via entry point mechanism")

find_controller_generic = PylonsApp.find_controller

# This is from pylons 1.0 source, will monkey-patch into 0.9.7
def find_controller(self, controller):
    if controller in self.controller_classes:
        return self.controller_classes[controller]
           
    # Check to see if its a dotted name
    if '.' in controller or ':' in controller:
        mycontroller = pkg_resources.EntryPoint.parse('x=%s' % controller).load(False)
    	self.controller_classes[controller] = mycontroller
    	return mycontroller
    	
    return find_controller_generic(self, controller)
    
PylonsApp.find_controller = find_controller