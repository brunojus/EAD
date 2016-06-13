from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^$','simpleead.core.views.home', name='home'),
    url(r'^admin/', admin.site.urls),
]
