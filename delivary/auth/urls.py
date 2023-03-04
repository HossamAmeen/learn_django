from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from auth.api import MyObtainTokenPairView, RegisterView, profileAPIView

urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('profile/', profileAPIView.as_view(), name='profile'),
]
