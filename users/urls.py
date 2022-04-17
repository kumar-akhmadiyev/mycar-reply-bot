from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.views import MyObtainTokenPairView, UserRegisterView


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
