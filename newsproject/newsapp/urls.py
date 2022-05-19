from django.urls import path
from . import views, views1, views2
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('/homicidios', views1.homicidios, name='homicidios'),
    path('/suicidios', views2.suicidios, name='suicidios'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns = [
#    url(r'^$', views.index, name='site_index'),
 #   ...
#]