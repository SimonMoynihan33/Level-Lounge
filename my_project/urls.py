from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500
from level_lounge import views

urlpatterns = [
    path('accounts/', include('allauth.urls')),  # Allauth routes
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path("", include("level_lounge.urls"), name="forum-urls"),
]

# Custom error handlers
handler404 = 'level_lounge.views.custom_404'
handler500 = 'level_lounge.views.custom_500'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
