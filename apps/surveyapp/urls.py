from django.conf.urls import url 
from . import views
urlpatterns = [
    # url(r'^/$', views.index)
    url(r'^$', views.surveyapp),
    url(r'^name$', views.name),
    url(r'^result$', views.result)
]