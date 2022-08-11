from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'Maktaba MS'
admin.site.index_title = 'Welcome Admin'
admin.site.site_title = 'Admin Panel'

urlpatterns = [
    path('maktaba/', include('staff.urls')),
    path('admin/', admin.site.urls),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)