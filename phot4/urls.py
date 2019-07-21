from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$',views.index, name = 'home'),
    url(r'^image/(?P<category_name>\w+)/(?P<image_id>\d+)',views.single_image, name='art'),
    url(r'^location/(?P<location>\d+)', views.location_filter, name='location_filter'),
    url(r'^search', views.search, name='search_images')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
