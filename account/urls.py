
from django.urls import path,include

from .profile import views

urlpatterns = [
    path('', views.index, name="index")),
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.jwt')),
    path('api/profile/', views.ProfileAPIView.as_view()),
]
