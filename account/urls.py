
from django.urls import path,include

from .profile import views

urlpatterns = [
    path('/', include('djoser.urls')),
    path('/', include('djoser.urls.jwt')),
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.jwt')),
    path('api/profile/', views.ProfileAPIView.as_view()),
]
