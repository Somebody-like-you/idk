from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('chatroute.urls')),
    path('bs/', include('chatroute.urls')),
    path('upload/', include('chatroute.urls'))
]
