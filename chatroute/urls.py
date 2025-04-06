from django.urls import path
from .views import home, query_view, audio,chat

urlpatterns = [
    path('', home, name='home'),
    path('bs/', query_view ),
    path('audio/', audio),
    path('chat/', chat),
]