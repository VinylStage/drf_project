from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from users import views

urlpatterns = [
    path('signup/', views.UserView.as_view(), name='UserView'),
    path('mock/', views.mockView.as_view(), name='mock_view'),
    path('api/token/', views.CustomToekonObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('<int:user_id>/', views.ProfileView.as_view(), name='ProfileView'),
    path('follow/<int:user_id>/', views.FollowView.as_view(), name='FollowView'),
]
