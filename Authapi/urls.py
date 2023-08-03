from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('api/', include('Auth.urls')),
    path('pokemon/',include('Pokemon.urls')),
     path('recipes/',include('Recipes.urls')),
     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
