from django.conf.urls.defaults import *
from django.contrib import admin
from tastypie.api import Api
admin.autodiscover()
from tilota.service import views

api = Api(api_name='tilota')
for resource_name in views.__all__:
    api.register(getattr(views, resource_name)())

urlpatterns = patterns('',
    (r'^api/', include(api.urls)),
    (r'^admin/', include(admin.site.urls)),
)
