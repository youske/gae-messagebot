"""`appengine_config` gets loaded when starting a new application instance."""
import vendor
# insert `lib` as a site directory so our `main` module can load
# third-party libraries, and override built-ins with newer
# versions.
vendor.add('lib')
vendor.add('libext')
remoteapi_CUSTOM_ENVIRONMENT_AUTHENTICATION = ('HTTP_X_APPENGINE_INBOUND_APPID',['gae-messagebot'])
