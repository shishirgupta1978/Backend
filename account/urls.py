
from django.urls import path,include
from . import views as accountviews
from .profile import views

urlpatterns = [
    path('', accountviews.index, name="index"),
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.jwt')),
    path('api/profile/', views.ProfileAPIView.as_view()),
]
