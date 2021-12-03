from django.urls import path
from . import views
from django.urls import include, path
from django.conf.urls import url 

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [url(r'^request/tasks$', views.execute)]


