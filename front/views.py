# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib import auth


def load_auth_template(request, template, context):
    if request.user.is_authenticated():
        t = loader.get_template(template)
        return HttpResponse(t.render(Context(context)))
    return HttpResponseRedirect('/login')


def play(request):
    return load_auth_template(request, 'play.html', {})


def login(request):
    t = loader.get_template('login.html')
    if request.method.lower() == 'post':
        user = auth.authenticate(username=request.POST['username'],
                        password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
    return HttpResponse(t.render(Context(csrf(request))))
