from django.conf.urls import url
from .views import home,allreqs,reqdocs

urlpatterns = [
    url(r'^$', home,name='home'),
    url(r'^allreqs/$',allreqs,name='allreqs'),
    url(r'^dcos/(uc\d{3})/$',reqdocs,name='reqdocs'),
]