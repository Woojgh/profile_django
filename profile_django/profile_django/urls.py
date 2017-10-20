
from django.conf.urls import url
from django.contrib import admin
from profile_django import home_view


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_view, name='homepage')
]
