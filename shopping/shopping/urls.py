from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

for app in settings.LOCAL_APPS:
    urlpatterns += [url(r'^', include(app + '.urls', namespace=app))]
