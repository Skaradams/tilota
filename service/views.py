from tastypie.resources import ModelResource
from tilota.service import models
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization

__all__ = (
    'GameInfoResource',
    'GameResource',
    'GameHistoryResource',
)

class OnlyUserContentAuthorization(DjangoAuthorization):
    def apply_limits(self, request, object_list):
        if request and hasattr(request, 'user'):
            return object_list.filter(
                user__pk=request.user.pk)
        return object_list.none()


class GameInfoResource(ModelResource):
    class Meta:
        queryset = models.Session.objects.all()
        resource_name = 'game-info'
        allowed_methods = ['get']
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()
    

class GameResource(ModelResource):
    class Meta:
        queryset = models.Session.objects.all()
        resource_name = 'game'
        allowed_methods = ['get', 'post', 'put', 'delete']
        authentication = BasicAuthentication()
        authorization = OnlyUserContentAuthorization()


class GameHistoryResource(ModelResource):
    class Meta:
        queryset = models.Session.objects.all()
        resource_name = 'game-history'
        allowed_methods = ['get', 'post']
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()

