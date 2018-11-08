from django.conf.urls import url
from . import views





urlpatterns = [
    
    #path ('',views.index,name='index')
    url(r'^$', views.index) ,
    
    url (r'^(?P<question_id>[0-9]*)/$', views.detail  ),
    url (r'^(?P<question_id>[0-9]*)/results/$', views.results ),
    url (r'^(?P<question_id>[0-9]*)/vote/$', views.vote ),
    
    
    
    
    
     
    
    ]


