from django.urls import path
from . import views
from django.urls import include, path


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [url(r'^api/tasks$', views.execute)]


