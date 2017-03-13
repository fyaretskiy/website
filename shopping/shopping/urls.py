from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

for app in settings.LOCAL_APPS:
    urlpatterns += [url(r'^', include(app + '.urls', namespace=app))]
