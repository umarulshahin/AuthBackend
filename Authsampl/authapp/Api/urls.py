from  authapp.views import *
from django.urls import path


from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    
    path('',getRouter,name="getRouter"),
    path('api/token/', MyTokenobtainedPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]
